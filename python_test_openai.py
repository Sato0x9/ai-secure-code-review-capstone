from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-4.1-mini",
    input="Explain what a Python function is in simple terms."
)

print(response.output_text)
