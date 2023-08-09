// JavaScript to display selected file name
       
document.addEventListener("DOMContentLoaded", function () {
    var fileInput = document.getElementById("cv-upload-input");
    var selectedFileName = document.getElementById("selected-file-name");

    fileInput.addEventListener("change", function () {
        selectedFileName.textContent = fileInput.files[0].name;
        selectedFileName.style.display = "inline-block";
    });
});









document.addEventListener("DOMContentLoaded", function () {
    const modal = document.getElementById("myModal");
    const submitButton = document.getElementById("submitButton");
    const closeModal = document.getElementById("closeModal");
    const goBackButton = document.getElementById("goBackButton");

    submitButton.addEventListener("click", function (event) {
        event.preventDefault(); // Prevent form submission
        modal.style.display = "block";
    });

    closeModal.addEventListener("click", function () {
        modal.style.display = "none";
    });

    goBackButton.addEventListener("click", function () {
        modal.style.display = "none";
    });
});


//timer
// Get the necessary elements
const countdownElement = document.getElementById("countdown");
const submitButton = document.getElementById("submitButton");
const questionnaireForm = document.getElementById("questionnaireForm");

let timeRemaining = 1800; // 30 minutes in seconds

function updateCountdown() {
    const minutes = Math.floor(timeRemaining / 60);
    const seconds = timeRemaining % 60;
    countdownElement.textContent = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
}

function submitForm() {
    questionnaireForm.submit();
}

const countdownInterval = setInterval(function () {
    if (timeRemaining > 0) {
        timeRemaining--;
        updateCountdown();
    } else {
        clearInterval(countdownInterval);
        updateCountdown();
        submitForm();
    }
}, 1000);
