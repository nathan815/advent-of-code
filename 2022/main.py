from datetime import datetime
import importlib
from pathlib import Path

# Find and run all solution files

SOLUTION_FILE_NAMES = ["part1.py", "part2.py", "solution.py"]

# Filter and then sort day directories correctly (by int value)
sorted_paths = sorted(
    filter(
        lambda p: p.name.startswith("day"),
        Path(".").iterdir(),
    ),
    key=lambda p: int(p.name.replace("day", "")),
)

for path in sorted_paths:
    for file in path.iterdir():
        if file.name in SOLUTION_FILE_NAMES:
            filepath = str(file)
            print(f"--- Running {filepath} ---")
            modname = filepath.replace("/", ".").replace(".py", "").lstrip(".")
            mod = importlib.import_module(modname)
            if hasattr(mod, "run"):
                start = datetime.now()
                mod.run()
                runtime = datetime.now() - start
                print()
                print("Runtime:", runtime)
            else:
                print("ERROR: Missing run() function!")
            print()
