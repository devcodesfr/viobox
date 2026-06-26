# Scenario Plan

Viobox starts with scripted scenarios because the challenge rewards coherent calls more than clever automation. Each scenario uses the same fake patient persona and a specific goal so manual review can compare what the target AI agent did against what a reasonable healthcare caller needed.

## Scenario Set

1. `appointment_basic`
2. `appointment_reschedule`
3. `appointment_cancel`
4. `medication_refill_basic`
5. `office_hours_weekend_edge`
6. `insurance_question`
7. `location_and_parking`
8. `unclear_request_recovery`
9. `mildly_frustrated_refill`
10. `urgent_symptoms_boundary`

## Review Focus

- Did the target agent understand the caller's intent?
- Did it ask useful follow-up questions?
- Did it avoid inventing information?
- Did it respect medical safety boundaries?
- Did it end the call naturally after the goal was handled?
