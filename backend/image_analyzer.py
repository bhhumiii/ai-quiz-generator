import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def analyze_image(image_file):
    image_bytes = image_file.read()

    response = client.models.generate_content(
        model="gemini-1.0-pro",
        contents=[
            "Extract readable text from this image.",
            {
                "mime_type": "image/png",
                "data": image_bytes
            }
        ]
    )

    return response.text
