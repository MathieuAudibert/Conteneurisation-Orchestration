from pathlib import Path
import sys

_here = Path(__file__).resolve()

for parent in _here.parents:
    if parent.name == "src":
        sys.path.insert(0, str(parent.parent))
        break
else:
    sys.path.insert(0, str(_here.parents[2]))