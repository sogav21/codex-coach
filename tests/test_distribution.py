"""Synthetic privacy regressions; no real learner data or credentials."""
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("distribution", ROOT / "scripts/verify_distribution.py")
distribution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(distribution)


class PublicationGateTests(unittest.TestCase):
    def setUp(self):
        self.payloads = distribution.working_payloads(ROOT)

    def test_clean_distribution_passes(self):
        self.assertEqual(distribution.inspect_payloads(self.payloads), [])

    def test_unexpected_private_file_is_rejected(self):
        self.payloads["sessions/private.json"] = b"{}"
        self.assertTrue(any("Unexpected distribution path" in x
                            for x in distribution.inspect_payloads(self.payloads)))

    def test_credential_in_allowed_file_is_rejected(self):
        self.payloads["README.md"] += ("\n" + "ghp" + "_" + "x" * 36).encode()
        self.assertTrue(any("credential token" in x
                            for x in distribution.inspect_payloads(self.payloads)))

    def test_email_in_allowed_file_is_rejected(self):
        self.payloads["README.md"] += ("\nlearner" + "@" + "example.invalid").encode()
        self.assertTrue(any("email address" in x
                            for x in distribution.inspect_payloads(self.payloads)))

    def test_personal_machine_path_is_rejected(self):
        self.payloads["README.md"] += ("\nC:" + chr(92) + "Users" + chr(92) + "test-person" + chr(92) + "notes").encode()
        self.assertTrue(any("personal home path" in x
                            for x in distribution.inspect_payloads(self.payloads)))

    def test_real_assessment_cannot_replace_blank_template(self):
        path = "templates/sessions/lesson-template.json"
        value = json.loads(self.payloads[path])
        value["assessment_template"]["initial_score"] = 50
        self.payloads[path] = json.dumps(value).encode()
        self.assertTrue(any("Non-blank or invalid session template" in x
                            for x in distribution.inspect_payloads(self.payloads)))

    def test_identifier_in_allowed_file_is_rejected(self):
        identifier = "-".join(["1" * 8, "2" * 4, "3" * 4, "4" * 4, "5" * 12])
        self.payloads["README.md"] += ("\n" + identifier).encode()
        self.assertTrue(any("stored identifier" in x
                            for x in distribution.inspect_payloads(self.payloads)))

    def test_binary_file_is_rejected(self):
        self.payloads["README.md"] = bytes([255, 254, 128])
        self.assertTrue(any("Non-text content" in x
                            for x in distribution.inspect_payloads(self.payloads)))


class GitHistoryPrivacyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="coach-publication-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        for name, raw in distribution.working_payloads(ROOT).items():
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(raw)
        self.run_git("init", "-b", "main")
        self.run_git("config", "core.autocrlf", "false")
        self.run_git("config", "commit.gpgsign", "false")
        (self.root / "empty-hooks").mkdir()
        self.run_git("config", "core.hooksPath", str(self.root / "empty-hooks"))

    def run_git(self, *args, email=None):
        env = os.environ.copy()
        for role in ("AUTHOR", "COMMITTER"):
            env["GIT_" + role + "_NAME"] = "Synthetic contributor"
            env["GIT_" + role + "_EMAIL"] = email or "noreply" + "@" + "github.com"
        return subprocess.run(["git", "-C", str(self.root), *args], env=env,
                              check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def commit(self, email=None):
        # The private-workspace .gitignore intentionally ignores its starter files.
        # Force only the already-reviewed distribution allowlist, never a directory.
        self.run_git("add", "--force", "--", *sorted(distribution.ALLOWED))
        self.run_git("commit", "-m", "Synthetic publication fixture", email=email)

    def test_complete_clean_history_passes(self):
        self.commit()
        issues, count = distribution.inspect_git(self.root)
        self.assertEqual(count, 1)
        self.assertEqual(issues, [])

    def test_private_commit_email_is_rejected(self):
        self.commit(email="private" + "@" + "example.invalid")
        issues, count = distribution.inspect_git(self.root)
        self.assertEqual(count, 1)
        self.assertTrue(any("Personal author/committer email" in issue for issue in issues))

    def test_removed_secret_is_still_found_in_history(self):
        path = self.root / "README.md"
        clean = path.read_bytes()
        path.write_bytes(clean + ("\n" + "ghp" + "_" + "y" * 36).encode())
        self.commit()
        path.write_bytes(clean)
        self.commit()
        issues, count = distribution.inspect_git(self.root)
        self.assertEqual(count, 2)
        self.assertTrue(any("credential token" in issue for issue in issues))

    def test_gitignore_blocks_private_state(self):
        result = self.run_git("check-ignore", "--", "COACH_PROFILE.md", "sessions/personal.json",
                              "sources/work.json", ".env")
        self.assertEqual(len(result.stdout.decode().splitlines()), 4)


if __name__ == "__main__":
    unittest.main()
