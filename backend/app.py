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

        # ✅ PASS FILE OBJECT DIRECTLY
        extracted_text = analyze_image(image_file)

        questions = generate_quiz(extracted_text)

        return jsonify({"questions": questions})

    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({"error": str(e)}), 500
