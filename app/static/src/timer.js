class Timer {
    constructor(minutes) {
        this.remainingTime = minutes * 60 * 1000;
        this.interval;
        this.isPaused = false;
        this.continue = true;
        setInterval(this.runTimer.bind(this), 1000)
    };

    setTime(minutes) {
        this.remainingTime = minutes * 60 * 1000;
    }
    
    startTimer() {
        this.isPaused = false;
    }

    pauseTimer() {
        this.isPaused = true; 
     } 

    runTimer() {
        if (!this.isPaused) {
            this.remainingTime = this.remainingTime - 1000;
            var time = this.msCalculator(this.remainingTime);
            console.log(time);
            // updateDisplay();
        }
    }

    msCalculator(ms) {
        const date = new Date(ms);
        return `${('00'+date.getMinutes()).slice(-2)}:${('00'+date.getSeconds()).slice(-2)}`
    }
}

