# Viobox

Viobox is a Python voice QA caller for a job build challenge. The goal is to call one approved assessment test number, run realistic fake-patient conversations, record and transcribe the calls, and turn the results into clear bug reports.

This repo is currently the project skeleton and local-first challenge setup. It does not place real phone calls yet. The first milestone is coherent scenario design, safe configuration, and scripts that make local development predictable before Twilio call logic is added.

## Current Status

- Scripted fake-patient scenarios are defined in code.
- Local scripts can list scenarios and preview one selected scenario.
- Config validation refuses any target number except `ASSESSMENT_TEST_NUMBER`.
- Data folders are prepared for future recordings, transcripts, and reports.
- Tests cover basic config and scenario behavior.

## Quick Start

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python scripts/list_scenarios.py
python scripts/run_call.py --scenario appointment_basic
python -m pytest
```

## Safety Note

The first commit intentionally avoids real Twilio call logic. No script should make a phone call until the calling layer is implemented and tested against the single allowed assessment number.
