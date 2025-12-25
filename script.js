function sendImage() {
    const file = document.getElementById("image").files[0];
    const formData = new FormData();
    formData.append("image", file);

    const API_URL = "https://ai-quiz-generator-586x.onrender.com/generate-quiz";
, {
        method: "POST",
            body: formData
    })
        .then(res => res.json())
        .then(data => {
            document.getElementById("quiz").innerText = data.quiz;
        })
        .catch(err => {
            alert("Error generating quiz");
            console.error(err);
        });
}
