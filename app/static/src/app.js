const timer = new Timer(25);

// timer.startTimer();

// let counterWorkElem = document.querySelector('.work');
// let counterRestElem = document.querySelector('.rest');
// let counterBreakElem = document.querySelector('.break');
// let counterDisplayElem = document.querySelector('.counter-display');
// let counterSkipElem = document.querySelector('.counter-skip');
// let counterStartElem = document.querySelector('.counter-start');

// // Default variables for when the todos page loads
// let counterMinute = 25;
// let counterSecond = 0;
// let isPaused = true;
// let currentButton = document.getElementById('work');
// currentButton.style.backgroundColor = "rgb(171, 169, 169)";

// function currentlyActive(selected){
//     currentButton.style.backgroundColor = "inherit";     // Removes previous highlight
//     currentButton = document.getElementById(selected);   // Reassigns active button
//     currentButton.style.backgroundColor = "rgb(171, 169, 169)";
// }

// const fillZero=(n)=> ('00'+n).slice(-2);
// updateDisplay();

// function updateDisplay(){
//     counterDisplayElem.innerHTML = fillZero(counterMinute) + ':' + fillZero(counterSecond);
// };

// // Event listeners

// counterSkipElem.addEventListener("click",()=>{
//     var orderOfButtons = ['work', 'rest', 'break', 'work'];
//     var index = orderOfButtons.indexOf(currentButton.id);
//     var redirect = orderOfButtons[index + 1];


//     clearInterval(PomodoroCounter);
//     updateDisplay();
// });

// counterWorkElem.addEventListener("click", ()=>{
//     counterMinute = 25;
//     counterSecond = 0;
//     updateDisplay();
//     currentlyActive(counterWorkElem.id);
// });

// counterRestElem.addEventListener("click", ()=>{
//     counterMinute = 5;
//     counterSecond = 0;
//     updateDisplay();
//     currentlyActive(counterRestElem.id);
// });

// counterBreakElem.addEventListener("click", ()=>{
//     counterMinute = 15;
//     counterSecond = 0;
//     updateDisplay();
//     currentlyActive(counterBreakElem.id);
// });

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
