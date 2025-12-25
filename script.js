function sendImage() {
    const fileInput = document.getElementById("image");
    const file = fileInput.files[0];

    if (!file) {
        alert("Please select an image first");
        return;
    }

    const formData = new FormData();
    formData.append("image", file);

    fetch("https://ai-quiz-generator-586x.onrender.com/generate-quiz", {
        method: "POST",
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
                return;
            }

            displayQuiz(data.questions);
        })
        .catch(error => {
            console.error(error);
            alert("Error generating quiz");
        });
}


function displayQuiz(questions) {
    const quizDiv = document.getElementById("quiz");
    quizDiv.innerHTML = "";

    questions.forEach((q, index) => {
        const questionBlock = document.createElement("div");

        questionBlock.innerHTML = `
            <p><strong>Q${index + 1}. ${q.question}</strong></p>
            ${q.options.map(opt => `<p>• ${opt}</p>`).join("")}
            <p><em>Answer: ${q.answer}</em></p>
            <hr>
        `;

        quizDiv.appendChild(questionBlock);
    });
}
