let counterWorkElem = document.querySelector('.work');
let counterRestElem = document.querySelector('.rest');
let counterBreakElem = document.querySelector('.break');
let counterDisplayElem = document.querySelector('.counter-display');
let counterSkipElem = document.querySelector('.counter-skip');
let counterStartElem = document.querySelector('.counter-start');

let counterMinute = 25;
let counterSecond = 0;
let isPaused = true;

const fillZero=(n)=> ('00'+n).slice(-2);
updateDisplay();

function updateDisplay(){
    counterDisplayElem.innerHTML = fillZero(counterMinute) + ':' + fillZero(counterSecond);
};

// Event listeners

counterSkipElem.addEventListener("click",()=>{
    clearInterval(PomodoroCounter);
    updateDisplay();
});

counterRestElem.addEventListener("click", ()=>{
    counterMinute = 5;
    counterSecond = 0;
    updateDisplay();
});

counterBreakElem.addEventListener("click", ()=>{
    counterMinute = 15;
    counterSecond = 0;
    updateDisplay();
});

counterStartElem.addEventListener("click", () => {
    if (isPaused) {
        isPaused = false;
        counterStartElem.innerHTML = 'Pause';
    } else {
        isPaused = true;
        counterStartElem.innerHTML = 'Start';
    }
    updateDisplay();
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
