from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import base64

from image_analyzer import analyze_image
from quiz_generator import generate_quiz

app = Flask(__name__)

# ✅ VERY IMPORTANT (fixes Netlify → Render issue)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/", methods=["GET"])
def home():
    return "AI Quiz Generator API is running"


@app.route("/generate-quiz", methods=["POST"])
def generate_quiz_api():
    try:
        if "image" not in request.files:
            return jsonify({"error": "No image uploaded"}), 400

        image_file = request.files["image"]
        image_bytes = image_file.read()

        if not image_bytes:
            return jsonify({"error": "Empty image file"}), 400

        # Convert image to base64
        image_base64 = base64.b64encode(image_bytes).decode("utf-8")

        # Step 1: analyze image
        image_text = analyze_image(image_base64)

        # Step 2: generate quiz
        quiz = generate_quiz(image_text)

        return jsonify({"quiz": quiz})

    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
