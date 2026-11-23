#!/usr/bin/env python3
"""Compare the public curated list with the SIN provisional inventory.

No network, external dependencies, installation or AI execution.
Checks literal inventory against pinned README, including duplicate handling.
"""
import argparse
import csv
import hashlib
import re
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BASELINE_BLOB = "6c2a529e97ff152ba12b83509f70e0f2542186f4"
EXPECTED_COUNTS = {
    "Open Source": 131,
    "OpenClaw ecosystem": 12,
    "Closed Source": 18,
    "Session managers & parallel runners": 116,
    "Orchestrators & autonomous loops": 62,
    "Agent infrastructure": 151,
}
COLS = [
    "row_id", "section", "entry_name", "entry_url",
    "source_readme_line", "duplicate_of", "technique_hypotheses",
    "domain_hypotheses", "review_wave", "review_state",
    "catalog_readme_blob", "primary_source_commit", "primary_license_state",
    "code_audit", "sandbox_eval", "comments",
]
ITEM = re.compile(r"^- \*\*\[([^]]+)\]\(([^)]+)\)\*\*(.*)$")

def git_blob_sha(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def parse_readme(raw: bytes):
    records = []
    section = ""
    for line_number, line in enumerate(raw.decode("utf-8").splitlines(), 1):
        if line.startswith("### "):
            section = line[4:]
        match = ITEM.match(line)
        if match:
            records.append((section, match.group(1), match.group(2), str(line_number)))
    return records

def validate(entries, rows):
    problems = []
    if len(entries) != 490 or len(rows) != 490:
        problems.append("expected 490 entries/rows")
    if len(set(v[2] for v in entries)) != 485:
        problems.append("expected exactly 485 distinct source URLs")
    if dict(Counter(x[0] for x in entries)) != EXPECTED_COUNTS:
        problems.append("category counts differ from pinned baseline")
    seen_urls = {}
    seen_ids = set()
    for i, (e, row) in enumerate(zip(entries, rows), 1):
        rid = "CLI-" + str(i).zfill(4)
        if row.get("row_id") != rid or rid in seen_ids:
            problems.append("ID mismatch " + str(i))
        seen_ids.add(rid)
        for key, expected in zip(
            ("section", "entry_name", "entry_url", "source_readme_line"), e
        ):
            if row.get(key) != expected:
                problems.append(rid + " source mismatch: " + key)
        first = seen_urls.get(e[2], "")
        if row.get("duplicate_of") != first:
            problems.append(rid + " duplicate mapping wrong")
        seen_urls.setdefault(e[2], rid)
        if row.get("catalog_readme_blob") != BASELINE_BLOB:
            problems.append(rid + " wrong source blob")
        if row.get("review_state") not in {
            "DISCOVERED_README_ONLY", "PRIMARY_NOT_READ", "SOURCE_INSPECTED",
            "CODE_AUDITED", "EVAL_PROPOSED", "SANDBOX_PASS", "BLOCKED", "REJECTED"
        }:
            problems.append(rid + " invalid review state")
        if row.get("review_wave") not in {"W1", "W2", "W3"}:
            problems.append(rid + " invalid wave")
        if not row.get("technique_hypotheses") or not row.get("domain_hypotheses"):
            problems.append(rid + " missing initial hypothesis")
        if row.get("review_state") == "SANDBOX_PASS" and row.get("sandbox_eval") != "PASS":
            problems.append(rid + " claims SANDBOX_PASS without PASS")
        if row.get("review_state") in {"SOURCE_INSPECTED", "CODE_AUDITED", "EVAL_PROPOSED", "SANDBOX_PASS"} and not row.get("primary_source_commit"):
            problems.append(rid + " claims inspection without primary commit")
    return problems

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    raw = (ROOT / "README.md").read_bytes()
    blob = git_blob_sha(raw)
    if blob != BASELINE_BLOB:
        raise SystemExit("FAIL: README changed; pinned baseline " + BASELINE_BLOB + " != " + blob)
    entries = parse_readme(raw)
    with (HERE / "INVENTORY.csv").open("r", encoding="utf-8", newline="") as fp:
        reader = csv.DictReader(fp)
        if reader.fieldnames != COLS:
            raise SystemExit("FAIL: columns mismatch")
        rows = list(reader)
    issues = validate(entries, rows)
    if issues:
        raise SystemExit("FAIL: " + "; ".join(issues[:20]))
    print("PASS: 490 entries, 485 unique URLs, 5 duplicate entries, pinned README and CSV aligned")
    if args.self_test:
        modified = [dict(r) for r in rows]
        modified[1]["row_id"] = modified[0]["row_id"]
        assert validate(entries, modified), "negative test failed: duplicate ID not caught"
        modified = [dict(r) for r in rows]
        modified[0]["review_state"] = "SANDBOX_PASS"
        assert validate(entries, modified), "negative test failed: unproven PASS not caught"
        modified = [dict(r) for r in rows]
        modified[0]["entry_url"] = "https://example.invalid/poison"
        assert validate(entries, modified), "negative test failed: tampered source not caught"
        print("PASS: 3 intentional negative mutations correctly rejected")

if __name__ == "__main__":
    main()
