const playButton = document.getElementById("play-button");
const welcomeScreen = document.getElementById("welcome-screen");
const cameraScreen = document.getElementById("camera-screen");
const webcam = document.getElementById("webcam");
const cameraError = document.getElementById("camera-error");

let cameraStream = null;

playButton.addEventListener("click", startCamera);

async function startCamera() {
    playButton.disabled = true;
    cameraError.textContent = "";

    try {
        // Request webcam permission
        cameraStream = await navigator.mediaDevices.getUserMedia({
            video: true,
            audio: false
        });

        // Connect the webcam to the video element
        webcam.srcObject = cameraStream;

        // Transition to the camera screen
        welcomeScreen.classList.add("hidden");
        cameraScreen.classList.remove("hidden");

        await webcam.play();

    } catch (error) {
        stopCamera();

        cameraScreen.classList.add("hidden");
        welcomeScreen.classList.remove("hidden");

        cameraError.textContent =
            "Unable to access your camera. Please check your permissions.";

        console.error(error);

    } finally {
        playButton.disabled = false;
    }
}

function stopCamera() {
    if (cameraStream) {
        cameraStream.getTracks().forEach(track => track.stop());
        cameraStream = null;
        webcam.srcObject = null;
    }
}

window.addEventListener("pagehide", stopCamera);