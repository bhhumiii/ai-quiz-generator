import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_quiz(text):
    prompt = f"""
    Create 3 multiple-choice questions from the following text.
    Respond ONLY in valid JSON.

    Text:
    {text}
    """

    response = client.models.generate_content(
        model="gemini-1.0-pro",
        contents=prompt
    )

    return response.text
