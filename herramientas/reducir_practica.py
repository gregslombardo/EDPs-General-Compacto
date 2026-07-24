"""Reduce la práctica de cada notebook a una ruta realizable.

Conserva como máximo dos ejercicios normales por notebook. Sólo mantiene un
tercer ejercicio de nivel General en los temas que los exámenes históricos
señalan como prioritarios. No modifica teoría, ejemplos ni demostraciones.

Uso:
    python herramientas/reducir_practica.py
"""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SEARCH_DIRS = ("calor", "LINEALES", "ONDA")

# El General histórico alterna estos núcleos. Los demás notebooks sirven para
# teoría y práctica corta, sin convertir cada sección en un simulacro.
GENERAL_PRIORITY = {
    "calor/03_04.03_Principio_debil_del_maximo.ipynb",
    "calor/07_04.07_Cauchy_no_homogeneo_y_Duhamel.ipynb",
    "calor/11_04.11_Problemas_iniciales_y_de_frontera.ipynb",
    "LINEALES/2.1.1_Transporte_constante (1).ipynb",
    "LINEALES/2.3.1_Ecuaciones_cuasilineales_y_sistema_caracteristico.ipynb",
    "LINEALES/2.5.1_Soluciones_debiles_y_Rankine_Hugoniot.ipynb",
    "LINEALES/2.6.2_Problema_de_Riemann.ipynb",
    "LINEALES/2.8.1_Burgers_y_modelo_LWR.ipynb",
    "ONDA/02_01_Cauchy_global_y_dAlembert (1).ipynb",
    "ONDA/02_01_Cauchy_global_y_dAlembert_ejecutado.ipynb",
    "ONDA/02_10_Dimension_dos_y_descenso_de_Hadamard (1).ipynb",
}

HEADING_RE = re.compile(r"(?m)^(?P<marks>#{1,6})[ \t]+(?P<title>[^\r\n]+)")
EXERCISE_TITLE_RE = re.compile(
    r"(?i)^\**\s*(?:"
    r"ejercicio(?:\s+normal)?\b|"
    r"problema\s+tipo\s+general\b|"
    r"★\s*variación\s+de\s+nivel\s+general\b"
    r")"
)
GENERAL_RE = re.compile(r"(?i)\b(?:examen\s+general|tipo\s+general|nivel\s+general)\b")


def source_text(cell: dict) -> str:
    source = cell.get("source", "")
    return "".join(source) if isinstance(source, list) else str(source)


def replace_source(cell: dict, text: str) -> None:
    # Una lista de líneas mantiene diffs legibles y es el formato usual de nbformat.
    cell["source"] = text.splitlines(keepends=True)


def trim_cell(text: str, keep_general: bool) -> tuple[str, int]:
    headings = list(HEADING_RE.finditer(text))
    exercises = [
        (index, match)
        for index, match in enumerate(headings)
        if EXERCISE_TITLE_RE.search(match.group("title"))
    ]
    if len(exercises) <= 2:
        return text, 0

    normal_indexes = [
        index
        for index, match in exercises
        if not GENERAL_RE.search(match.group("title"))
    ][:2]
    general_indexes = [
        index
        for index, match in exercises
        if GENERAL_RE.search(match.group("title"))
    ][:1]
    selected = set(normal_indexes)
    if keep_general:
        selected.update(general_indexes)

    remove_ranges: list[tuple[int, int]] = []
    for position, (heading_index, match) in enumerate(exercises):
        if heading_index in selected:
            continue
        start = match.start()
        if position + 1 < len(exercises):
            end = exercises[position + 1][1].start()
        else:
            level = len(match.group("marks"))
            end = len(text)
            for following in headings[heading_index + 1 :]:
                if len(following.group("marks")) <= level:
                    end = following.start()
                    break
        remove_ranges.append((start, end))

    for start, end in reversed(remove_ranges):
        text = text[:start] + text[end:]
    return text, len(remove_ranges)


def main() -> None:
    changed_files = 0
    removed_exercises = 0

    for directory in SEARCH_DIRS:
        for path in sorted((ROOT / directory).rglob("*.ipynb")):
            notebook = json.loads(path.read_text(encoding="utf-8"))
            relative = path.relative_to(ROOT).as_posix()
            changed = False
            for cell in notebook.get("cells", []):
                if cell.get("cell_type") != "markdown":
                    continue
                original = source_text(cell)
                reduced, removed = trim_cell(
                    original, keep_general=relative in GENERAL_PRIORITY
                )
                if removed:
                    replace_source(cell, reduced)
                    removed_exercises += removed
                    changed = True
            if changed:
                path.write_text(
                    json.dumps(notebook, ensure_ascii=False, indent=1) + "\n",
                    encoding="utf-8",
                )
                changed_files += 1

    print(f"Notebooks reducidos: {changed_files}")
    print(f"Ejercicios retirados de la ruta corta: {removed_exercises}")


if __name__ == "__main__":
    main()
