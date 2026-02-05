def explain_issue(issue_id, metadata=None):
    explanations = {
        "B105": {
            "why": "Hardcoded passwords can be extracted from source code and reused by attackers.",
            "risk": "If the code is leaked, credentials are immediately compromised.",
            "fix": "Use environment variables or secure credential storage."
        },
        "B307": {
            "why": "eval() executes arbitrary code passed as input.",
            "risk": "This can lead to remote code execution (RCE).",
            "fix": "Use ast.literal_eval() or explicit parsing logic."
        },
        "E225": {
            "why": "Missing whitespace reduces readability.",
            "risk": "Poor readability increases maintenance errors.",
            "fix": "Follow PEP8 spacing rules."
        },
        "E302": {
            "why": "Functions should be separated by blank lines.",
            "risk": "Tightly packed code is harder to maintain.",
            "fix": "Add two blank lines before function definitions."
        }
    }

    return explanations.get(issue_id, {
        "why": "This issue affects code quality or security.",
        "risk": "May lead to bugs or vulnerabilities.",
        "fix": "Follow recommended best practices."
    })
