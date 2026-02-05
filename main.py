from scanner.security_scan import run_security_scan
from pathlib import Path

from pathlib import Path

from scanner.security_scan import run_security_scan
from scanner.style_scan import run_style_scan
from ai_helper.explainer import explain_issue


BASE_DIR = Path(__file__).resolve().parent
TARGET_FILE = BASE_DIR / "samples" / "vulnerable.py"


if __name__ == "__main__":
    print("=== Secure Code Review Report ===")

    # --------------------
    # Security Scan
    # --------------------
    security_report = run_security_scan(str(TARGET_FILE))
    security_issues = security_report.get("results", [])

    print("\n--- Security Issues ---")

    if not security_issues:
        print("No security issues found.")
    else:
        for idx, issue in enumerate(security_issues, start=1):
            explanation = explain_issue(issue["test_id"], issue)

            print(f"\n[{idx}] {issue['test_id']} - {issue['test_name']}")
            print(f"Severity   : {issue['issue_severity']}")
            print(f"Confidence : {issue['issue_confidence']}")
            print(f"Line       : {issue['line_number']}")
            print(f"Code       : {issue['code'].strip()}")

            print("Why it matters :", explanation["why"])
            print("Risk           :", explanation["risk"])
            print("Suggested fix  :", explanation["fix"])

    # --------------------
    # PEP8 / Style Scan
    # --------------------
    style_issues = run_style_scan(str(TARGET_FILE))

    print("\n--- PEP8 / Style Issues ---")

    if not style_issues:
        print("No PEP8 issues found.")
    else:
        for idx, issue in enumerate(style_issues, start=1):
            issue_code = issue["message"].split()[0]
            explanation = explain_issue(issue_code)

            print(f"\n[{idx}] Line {issue['line']}, Col {issue['column']}")
            print(f"Message : {issue['message']}")

            print("Why it matters :", explanation["why"])
            print("Risk           :", explanation["risk"])
            print("Suggested fix  :", explanation["fix"])

