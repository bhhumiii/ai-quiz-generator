import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def analyze_image(image_file):
    model = genai.GenerativeModel("gemini-1.5-flash")

    image_bytes = image_file.read()

    response = model.generate_content([
        "Read the image and extract important text for quiz questions",
        image_bytes
    ])

    return response.text
