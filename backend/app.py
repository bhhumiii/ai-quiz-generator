from flask import Flask, request, jsonify
from image_analyzer import analyze_image
from quiz_generator import generate_quiz
import os


app = Flask(__name__)


@app.route("/generate-quiz", methods=["POST"])
def generate():
    image = request.files["image"]
    text = analyze_image(image)
    quiz = generate_quiz(text)
    return jsonify({"quiz": quiz})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
