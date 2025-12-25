function sendImage() {
    const imageInput = document.getElementById("image");
    const quizDiv = document.getElementById("quiz");

    if (imageInput.files.length === 0) {
        alert("Please select an image first");
        return;
    }

    quizDiv.innerHTML = "⏳ Generating quiz...";

    const formData = new FormData();
    formData.append("image", imageInput.files[0]);

    fetch("https://ai-quiz-generator-586x.onrender.com/generate-quiz", {
        method: "POST",
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            displayQuiz(data.quiz);
        })
        .catch(error => {
            quizDiv.innerHTML = "❌ Error generating quiz";
            console.error(error);
        });
}

function displayQuiz(quizText) {
    const quizDiv = document.getElementById("quiz");
    quizDiv.innerHTML = "";

    const lines = quizText.split("\n");

    lines.forEach(line => {
        if (line.trim() !== "") {
            const p = document.createElement("p");
            p.textContent = line;
            quizDiv.appendChild(p);
        }
    });
}
