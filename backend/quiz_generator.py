import google.generativeai as genai
import json

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_quiz(text):
    prompt = f"""
    Create 3 multiple choice questions from the content below.
    Return ONLY valid JSON in this format:

    {{
      "questions": [
        {{
          "question": "...",
          "options": ["A", "B", "C", "D"],
          "answer": "A"
        }}
      ]
    }}

    Content:
    {text}
    """

    response = model.generate_content(prompt)

    try:
        return json.loads(response.text)
    except:
        return {"error": "Failed to generate quiz"}

