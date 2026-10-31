# Learning plan — v1.2 starter

Status: planned, not yet taught. Start with an ungraded diagnostic in clear
delegation, failure diagnosis, and evidence-based evaluation. The coach chooses
weekly projects from declared interests, actual skill evidence, prerequisites,
and available time. Existing work is useful evidence, not the whole curriculum.

| Topic | Prerequisite | Example exercise | Evidence of understanding |
|---|---|---|---|
| Problem and product | None | Brief for a small tool | Defines user, need, useful first result, and boundaries |
| User flow | A clear need | Booking success/error flow | Explains behavior for invalid input |
| Data and quality | A flow | Fields and a synthetic CSV | Finds gaps/duplicates and verifies a total |
| App structure | Flow and data | Separate display, rules, storage | Explains where a rule belongs |
| APIs and automation | Data and storage | Repeated request and timeout | Specifies failure and duplicate handling |
| AI and evaluation | Evidence checks | Distinguish sources and claims | Designs a new check and leaves missing evidence open |
| Versions and reliability | A small app | Change checks and recovery | Explains acceptance and rollback criteria |

## Weekly selection and saved plan

Every Saturday, prepare a new small project for the coming week without asking
the learner to select one. Connect a declared interest to an evidenced learning
need and one or two new concepts; explain the difficulty and prerequisites. Read
first answers, initial scores, help, and unseen transfer results, not just assisted
final scores. Record uncertainty. No answer means unknown, not failure.

Use the local Monday date (YYYY-MM-DD) as week_id. Store the full
next_week_project_plan in the dated review, and keep its current reference here:

| Week | Revision | Review / plan record | Project brief | Selection | State |
|---|---|---|---|---|---|
| Not scheduled | None | None | None selected | None | Not prepared |

Keep one current plan per week. Update its revision and preserve the previous
plan in revision_history when actual review answers change it. A rerun with no
new evidence should reuse the same plan. Saturday preparation selects the next
week's project; it does not activate a second project during the current week.
Daily preparation follows the appropriate week's plan and resumes its next
unfinished step. If that week's plan is missing, prepare one for the current
week with the same workflow rather than waiting until the next Saturday.
For midweek recovery, reduce scope and steps to the remaining learning days;
elapsed days are not evidence of completed work or failed learning.

Keep at most one active educational project. Record the previous project's
completion, explicit deferral, or closure before activating a new one. If it is
better to continue, use continue_project, explain why, scope the remaining work,
and define a finish condition. Repeated carryover requires rescoping or explicit
deferral; do not silently abandon work or accumulate parallel projects.
Update affected pending-session states and profile pointers on deferral or
closure, preserving answers so an old lesson cannot reactivate the project.

If interests are unknown, ask one initial question during interaction. Background
preparation can use a neutral provisional candidate. If skills are unknown, use a
small diagnostic project and provisional difficulty. Neither case justifies
inventing preferences, scores, prior teaching, or demonstrated ability.

## Required weekly project brief

Record the useful artifact, learning outcomes, reason for selection, interest
sources, skill evidence and its limits, prerequisites, difficulty, one or two new
concepts, five weekday steps within the daily time budget, learner decisions,
agent work, acceptance criteria, a new transfer case, and exclusions. Leave the
decisions being taught open. The coach plans the exercise; the learner defines
the relevant requirements and checks before the agent implements them.

## Neutral one-week example — not selected or personalized

Candidate: learning-projects/room-booking/BRIEF.md. The coach may choose a
completely different project when interests and evidence are available. This
example is not a timetable the learner must follow or a promise of completion.

| Session | Activity / small deliverable | Learner decision | Budget |
|---|---|---|---|
| Monday | Diagnostic, one new concept, M1 brief | User, boundaries, observable success | 30–45 min |
| Tuesday | M2 success/error flow | Overlap and invalid time behavior | 30–45 min |
| Wednesday | M3 agent implements the agreed small step | Scope and checks before implementation | 30–45 min |
| Thursday | M4 failure investigation with synthetic evidence | A check that separates two possible causes | 30–45 min |
| Friday | M5 acceptance and unseen transfer | What evidence supports acceptance and what is unknown | 30–45 min |
| Saturday | Review and autonomous plan for the next week | Explain learning and update interests if needed | About 60 min |

All sessions are initially planned. No concepts are recorded as taught, applied,
or transferred. Track artifact completion separately from understanding. Resume
or explicitly defer unfinished lessons without discarding answers. Adjust scope
to the actual time available; do not add a second curriculum alongside the project.
