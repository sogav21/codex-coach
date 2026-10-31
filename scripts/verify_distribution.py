"""Check the reusable public distribution without printing sensitive matches."""
from __future__ import annotations

import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
ALLOWED = frozenset({
    ".gitignore", "README.md", "skills/codex-coach/SKILL.md",
    "skills/codex-coach/agents/openai.yaml",
    "skills/codex-coach/references/rubrics.md",
    "templates/.gitignore", "templates/AGENTS.md", "templates/COACH_PROFILE.md",
    "templates/LEARNING_PLAN.md", "templates/CHANGE_PROPOSALS.md",
    "templates/AUTOMATIONS.md", "templates/sessions/lesson-template.json",
    "templates/sessions/review-template.json",
    "templates/learning-projects/room-booking/BRIEF.md",
    "scripts/verify_distribution.py", "tests/test_distribution.py",
})
PATTERNS = {
    "credential token": re.compile(r"\b(?:gh[opsu]_[A-Za-z0-9_]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-(?:proj-)?[A-Za-z0-9_-]{20,}|AKIA[A-Z0-9]{16})"),
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "personal home path": re.compile(r"(?i)(?:[A-Z]:[\\/]Users[\\/][^\s`\"']+|/(?:Users|home)/[^\s/`\"']+/)"),
    "email address": re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    "stored identifier": re.compile(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b", re.I),
    "credential assignment": re.compile(r"(?i)(?:api[_-]?key|access[_-]?token|password)\s*[=:]\s*[\"'][^\"'\s]{8,}[\"']"),
}
ASSESSMENT_NULLS = {"first_answer", "initial_score", "initial_criterion_scores",
                    "final_answer", "final_score", "final_criterion_scores",
                    "transfer_answer", "transfer_score", "help_level"}


def inspect_payloads(payloads: dict[str, bytes]) -> list[str]:
    issues = []
    for path in sorted(set(payloads) - ALLOWED):
        issues.append(f"Unexpected distribution path: {path}")
    for path in sorted(ALLOWED - set(payloads)):
        issues.append(f"Missing distribution path: {path}")
    for path, raw in payloads.items():
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            issues.append(f"Non-text content: {path}")
            continue
        for label, pattern in PATTERNS.items():
            if pattern.search(text):
                issues.append(f"{label}: {path}")
        if path.startswith("templates/sessions/") and path.endswith(".json"):
            try:
                data = json.loads(text)
                assert data["status"] == "template"
                assert data["id"] is None and data["created_at"] is None
                assert data["participation"] is False and data["completed"] is False

                def blank(value):
                    if isinstance(value, dict):
                        for key, item in value.items():
                            if key in ASSESSMENT_NULLS:
                                assert item is None
                            if key in {"help", "user_decisions", "personal_decisions",
                                       "scores", "help_recorded", "taught", "applied",
                                       "transferred", "evidence", "work_review"}:
                                assert item == []
                            if key in {"answer", "score"}:
                                assert item is None
                            if key == "real_answers":
                                assert item == 0
                            blank(item)
                    elif isinstance(value, list):
                        for item in value:
                            blank(item)
                blank(data)
                if data["kind"] == "lesson":
                    assert data["questions"] == []
            except (ValueError, KeyError, AssertionError, TypeError):
                issues.append(f"Non-blank or invalid session template: {path}")
    return issues


def working_payloads(root: Path) -> dict[str, bytes]:
    payloads = {}
    for path in root.rglob("*"):
        rel = path.relative_to(root)
        if ".git" in rel.parts or "__pycache__" in rel.parts:
            continue
        if path.is_symlink():
            raise ValueError("Symlink found in distribution")
        if path.is_file():
            payloads[rel.as_posix()] = path.read_bytes()
    return payloads


def git(root: Path, *args: str) -> bytes:
    return subprocess.run(["git", "-C", str(root), *args], check=True,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout


def inspect_git(root: Path) -> tuple[list[str], int]:
    issues = []
    if not (root / ".git").exists():
        return issues, 0
    for name in git(root, "ls-files", "-z").decode("utf-8").split("\0"):
        if name and name not in ALLOWED:
            issues.append(f"Unexpected indexed path: {name}")
    commits = git(root, "rev-list", "--all").decode("ascii").splitlines()
    for commit in commits:
        names = git(root, "ls-tree", "-r", "--name-only", "-z", commit).decode("utf-8").split("\0")
        payloads = {name: git(root, "show", f"{commit}:{name}") for name in names if name}
        issues.extend(f"Commit {commit}: {issue}" for issue in inspect_payloads(payloads))
        emails = git(root, "show", "-s", "--format=%ae%n%ce", commit).decode("utf-8").splitlines()
        for email in emails:
            if email != "noreply" + "@" + "github.com" and not re.fullmatch(
                    r"(?:[0-9]+\+)?[A-Za-z0-9-]+@users\.noreply\.github\.com", email):
                issues.append(f"Personal author/committer email in commit {commit}")
        message = git(root, "show", "-s", "--format=%B%n%an%n%cn", commit).decode("utf-8")
        for label, pattern in PATTERNS.items():
            if pattern.search(message):
                issues.append(f"{label} in commit metadata {commit}")
    return issues, len(commits)


def main() -> int:
    try:
        payloads = working_payloads(ROOT)
        issues = inspect_payloads(payloads)
        history_issues, commit_count = inspect_git(ROOT)
        issues.extend(history_issues)
    except (OSError, ValueError, subprocess.SubprocessError):
        print("FAIL: publication inspection could not complete", file=sys.stderr)
        return 1
    if issues:
        for issue in issues:
            print(f"FAIL: {issue}", file=sys.stderr)
        return 1
    print(f"PASS: {len(payloads)} reviewed files; {commit_count} Git commits; blank learner templates")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
