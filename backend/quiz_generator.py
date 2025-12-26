import os
from google import genai

# Initialize client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_quiz(text):
    prompt = f"""
Generate 3 multiple-choice questions from the following text.
Return ONLY valid JSON (no markdown, no ```).

Format:
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

Text:
{text}
"""

    response = client.models.generate_content(
        model="gemini-1.0-pro",
        contents=prompt
    )

    return response.text
