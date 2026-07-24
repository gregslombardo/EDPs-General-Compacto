"""Sustituye imágenes locales ausentes por una nota verificable.

No fabrica capturas ni atribuye una imagen equivocada a una fuente. Conserva
la descripción y la ruta original para que pueda restaurarse si aparece el
material fuente.
"""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")


def source_text(cell: dict) -> str:
    source = cell.get("source", "")
    return "".join(source) if isinstance(source, list) else str(source)


def main() -> None:
    changed = 0
    replaced = 0

    for path in sorted(ROOT.rglob("*.ipynb")):
        notebook = json.loads(path.read_text(encoding="utf-8"))
        notebook_changed = False

        for cell in notebook.get("cells", []):
            if cell.get("cell_type") != "markdown":
                continue
            text = source_text(cell)

            def replacement(match: re.Match[str]) -> str:
                nonlocal replaced, notebook_changed
                alt, link = match.groups()
                if re.match(r"^(?:https?://|data:|attachment:)", link):
                    return match.group(0)
                if (path.parent / link.split("#", 1)[0]).exists():
                    return match.group(0)
                replaced += 1
                notebook_changed = True
                label = alt.strip() or "imagen de apoyo"
                return (
                    f"> **Fuente visual no incluida en el repositorio:** {label}. "
                    f"Referencia original: `{link}`."
                )

            updated = IMAGE_RE.sub(replacement, text)
            if updated != text:
                cell["source"] = updated.splitlines(keepends=True)

        if notebook_changed:
            path.write_text(
                json.dumps(notebook, ensure_ascii=False, indent=1) + "\n",
                encoding="utf-8",
            )
            changed += 1

    print(f"Notebooks corregidos: {changed}")
    print(f"Referencias sustituidas: {replaced}")


if __name__ == "__main__":
    main()
