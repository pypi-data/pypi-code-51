#!/usr/bin/env python3
from runpy import run_path
from pathlib import Path

repo_root = Path(__file__).parent.parent
info_file = repo_root / "nipype" / "info.py"
reqs = repo_root / "requirements.txt"

info = run_path(info_file)
requirements = info["REQUIRES"]

script_name = Path(__file__).relative_to(repo_root)

lines = [f"# Auto-generated by {script_name}", ""]

# Write requirements
lines[1:-1] = requirements
reqs.write_text("\n".join(lines))
