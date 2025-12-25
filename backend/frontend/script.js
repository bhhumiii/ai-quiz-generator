let correctAnswers = [];

function sendImage() {
    let file = document.getElementById("image").files[0];
    let formData = new FormData();
    formData.append("image", file);

    fetch("https://ai-quiz-generator-586x.onrender.com/generate-quiz", {
 {
            method: "POST",
            body: formData
        })
        .then(res => res.json())
        .then(data => {
            displayQuiz(data.quiz);

        });
}

function displayQuiz(questions) {
    let quizDiv = document.getElementById("quiz");
    quizDiv.innerHTML = "";
    correctAnswers = [];

    questions.forEach((q, index) => {
        correctAnswers.push(q.answer);

        let html = `<p>${index + 1}. ${q.question}</p>`;
        q.options.forEach(opt => {
            html += `
            <input type="radio" name="q${index}" value="${opt}">
            ${opt}<br>
            `;
        });
        quizDiv.innerHTML += html;
    });
}

function submitQuiz() {
    let score = 0;

    correctAnswers.forEach((ans, i) => {
        let selected = document.querySelector(`input[name="q${i}"]:checked`);
        if (selected && selected.value === ans) {
            score++;
        }
    });

    document.getElementById("score").innerText =
        `Score: ${score} / ${correctAnswers.length}`;
}
