import subprocess
import json

def run_security_scan(file_path):
    result = subprocess.run(
        ["bandit", "-r", file_path, "-f", "json"],
        capture_output=True,
        text=True
    )

    if not result.stdout:
        return {}

    return json.loads(result.stdout)
