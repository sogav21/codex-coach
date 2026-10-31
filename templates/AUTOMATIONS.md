# Optional scheduled preparation — not installed

Status: no tasks registered by this starter. Configure only after the learner asks,
the real local coaching project is known, and preparation/persistence are tested.

Editable defaults: weekday lesson at 09:00, Saturday review at 10:00,
Europe/Athens. Use the private profile's actual preferences. Inspect existing
tasks before creation; preserve IDs when updating.

## Lesson prompt

```text
Use $codex-coach in this private local coaching project to prepare my next
30–45 minute lesson. Read the profile, selected plan for the current local week,
saved progress, current project brief, and pending session first. If the weekly
plan is missing, prepare it with the skill's weekly planning workflow. Follow its
next milestone and resume unfinished work; do not select a different project each
day. Continue even when existing projects have no recent activity. Prepare a small guided task, necessary
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
plan, declared interests and their sources, the current project, and selected
readable work evidence. Distinguish
planned/taught/applied/transferred, learner understanding, artifact completion,
agent errors, and missing data. Without actual learner answers, state that learning
progress cannot yet be evaluated. Autonomously select and plan a new small project
for the coming week from demonstrated skills, prerequisites, interests, and time.
Use initial answers, help, and unseen transfer performance; an assisted final score
does not establish independent mastery. Explain the selection and evidence limits.
Prepare its brief, one or two new concepts, five weekday milestones within the
daily time budget, learner decisions, agent work, acceptance criteria, and a new
transfer case. Leave the learning decisions open. Keep at most one active project;
record the previous project's disposition, or explicitly justify a scoped
continue_project plan and finish condition. Unknown interests or skills require a
provisional diagnostic plan, not invented personalization or grades. Use the next
local Monday as week_id, save next_week_project_plan in the review, and index it
in LEARNING_PLAN.md. Revise the same week's plan after actual review answers and
on reruns, preserving previous revisions and learner history. Also prepare at most
three supported exact instruction-change proposals. Save the review
ready for discussion, with no invented participation, completion, or scores.
Keep proposals pending until explicitly approved. Return a short summary and the
first review question.
```

Weekly project planning belongs to this review task; it does not require another
automation or routine approval of each curriculum choice. Instruction changes
still require the learner's explicit approval. Preparation never records a planned
project as active early, completed, taught, or understood.

## Verification record — fill only in the private workspace

Record real task IDs, project/cwd, status, model, effective timezone, nominal
schedule, actual next-run timestamps, and timestamp of inspection. Record timing
offsets or unsupported independent timezone/exact-schedule controls explicitly.
Test reuse of the same IDs to prevent duplicates. Active status does not establish
a successful run. Keep missed-run recovery unverified until observed. Never write
internal app databases to bypass unavailable scheduling capabilities.
