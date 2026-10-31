# New learning project: one-room booking tool

Proposed user: coordinator of a shared room.
Need: enter a booking and see whether it is allowed under agreed rules.
First feature: validate and record one booking. Initial boundaries: one room,
synthetic data, no accounts, billing, or real notifications. Storage design is a
later learner decision.

New concepts: testable acceptance criterion and booking rule/flow.
The learner defines behavior, choices, and checks. The agent writes the code only
after the relevant learner decision. Functional completion and understanding are
recorded separately.

| Milestone | Deliverable | Learner decision | Status |
|---|---|---|---|
| M1 | Brief and criteria | When a booking is allowed | Awaiting learner |
| M2 | Success/error flow | Boundary times and invalid input | Planned |
| M3 | First implementation | Agrees the specific small step | Not started |
| M4 | Storage and reload | Required fields and retention | Planned |
| M5 | Acceptance and transfer | Actual evidence and an equipment-loan case | Planned |

Synthetic diagnostic: a booking exists at 10:00–11:00 and a new request is
10:30–11:30. Ask for a rule and reasoning, one question at a time. No personal
decision, acceptance test result, or learner score is assumed by this brief.
