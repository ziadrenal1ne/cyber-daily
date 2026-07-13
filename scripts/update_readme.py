from pathlib import Path
from datetime import datetime , UTC
import re

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"

today = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

content = README.read_text(encoding="utf-8")

badge = f"**Last automated update:** {today}"

pattern = r"\*\*Last automated update:\*\*.*"

if re.search(pattern, content):
    content = re.sub(pattern, badge, content)
else:
    content += f"\n\n---\n\n{badge}\n"

README.write_text(content, encoding="utf-8")

print("README updated successfully.")
