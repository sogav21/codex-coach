# Codex Coach

A reusable Codex skill for learning to build with an AI coding agent.
The learner decides what to build, explains design choices, and evaluates evidence;
the agent writes the code. Lessons use one question at a time and preserve progress
across chats without treating generated code as proof of the learner's understanding.

This v1.1 starter includes a coaching skill, scoring rubrics, blank private-workspace
templates, and a two-week curriculum with a new room-booking project.
It contains no real learner profile, chat history, answers, scores, project inventory,
machine paths, or active automation registrations.

## Install

1. Clone or download this repository. Copy `skills/codex-coach` into your personal
   Codex skill directory, normally `~/.agents/skills/codex-coach`.
   If this installation already uses another supported user skill directory, use
   that directory instead. Keep only one installed copy with this skill name.
2. Make a separate **private local folder** for coaching. Copy the contents of
   `templates/` into it. Do not use this public distribution checkout to store
   learner progress. Review the new `AGENTS.md` before adopting it; merge rather
   than overwrite if the destination already has instructions.
3. Open that folder as a local project in Codex. Start a chat with:

   ```text
   Use $codex-coach. Initialize my coaching profile and learning plan from the
   blank templates, confirm which project evidence is actually accessible,
   and begin an ungraded diagnostic with one question at a time.
   ```

4. Set your preferred language, goals, available learning time, and timezone in
   the private profile. The starter uses Greek and Europe/Athens as editable
   examples; it has no assumed learner identity or registered project IDs.

Codex normally detects skill changes automatically. If the skill does not appear,
restart the app. See the [official skills documentation](https://learn.chatgpt.com/docs/build-skills).

## What the coach does

- Prepares lessons from the curriculum even when existing projects have no recent work.
- Guides one small new project at a time and leaves meaningful decisions to the learner.
- Records first answers, initial scores, help, final answers, and new-example performance
  separately. Missing answers remain unassessed, rather than receiving a zero.
- Prepares weekly reviews that distinguish planned, taught, applied, and transferred knowledge.
- Keeps instruction-change proposals pending until the learner approves their exact scope.
- Reloads saved sessions and resumes unfinished lessons instead of creating daily duplicates.

Scores use declared rubrics; they are estimates of demonstrated understanding.
Initial exploration of unfamiliar material can remain ungraded. The learner's
progress and the functional state of the agent's software are separate records.

## Scheduling is optional and requires local setup

No automation is installed by cloning this repository. After testing preparation
and persistence in the private workspace, ask Codex to create the two local project
tasks described in `AUTOMATIONS.md`: weekday lessons and a Saturday review.
The template times are 09:00 and 10:00 in Europe/Athens; change them as needed.

Verify actual IDs, project, status, effective timezone, nominal times, and next
scheduled timestamps. A scheduler can apply timing offsets or use the computer's
timezone rather than store a separate IANA timezone. Report such limits explicitly;
do not promise exact timing, DST behavior, or catch-up for missed runs without evidence.
Local-file tasks require the computer and app to be available. See
[official scheduling documentation](https://learn.chatgpt.com/docs/automations).

## Privacy and publication checks

The distribution is separate from the private coaching workspace. Its `.gitignore`
allows only the explicit reusable file set. This reduces accidental staging of
profiles, sessions, source evidence, credentials, and generated reports; already
tracked files are still checked by the verifier.

Run before publishing:

```text
python scripts/verify_distribution.py
python -m unittest discover -s tests -v
```

The verifier checks the exact distribution inventory, blank learner fields, content
patterns, and all Git commits, including author/committer email metadata. It reports
file paths or commit IDs, without printing matching sensitive content. Pattern checks
are a guardrail, not a guarantee that arbitrary free text has no personal information.
Review every staged file as well. Never publish a private coaching workspace.

## Layout

```text
skills/codex-coach/    Reusable teaching workflow and rubrics
templates/            Clean starter files for a separate private workspace
scripts/              Read-only publication verification
tests/                Privacy-gate regression tests with synthetic data only
```

The public starter's structural checks do not establish a learning outcome or a
future scheduled execution. Real coaching requires real learner participation.
