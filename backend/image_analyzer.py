import os
import google.generativeai as genai

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))


def analyze_image(image_file):
    model = genai.GenerativeModel("gemini-pro-vision")

    image_bytes = image_file.read()

    response = model.generate_content([
        "Extract the educational content from this image clearly.",
        {
            "mime_type": image_file.mimetype,
            "data": image_bytes
        }
    ])

    return response.text
