let displayElem = document.querySelector('.counter-display');
let workElem = document.querySelector('.work');
let restElem = document.querySelector('.rest');
let breakElem = document.querySelector('.break');
let counterSkipElem = document.querySelector('.counter-skip');
let counterStartElem = document.querySelector('.counter-start');
let currentButton = document.getElementById('work');

const timer = new Timer(25);


currentButton.style.backgroundColor = "rgb(171, 169, 169)";

function currentlyActive(selected){
    currentButton.style.backgroundColor = "inherit";     // Removes previous highlight
    currentButton = document.getElementById(selected);   // Reassigns active button
    currentButton.style.backgroundColor = "rgb(171, 169, 169)";
}

function timerSetup(minutes, element) {
    if (currentButton != element) {
        timer.newTimer(minutes);
        currentlyActive(element.id);
        timer.updateDisplay();
    }
}
// Event listeners

workElem.addEventListener("click", function() {
    timerSetup(25, workElem);
});

restElem.addEventListener("click", function() {
    timerSetup(5, restElem);
});

breakElem.addEventListener("click", function() {
    timerSetup(15, breakElem);
});

counterStartElem.addEventListener("click", () => {
    if (timer.isPaused) {
        timer.startTimer();
    } else {
        timer.pauseTimer();
    };
});

counterSkipElem.addEventListener("click", ()=> {
    timerSetup(timer.timerSequence(), timer.currentMode(timer.timerSequence()));
})