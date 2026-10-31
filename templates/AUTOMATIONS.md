# Optional scheduled preparation — not installed

Status: no tasks registered by this starter. Configure only after the learner asks,
the real local coaching project is known, and preparation/persistence are tested.

Editable defaults: weekday lesson at 09:00, Saturday review at 10:00,
Europe/Athens. Use the private profile's actual preferences. Inspect existing
tasks before creation; preserve IDs when updating.

## Lesson prompt

```text
Use $codex-coach in this private local coaching project to prepare my next
30–45 minute lesson. Read the learning plan, saved progress, current new project,
and pending session first. Choose one appropriate curriculum outcome, even when
existing projects have no recent activity. Prepare a small guided task, necessary
teaching and synthetic data, declared 0–100 criteria, a new transfer case, and
the first question. The learner makes meaningful decisions; the agent writes code.
Save as ready_awaiting_participation, preserving previous answers and resuming an
unfinished lesson. Record actual sources and missing evidence. Leave answers,
grades, participation, and completion unassessed until real learner interaction.
Keep instruction proposals pending and return a short topic/resume summary.
```

## Review prompt

```text
Use $codex-coach in this private local coaching project to prepare a weekly review
of about 60 minutes. Cover the period since the last completed review, or the last
seven days if none exists. Read actual answers, scores, assistance, the learning
plan, the current new project, and selected readable work evidence. Distinguish
planned/taught/applied/transferred, learner understanding, artifact completion,
agent errors, and missing data. Without actual learner answers, state that learning
progress cannot yet be evaluated. Prepare a new transfer case, next-week priorities,
and at most three supported exact instruction-change proposals. Save the review
ready for discussion, with no invented participation, completion, or scores.
Keep proposals pending until explicitly approved. Return a short summary and the
first review question.
```

## Verification record — fill only in the private workspace

Record real task IDs, project/cwd, status, model, effective timezone, nominal
schedule, actual next-run timestamps, and timestamp of inspection. Record timing
offsets or unsupported independent timezone/exact-schedule controls explicitly.
Test reuse of the same IDs to prevent duplicates. Active status does not establish
a successful run. Keep missed-run recovery unverified until observed. Never write
internal app databases to bypass unavailable scheduling capabilities.
