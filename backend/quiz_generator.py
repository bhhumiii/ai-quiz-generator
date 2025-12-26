import os
import google.generativeai as genai

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))


def generate_quiz(text):
    model = genai.GenerativeModel("gemini-pro")

    prompt = f"""
    Based on the following text, create 5 multiple-choice questions.
    Each question should have 4 options and one correct answer.

    Text:
    {text}

    Format the output as JSON with this structure:
    [
      {{
        "question": "...",
        "options": ["A", "B", "C", "D"],
        "answer": "A"
      }}
    ]
    """

    response = model.generate_content(prompt)

    return eval(response.text)
