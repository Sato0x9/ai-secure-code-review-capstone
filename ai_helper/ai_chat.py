import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are a secure coding assistant.
Explain security and PEP8 issues in simple, beginner-friendly language.
Be concise, practical, and calm.
Avoid jargon unless necessary.
"""

def ask_ai(user_question: str) -> str:
    if not user_question.strip():
        return "Please ask a question."

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_question}
            ],
            temperature=0.3,
            max_tokens=200
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"AI error: {str(e)}"
