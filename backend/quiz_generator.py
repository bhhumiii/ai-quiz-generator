import os
from google import genai

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))


def generate_quiz(text):
    prompt = f"""
    Create 3 multiple-choice questions from the text below.
    Each question must have 4 options and one correct answer.
    Return JSON only.

    Text:
    {text}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
