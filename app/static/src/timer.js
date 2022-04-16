class Timer {
    constructor(minutes, display) {
        this.remainingTime = this.minToMs(minutes);
        this.isPaused = false;
        this.continue = true;
        this.display = display;
        this.updateDisplay();
        setInterval(this.runTimer.bind(this), 1000);
    };

    startTimer() {
        this.isPaused = false;
    }
    
    pauseTimer() {
        this.isPaused = true; 
    } 

    updateDisplay() {
        var time = this.msCalculator(this.remainingTime);
        this.display.innerHTML = time;
    }
    
    runTimer() {
        if (!this.isPaused) {
            this.remainingTime = this.remainingTime - 1000;
            this.updateDisplay();
        }  
    }

    minToMs(minutes) {
        return minutes * 60 * 1000;
    }
    
    msCalculator(ms) {
        const date = new Date(ms);
        return `${('00'+date.getMinutes()).slice(-2)}:${('00'+date.getSeconds()).slice(-2)}`
    }
}

