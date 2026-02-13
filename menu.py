from pathlib import Path
import subprocess
import sys

from ai_helper.explainer import explain_issue
from ai_helper.assistant import intro


BASE_DIR = Path(__file__).resolve().parent


def print_menu():
    print("\n🔐 Secure Code Review Tool")
    print("1. Scan a Python file")
    print("2. Explain an issue code (B105, B307, E225)")
    print("3. Exit")


def scan_file():
    file_path = input("Enter path to Python file: ").strip()

    if not file_path:
        print("No file provided.")
        return

    target = Path(file_path)

    if not target.exists():
        print("File does not exist.")
        return

    print("\nRunning security scan...\n")

    # Call main.py exactly how a user would
    subprocess.run(
        [sys.executable, "main.py", "--file", str(target)],
        cwd=BASE_DIR
    )


def explain_issue_menu():
    print("\nEnter an issue code (e.g. B105, B307, E225)")
    code = input("Issue code: ").strip().upper()

    if not code:
        print("No issue code provided.")
        return

    explanation = explain_issue(code)

    print(f"\n🧠 Issue {code}")
    print(f"Why it matters : {explanation['why']}")
    print(f"Risk           : {explanation['risk']}")
    print(f"Suggested fix  : {explanation['fix']}")


def main():
    while True:
        print_menu()
        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            scan_file()
        elif choice == "2":
            explain_issue_menu()
        elif choice == "3":
            print("Stay secure 👋")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
