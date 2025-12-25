function sendImage() {
    // Get selected image
    const fileInput = document.getElementById("image");
    const file = fileInput.files[0];

    if (!file) {
        alert("Please select an image first");
        return;
    }

    // Create form data INSIDE the function
    const formData = new FormData();
    formData.append("image", file);

    fetch("https://ai-quiz-generator-586x.onrender.com/generate-quiz", {
        method: "POST",
        body: formData
    })
        .then(response => {
            if (!response.ok) {
                throw new Error("Server error");
            }
            return response.json();
        })
        .then(data => {
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
        const div = document.createElement("div");
        div.innerHTML = `
            <p><strong>Q${index + 1}:</strong> ${q.question}</p>
            <ul>
                ${q.options.map(opt => `<li>${opt}</li>`).join("")}
            </ul>
        `;
        quizDiv.appendChild(div);
    });
}

