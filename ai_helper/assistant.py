from ai_helper.explainer import explain_issue


def intro():
    print("\n🤖 Secure Code Review Assistant")
    print("Ask me what an issue means in simple terms.")
    print("Examples: B307 | explain B105 | E225")
    print("Type 'exit' or 'quit' to leave.\n")

    while True:
        try:
            user_input = input("You > ").strip()

            if not user_input:
                continue

            if user_input.lower() in {"exit", "quit"}:
                print("Assistant > Stay secure 👋")
                break

            handle_question(user_input)

        except KeyboardInterrupt:
            print("\nAssistant > Interrupted. Exiting 👋")
            break


def handle_question(user_input: str):
    """
    Extract issue code and explain it.
    Accepts:
    - B307
    - explain B307
    - what is B307
    """

    parts = user_input.upper().split()

    # Grab last token (B307, E225, etc.)
    issue_code = parts[-1]

    explanation = explain_issue(issue_code)

    print(f"\nAssistant > Issue {issue_code}")
    print(f"Why it matters : {explanation['why']}")
    print(f"Risk           : {explanation['risk']}")
    print(f"Suggested fix  : {explanation['fix']}\n")

