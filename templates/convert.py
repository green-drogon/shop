from pathlib import Path
import re

patterns = [
    (r"\./assets/", ""),
    (r"assets/", ""),
]

for file in Path(".").rglob("*.html"):
    text = file.read_text(encoding="utf-8")
    original = text

    for old, new in patterns:
        text = re.sub(old, new, text)

    if text != original:
        file.write_text(text, encoding="utf-8")
        print(f"✔ Fixed: {file}")

print("\n========== Remaining assets references ==========\n")

for file in Path(".").rglob("*.html"):
    text = file.read_text(encoding="utf-8")

    if "assets/" in text or "./assets/" in text:
        print(f"⚠ Still contains assets/: {file}")