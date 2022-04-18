let displayElem = document.querySelector('.counter-display');
let workElem = document.querySelector('.work');
let restElem = document.querySelector('.rest');
let breakElem = document.querySelector('.break');
let counterSkipElem = document.querySelector('.counter-skip');
let counterStartElem = document.querySelector('.counter-start');
let currentButton = document.getElementById('work');

const timer = new Timer(25, displayElem);


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
    }
}
// Event listeners

// counterSkipElem.addEventListener("click",()=>{
//     var orderOfButtons = ['work', 'rest', 'break', 'work'];
//     var index = orderOfButtons.indexOf(currentButton.id);
//     var redirect = orderOfButtons[index + 1];


//     clearInterval(PomodoroCounter);
//     updateDisplay();
// });

workElem.addEventListener("click", function() {
    timerSetup(25, workElem);
});

restElem.addEventListener("click", function() {
    timerSetup(5, restElem);
});

breakElem.addEventListener("click", function() {
    timerSetup(15, breakElem);
});

// counterStartElem.addEventListener("click", () => {
//     if (isPaused) {
//         isPaused = false;
//         counterStartElem.innerHTML = 'Pause';
//     } else {
//         isPaused = true;
//         counterStartElem.innerHTML = 'Start';
//     }
//     updateDisplay();
// })

// PomodoroCounter = setInterval(timer, 1000);

// function timer() {
//     if (!isPaused) {
//         if (counterSecond == 0) {
//             counterMinute--;
//             counterSecond = 60;
//             updateDisplay();
//         } 
//         if (counterMinute <= 1) {
//             clearInterval(PomodoroCounter);
//         }
    
//         counterSecond--;
//         updateDisplay();
//     }
//     }
