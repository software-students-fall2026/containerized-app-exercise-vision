const playButton = document.getElementById("play-button");
const welcomeScreen = document.getElementById("welcome-screen");
const cameraScreen = document.getElementById("camera-screen");
const webcam = document.getElementById("webcam");
const cameraError = document.getElementById("camera-error");

const countdownOverlay = document.getElementById("countdown-overlay");
const countdownNumber = document.getElementById("countdown-number");
const gameHeading = document.getElementById("game-heading");
const gameInstruction = document.getElementById("game-instruction");

let cameraStream = null;

playButton.addEventListener("click", startCamera);

// webcam permission
async function startCamera() {
    playButton.disabled = true;
    cameraError.textContent = "";

    try {
        cameraStream = await navigator.mediaDevices.getUserMedia({
            video: true,
            audio: false
        });

        webcam.srcObject = cameraStream;

        welcomeScreen.classList.add("hidden");
        cameraScreen.classList.remove("hidden");

        await webcam.play();


        await startCountdown();

    } catch (error) {
        stopCamera();

        cameraScreen.classList.add("hidden");
        welcomeScreen.classList.remove("hidden");

        cameraError.textContent =
            "Unable to start the game. Please check your camera permissions.";

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

// Wait for a specified amount of time
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// Automatic starting countdown
async function startCountdown() {
    gameHeading.textContent = "Get Ready!";
    countdownOverlay.classList.remove("hidden");

    for (let count = 3; count > 0; count--) {
        countdownNumber.textContent = count;

        countdownNumber.classList.remove("countdown-pop");
        void countdownNumber.offsetWidth;
        countdownNumber.classList.add("countdown-pop");

        await sleep(1000);
    }

    countdownNumber.textContent = "GO!";

    await sleep(700);

    countdownOverlay.classList.add("hidden");

    startGame();
}

// placeholder for now, need game logic 
function startGame() {
    gameHeading.textContent = "Simon Says!";
    gameInstruction.textContent = "Let the game begin!";
}

window.addEventListener("pagehide", stopCamera);