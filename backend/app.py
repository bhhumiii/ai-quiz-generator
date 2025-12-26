from flask import Flask, request, jsonify
from flask_cors import CORS
import json

from image_analyzer import analyze_image
from quiz_generator import generate_quiz


app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def home():
    return "AI Quiz Generator API running"


@app.route("/generate-quiz", methods=["POST"])
def generate_quiz_api():
    try:
        if "image" not in request.files:
            return jsonify({"error": "No image uploaded"}), 400

        image_file = request.files["image"]

        extracted_text = analyze_image(image_file)

        raw_output = generate_quiz(extracted_text)

        # 🔥 FORCE CLEAN
        cleaned = raw_output.strip()

        if cleaned.startswith("```"):
            cleaned = cleaned.replace("```json", "")
            cleaned = cleaned.replace("```", "")
            cleaned = cleaned.strip()

        questions = json.loads(cleaned)

        return jsonify({
            "questions": questions
        })

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
