import os
from google import genai


def generate_quiz(text):
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    prompt = f"""
    Generate 3 multiple-choice quiz questions from the text below.
    Return ONLY valid JSON. No markdown. No explanation.

    Text:
    {text}

    JSON format:
    [
      {{
        "question": "...",
        "options": {{
          "A": "...",
          "B": "...",
          "C": "...",
          "D": "..."
        }},
        "correct_answer": "A"
      }}
    ]
    """

    response = client.models.generate_content(
        model="gemini-1.5-pro",
        contents=prompt
    )

    return response.text
