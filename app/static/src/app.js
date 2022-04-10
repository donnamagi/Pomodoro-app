let counterDisplayElem = document.querySelector('.counter-display');
let counterPauseElem = document.querySelector('.counter-pause');
let counterSkipElem = document.querySelector('.counter-skip');
let counterStartElem = document.querySelector('.counter-start');

let counterMinute = 9;
let counterSecond = 11;
let isPaused = true;

const fillZero=(n)=> ('00'+n).slice(-2);
updateDisplay();

function updateDisplay(){
    counterDisplayElem.innerHTML = fillZero(counterMinute) + ':' + fillZero(counterSecond);
};

counterPauseElem.addEventListener("click",()=>{
    isPaused = true;
    updateDisplay();
});

counterSkipElem.addEventListener("click",()=>{
    clearInterval(PomodoroCounter);
    updateDisplay();
});

counterStartElem.addEventListener("click", () => {
    isPaused = false;
})

PomodoroCounter = setInterval(timer, 1000);

function timer() {
    if (!isPaused) {
        if (counterSecond == 0) {
            counterMinute--;
            counterSecond = 60;
            updateDisplay();
        } 
        if (counterMinute <= 1) {
            clearInterval(PomodoroCounter);
        }
    
        counterSecond--;
        updateDisplay();
    }
    }
