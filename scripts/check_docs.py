from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
TEXT_FILES = [
    *ROOT.rglob("*.md"),
    *ROOT.rglob("*.csv"),
    *ROOT.rglob("*.yml"),
    *ROOT.rglob("*.yaml"),
]
SKIP_PARTS = {".git"}
PRIVATE_TERMS = (
    "Abhinav Raj",
    "Lakshay Kapoor",
)


def relevant(path: Path) -> bool:
    return not any(part in SKIP_PARTS for part in path.parts)


def check_links(path: Path, text: str) -> list[str]:
    errors = []
    for target in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", text):
        target = target.strip().split(" ", 1)[0]
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        file_part = unquote(target.split("#", 1)[0])
        if file_part and not (path.parent / file_part).resolve().exists():
            errors.append(f"{path.relative_to(ROOT)}: broken link to {target}")
    return errors


def main() -> int:
    errors: list[str] = []
    checked_files = sorted({p for p in TEXT_FILES if relevant(p)})
    for path in checked_files:
        text = path.read_text(encoding="utf-8")
        if "—" in text or "–" in text:
            errors.append(f"{path.relative_to(ROOT)}: contains an em dash or en dash")
        for term in PRIVATE_TERMS:
            if term in text:
                errors.append(
                    f"{path.relative_to(ROOT)}: contains private candidate name {term}"
                )
        errors.extend(check_links(path, text))

    if errors:
        print("Playbook checks failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Playbook checks passed for {len(checked_files)} files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
