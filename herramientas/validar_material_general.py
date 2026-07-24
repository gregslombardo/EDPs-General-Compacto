"""Valida estructura, recursos y tamaño de la práctica para el General.

Uso:
    python herramientas/validar_material_general.py

La validación no ejecuta celdas ni renderiza animaciones.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HEADING_RE = re.compile(r"(?m)^\s{0,3}#{1,6}\s+(?P<title>[^\r\n]+)")
EXERCISE_TITLE_RE = re.compile(
    r"(?i)^\**\s*(?:"
    r"ejercicio(?:\s+normal)?\b|"
    r"problema\s+tipo\s+general\b|"
    r"★\s*variación\s+de\s+nivel\s+general\b"
    r")"
)
GENERAL_RE = re.compile(r"(?i)\b(?:examen\s+general|tipo\s+general|nivel\s+general)\b")
IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")


def cell_source(cell: dict) -> str:
    value = cell.get("source", "")
    return "".join(value) if isinstance(value, list) else str(value)


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    hashes: dict[str, list[str]] = defaultdict(list)
    checked = 0
    total_exercises = 0
    total_general = 0

    for path in sorted(ROOT.rglob("*.ipynb")):
        rel = path.relative_to(ROOT).as_posix()
        raw = path.read_bytes()
        hashes[hashlib.sha256(raw).hexdigest()].append(rel)

        try:
            notebook = json.loads(raw)
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            errors.append(f"{rel}: no es un notebook JSON válido ({exc})")
            continue

        checked += 1
        exercise_count = 0
        general_count = 0
        is_legacy = False

        for index, cell in enumerate(notebook.get("cells", []), start=1):
            text = cell_source(cell)

            if index == 1 and re.search(r"(?i)archivo\s+legado", text):
                is_legacy = True

            if cell.get("cell_type") == "markdown":
                for heading in HEADING_RE.finditer(text):
                    title = heading.group("title")
                    if EXERCISE_TITLE_RE.search(title):
                        exercise_count += 1
                        if GENERAL_RE.search(title):
                            general_count += 1

                for link in IMAGE_RE.findall(text):
                    if re.match(r"^(?:https?://|data:|attachment:)", link):
                        continue
                    target = path.parent / link.split("#", 1)[0]
                    if not target.exists():
                        warnings.append(
                            f"{rel}: celda {index}, recurso local ausente: {link}"
                        )

            if cell.get("cell_type") == "code":
                stripped = text.strip()
                if stripped and len(stripped) <= 4:
                    errors.append(
                        f"{rel}: celda {index}, código sospechosamente corto: "
                        f"{stripped!r}"
                    )
                for output in cell.get("outputs", []):
                    if output.get("output_type") == "error":
                        errors.append(
                            f"{rel}: celda {index} conserva una salida de error"
                        )

        if not is_legacy:
            total_exercises += exercise_count
            total_general += general_count
            if exercise_count > 3:
                warnings.append(
                    f"{rel}: {exercise_count} ejercicios; objetivo máximo: 3"
                )
            if general_count > 1:
                warnings.append(
                    f"{rel}: {general_count} ejercicios de nivel General; "
                    "objetivo máximo: 1"
                )

    for paths in hashes.values():
        if len(paths) > 1:
            warnings.append("notebooks exactamente duplicados: " + " | ".join(paths))

    print(f"Notebooks válidos revisados: {checked}")
    print(f"Ejercicios en la ruta activa: {total_exercises}")
    print(f"Ejercicios de nivel General: {total_general}")
    print(f"Errores: {len(errors)}")
    for item in errors:
        print(f"ERROR: {item}")
    print(f"Advertencias: {len(warnings)}")
    for item in warnings:
        print(f"AVISO: {item}")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
