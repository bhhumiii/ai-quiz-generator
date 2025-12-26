import os
from google import genai
from google.genai.types import Part


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def analyze_image(image_file):
    # Read image bytes
    image_bytes = image_file.read()

    model = client.models.get("gemini-1.0-pro-vision")

    response = model.generate_content(
        contents=[
            "Extract readable text from this image.",
            Part.from_bytes(
                data=image_bytes,
                mime_type=image_file.mimetype
            )
        ]
    )

    return response.text
