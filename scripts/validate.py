"""Validate package integrity without reading private state or requiring dependencies."""
import re
import sys
from urllib.parse import unquote, urlsplit
from build_prompt import ROOT, SKILL, TEMPLATES, render

def validate():
    failures = []
    public = [p for p in ROOT.rglob("*") if p.is_file() and not any(part.startswith(".") or part == "__pycache__" for part in p.relative_to(ROOT).parts)]
    expected = ROOT / "second-brain/brain-prompt.md"
    if not expected.exists() or expected.read_text(encoding="utf-8") != render():
        failures.append("Standalone prompt differs from canonical sources")
    for name in TEMPLATES:
        if not (SKILL / "templates" / name).is_file():
            failures.append(f"Missing bundled template: {name}")
    if (SKILL / "templates/AGENTS.md").read_bytes() != (SKILL / "templates/CLAUDE.md").read_bytes():
        failures.append("Agent instruction templates diverge")
    entry = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    if not re.match(r"^---\nname: shared-second-brain\ndescription: .+\n---\n", entry):
        failures.append("Invalid skill entrypoint metadata")
    for p in public:
        if p.suffix != ".md":
            continue
        text = p.read_text(encoding="utf-8")
        # Links inside examples/code are literal data, not navigation.
        prose = re.sub(r"```.*?```", "", text, flags=re.S)
        for dest in re.findall(r"(?<!!)\[[^]\n]+\]\(([^)]+)\)", prose):
            if urlsplit(dest).scheme or dest.startswith("#"):
                continue
            target = (p.parent / unquote(dest.split("#", 1)[0])).resolve()
            if not target.is_relative_to(ROOT) or not target.exists():
                failures.append(f"Broken local link in {p.relative_to(ROOT)}: {dest}")
        # Templates and the generated prompt deliberately contain fill-in fields.
        if "templates" not in p.parts and p != expected and re.search(r"\{\{[a-z_]+\}\}", re.sub(r"`[^`]+`", "", prose)):
            failures.append(f"Unresolved template field in {p.relative_to(ROOT)}")
    return failures, len(public)

if __name__ == "__main__":
    problems, count = validate()
    if problems:
        print("\n".join(problems))
        sys.exit(1)
    print(f"PASS: {count} public files; links, skill bundle, template parity and generated prompt.")
