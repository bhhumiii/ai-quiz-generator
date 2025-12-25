import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def generate_quiz(text):
    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = f"""
    Create 5 multiple choice questions from this text.
    Each question should have 4 options and one correct answer.
    Return response as JSON like:
    {{
      "questions": [
        {{
          "question": "",
          "options": [],
          "answer": ""
        }}
      ]
    }}
    Text:
    {text}
    """

    response = model.generate_content(prompt)
    return response.text
