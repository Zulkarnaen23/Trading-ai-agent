#!/usr/bin/env python3
"""Validate Advanced Company Trading Team files."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent

REQUIRED_FILES = [
    ROOT / "README.md",
    ROOT / "WORKFLOW.md",
    ROOT / "AGENTS.md",
    ROOT / "config" / "company-trading-team.json",
    ROOT / "prompts" / "company-system-prompt.md",
    ROOT / "protocols" / "operating-protocol.md",
    ROOT / "protocols" / "information-access-policy.md",
]

SECRET_PATTERNS = [
    re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"ghp_[A-Za-z0-9_]{20,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"ANTHROPIC_API_KEY\s*=\s*[^\s]+"),
    re.compile(r"OPENAI_API_KEY\s*=\s*[^\s]+"),
    re.compile(r"DEEPSEEK_API_KEY\s*=\s*[^\s]+"),
]


def fail(message: str) -> None:
    raise SystemExit(f"VALIDATION_FAILED: {message}")


def validate_required_files() -> None:
    missing = [str(path.relative_to(REPO)) for path in REQUIRED_FILES if not path.exists()]
    if missing:
        fail("Missing files: " + ", ".join(missing))


def validate_json_config() -> None:
    config_path = ROOT / "config" / "company-trading-team.json"
    data = json.loads(config_path.read_text(encoding="utf-8"))

    required_keys = ["company_name", "version", "mode", "roles", "decision_statuses", "required_gates"]
    for key in required_keys:
        if key not in data:
            fail(f"Missing config key: {key}")

    if len(data["roles"]) < 10:
        fail("Expected at least 10 agent roles")

    expected_statuses = {"VALID", "WAIT", "REJECT", "NEEDS_DATA", "NEEDS_BACKTEST"}
    if set(data["decision_statuses"]) != expected_statuses:
        fail("Decision statuses do not match required set")


def validate_no_hardcoded_secrets() -> None:
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                fail(f"Possible hardcoded secret in {path.relative_to(REPO)}")


def validate_markdown_keywords() -> None:
    workflow = (ROOT / "WORKFLOW.md").read_text(encoding="utf-8")
    for keyword in ["Source Verification", "Risk Review", "Final Committee Review"]:
        if keyword not in workflow:
            fail(f"WORKFLOW.md missing keyword: {keyword}")


def main() -> None:
    validate_required_files()
    validate_json_config()
    validate_no_hardcoded_secrets()
    validate_markdown_keywords()
    print("Advanced Company Trading Team validation passed.")


if __name__ == "__main__":
    main()
