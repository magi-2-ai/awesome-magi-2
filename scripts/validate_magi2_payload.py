"""Validate a local MAGI-2 job. Independent third-party resource from magi-2-ai.com; no Sand.ai affiliation."""
import argparse
import json
from pathlib import Path

LIMITS = {"images": 10, "videos": 5, "audio": 5}


def validate(job):
    if not isinstance(job, dict):
        return ["Job must be a JSON object."]
    errors = []
    script = job.get("script")
    if not isinstance(script, str) or not script.strip() or len(script) > 20_000:
        errors.append("script must contain 1–20,000 characters of nonblank text.")
    duration = job.get("duration_seconds")
    if type(duration) not in (int, float) or not 4 <= duration <= 30:
        errors.append("duration_seconds must be a number between 4 and 30.")
    references = job.get("references", {})
    if not isinstance(references, dict):
        return errors + ["references must be an object."]
    total = 0
    for category, items in references.items():
        if category not in LIMITS:
            errors.append(f"Unknown reference category: {category}")
        if not isinstance(items, list):
            errors.append(f"{category} must be a list of asset identifiers.")
            continue
        total += len(items)
        if any(not isinstance(item, str) or not item.strip() for item in items):
            errors.append(f"{category} entries must be nonblank strings.")
        if category in LIMITS and len(items) > LIMITS[category]:
            errors.append(f"{category} allows at most {LIMITS[category]} assets.")
    if total > 20:
        errors.append("At most 20 total references are allowed.")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("job", type=Path, help="Path to a UTF-8 JSON job")
    args = parser.parse_args()
    try:
        job = json.loads(args.job.read_text(encoding="utf-8-sig"))
    except (OSError, ValueError) as error:
        parser.exit(1, f"{error}\n")
    errors = validate(job)
    if errors:
        parser.exit(1, "\n".join(errors) + "\n")
    print("Valid MAGI-2 job")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
