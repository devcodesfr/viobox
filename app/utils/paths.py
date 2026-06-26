"""Common project paths."""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"
CALLS_DIR = DATA_DIR / "calls"
REPORTS_DIR = DATA_DIR / "reports"
