"""List available Viobox scenarios."""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from app.scenarios.registry import list_scenarios


def main() -> None:
    for scenario in list_scenarios():
        print(f"{scenario.id}\t{scenario.title}")


if __name__ == "__main__":
    main()
