import subprocess

def run_style_scan(file_path):
    result = subprocess.run(
        ["flake8", file_path],
        capture_output=True,
        text=True
    )

    if not result.stdout:
        return []

    issues = []
    for line in result.stdout.strip().splitlines():
        parts = line.split(":", 3)
        if len(parts) == 4:
            filename, line_no, col_no, message = parts
            issues.append({
                "file": filename.strip(),
                "line": line_no.strip(),
                "column": col_no.strip(),
                "message": message.strip()
            })

    return issues
