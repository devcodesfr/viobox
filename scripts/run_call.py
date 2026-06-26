"""Preview a scenario without making a real phone call."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from app.scenarios.registry import get_scenario


def main() -> None:
    parser = argparse.ArgumentParser(description="Preview a Viobox scenario.")
    parser.add_argument("--scenario", required=True, help="Scenario ID to preview.")
    args = parser.parse_args()

    scenario = get_scenario(args.scenario)
    print(f"{scenario.id}: {scenario.title}")
    print(f"Goal: {scenario.goal}")
    print(f"Opening: {scenario.opening_line}")
    print("No phone call was made. Twilio logic is not implemented yet.")


if __name__ == "__main__":
    main()
