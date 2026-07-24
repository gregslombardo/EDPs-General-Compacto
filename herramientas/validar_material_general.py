"""Valida la ruta canónica y la salud estructural del repositorio.

Uso:
    python herramientas/validar_material_general.py

La carga obligatoria se cuenta exclusivamente dentro de ``GENERAL/``.
La validación no ejecuta celdas ni renderiza animaciones.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GENERAL = ROOT / "GENERAL"

EXPECTED_SECTIONS = {
    "01.01",
    "01.02",
    "01.03",
    "01.04",
    "01.05",
    "01.06",
    "02.01",
    "02.02",
    "02.03",
    "02.04",
    "02.05",
    "02.06",
    "03.01",
    "03.02",
    "03.03",
    "03.04",
    "03.05",
    "03.06",
    "03.07",
    "04.01",
    "04.02",
    "04.03",
    "04.04",
    "04.05",
    "04.06",
    "04.07",
}
EXPECTED_GENERAL = {
    "01.03",
    "01.06",
    "02.01",
    "02.06",
    "03.03",
    "03.05",
    "04.01",
    "04.05",
}

NORMAL_HEADING_RE = re.compile(
    r"(?mi)^\s{0,3}#{1,6}\s+ejercicio\s+normal\s+([0-9.]+)\s*$"
)
GENERAL_HEADING_RE = re.compile(
    r"(?mi)^\s{0,3}#{1,6}\s+problema\s+tipo\s+general\s+([0-9.]+G)\s*$"
)
FIRST_TITLE_RE = re.compile(r"(?m)^\s*#\s+([0-9]{2}\.[0-9]{2})\s+—\s+.+$")
MARKDOWN_IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
HTML_MEDIA_RE = re.compile(
    r"""<(?:source|video|img)\b[^>]*\b(?:src)=["']([^"']+)["']""",
    re.IGNORECASE,
)


def cell_source(cell: dict) -> str:
    value = cell.get("source", "")
    return "".join(value) if isinstance(value, list) else str(value)


def local_resources(text: str) -> list[str]:
    links = MARKDOWN_IMAGE_RE.findall(text) + HTML_MEDIA_RE.findall(text)
    return [
        link
        for link in links
        if not re.match(r"^(?:https?://|data:|attachment:)", link)
    ]


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    valid_all = 0
    extended = 0
    canonical: dict[str, Path] = {}
    normal_total = 0
    general_total = 0

    for path in sorted(ROOT.rglob("*.ipynb")):
        rel = path.relative_to(ROOT).as_posix()
        is_canonical = path.is_relative_to(GENERAL)

        try:
            notebook = json.loads(path.read_text(encoding="utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            errors.append(f"{rel}: no es JSON válido ({exc})")
            continue

        valid_all += 1
        if not is_canonical:
            extended += 1

        markdown = []
        for index, cell in enumerate(notebook.get("cells", []), start=1):
            text = cell_source(cell)
            if cell.get("cell_type") == "markdown":
                markdown.append(text)
                for link in local_resources(text):
                    target = (path.parent / link.split("#", 1)[0]).resolve()
                    if not target.exists():
                        errors.append(
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

        if not is_canonical:
            continue

        full_text = "\n".join(markdown)
        metadata = notebook.get("metadata", {}).get("general_edp", {})
        section = str(metadata.get("section", ""))
        canonical_flag = metadata.get("canonical") is True
        title_match = FIRST_TITLE_RE.search(full_text)
        title_section = title_match.group(1) if title_match else ""
        filename_section = path.name[:5]
        normals = NORMAL_HEADING_RE.findall(full_text)
        generals = GENERAL_HEADING_RE.findall(full_text)

        if not canonical_flag:
            errors.append(f"{rel}: falta metadata general_edp.canonical=true")
        if section not in EXPECTED_SECTIONS:
            errors.append(f"{rel}: sección canónica desconocida: {section!r}")
        elif section in canonical:
            errors.append(
                f"{rel}: duplica la sección {section} de "
                f"{canonical[section].relative_to(ROOT).as_posix()}"
            )
        else:
            canonical[section] = path
        if not (section == filename_section == title_section):
            errors.append(
                f"{rel}: sección, nombre y título no coinciden "
                f"({section!r}, {filename_section!r}, {title_section!r})"
            )
        if len(normals) != 2:
            errors.append(
                f"{rel}: contiene {len(normals)} ejercicios normales; deben ser 2"
            )
        if len(generals) > 1:
            errors.append(
                f"{rel}: contiene {len(generals)} problemas General; máximo 1"
            )

        should_have_general = section in EXPECTED_GENERAL
        if bool(generals) != should_have_general:
            expected = 1 if should_have_general else 0
            errors.append(
                f"{rel}: contiene {len(generals)} problemas General; "
                f"para esta sección deben ser {expected}"
            )

        normal_total += len(normals)
        general_total += len(generals)

    found = set(canonical)
    for section in sorted(EXPECTED_SECTIONS - found):
        errors.append(f"falta el notebook canónico de la sección {section}")
    for section in sorted(found - EXPECTED_SECTIONS):
        errors.append(f"sobra una sección canónica no prevista: {section}")

    if len(canonical) != 26:
        errors.append(f"hay {len(canonical)} notebooks canónicos; deben ser 26")
    if normal_total != 52:
        errors.append(f"hay {normal_total} ejercicios normales; deben ser 52")
    if general_total != 8:
        errors.append(f"hay {general_total} problemas General; deben ser 8")

    print(f"Notebooks JSON válidos en todo el repositorio: {valid_all}")
    print(f"Biblioteca extendida (fuera de GENERAL): {extended}")
    print(f"Notebooks canónicos: {len(canonical)}/26")
    print(f"Ejercicios normales canónicos: {normal_total}/52")
    print(f"Problemas tipo General: {general_total}/8")
    print(f"Errores: {len(errors)}")
    for item in errors:
        print(f"ERROR: {item}")
    print(f"Advertencias: {len(warnings)}")
    for item in warnings:
        print(f"AVISO: {item}")

    return 1 if errors or warnings else 0


if __name__ == "__main__":
    sys.exit(main())
