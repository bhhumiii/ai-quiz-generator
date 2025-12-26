import os
from google import genai
from PIL import Image


def analyze_image(image_file):
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    image = Image.open(image_file)

    response = client.models.generate_content(
        model="gemini-1.5-pro",
        contents=[
            "Extract all readable text from this image.",
            image
        ]
    )

    return response.text
