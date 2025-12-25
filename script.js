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
    console.log(data);
    // show quiz here
})
.catch(error => {
    alert("Error generating quiz");
    console.error(error);
});


