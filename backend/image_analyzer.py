import google.generativeai as genai
from PIL import Image

genai.configure(api_key="AIzaSyCICDMGX9dRPKUTzIu09R8N1UIX7MNq838")

model = genai.GenerativeModel("gemini-2.5-flash")

def analyze_image(image_file):
    image = Image.open(image_file)
    response = model.generate_content(
        ["Explain the educational content in this image", image]
    )
    return response.text

