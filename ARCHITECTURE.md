# Architecture

Viobox is planned as a Twilio + FastAPI voice QA tool. Twilio will call the single approved assessment test number, route speech turns through FastAPI webhooks, and save recordings/transcripts under `data/`. The app will keep per-call state so each test scenario can stay focused on one realistic patient goal.

Conversation behavior will be scripted first for reliability. A small rules engine will select safe patient replies from scenario facts, success criteria, and known recovery paths. Optional LLM assistance may later polish wording or suggest analysis findings, but it must not invent patient facts or fully control the conversation. Final bug reports will be manually reviewed before submission.
