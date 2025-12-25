from flask import Flask, request, jsonify
from flask_cors import CORS
import os

from image_analyzer import analyze_image
from quiz_generator import generate_quiz

app = Flask(__name__)

# ✅ Allow Netlify frontend to call Render backend
CORS(app, resources={
    r"/*": {
        "origins": [
            "https://soft-babka-85acad.netlify.app"
        ]
    }
})


@app.route("/", methods=["GET"])
def home():
    return "AI Quiz Generator backend is running!"


@app.route("/generate-quiz", methods=["POST"])
def generate_quiz_api():
    try:
        # ✅ Check image
        if "image" not in request.files:
            return jsonify({"error": "No image uploaded"}), 400

        image = request.files["image"]

        if image.filename == "":
            return jsonify({"error": "Empty image"}), 400

        # ✅ Step 1: OCR / Image understanding
        extracted_text = analyze_image(image)

        if not extracted_text:
            return jsonify({"error": "Could not read text from image"}), 400

        # ✅ Step 2: Generate quiz from text
        questions = generate_quiz(extracted_text)

        return jsonify({
            "questions": questions
        })

    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({"error": "Internal server error"}), 500


# ✅ Required for Render
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
