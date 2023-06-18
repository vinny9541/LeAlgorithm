var isRecording = false;

function toggleRecording() {
    var recordingText = document.getElementById("recordingText");
    var speechButton = document.getElementById("speechButton");
    var speechText = document.getElementById("speechText");
    var speechImage = document.getElementById("speechImage");

    if (isRecording) {
        recordingText.style.display = "none";
        recordingText.classList.remove("blink-animation");
        speechText.textContent = "Speech to Speech translation";
        speechImage.style.filter = "";  // remove the filter
    } else {
        recordingText.style.display = "block";
        recordingText.classList.add("blink-animation");
        speechText.textContent = "Stop Recording";
        speechImage.style.filter = "invert(35%) sepia(100%) saturate(3432%) hue-rotate(360deg) brightness(100%) contrast(104%)";  // add a filter to make the image look red
    }

    isRecording = !isRecording;
}

function togglePlay() {
    alert("test");
}