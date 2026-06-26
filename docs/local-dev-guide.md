# Local Development Guide

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and set `ASSESSMENT_TEST_NUMBER` to the approved challenge number. Do not commit `.env`.

## Useful Commands

```bash
python scripts/list_scenarios.py
python scripts/run_call.py --scenario appointment_basic
python -m pytest
```

## Current Limitation

The project skeleton does not make real phone calls yet. Twilio logic will be added after local scenario behavior is easy to inspect.
