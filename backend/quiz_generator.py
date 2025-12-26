import os
from google import genai


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_quiz(text):
    model = client.models.get("gemini-1.0-pro")

    prompt = f"""
    Create 3 multiple-choice questions from the following text.
    Respond ONLY in valid JSON.

    Text:
    {text}
    """

    response = model.generate_content(prompt)
    return response.text
