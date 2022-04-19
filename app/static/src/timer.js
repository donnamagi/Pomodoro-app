class Timer {
    constructor(minutes, display) {
        this.remainingTime = this.minToMs(minutes);
        this.isPaused = true;
        this.continue = true;
        this.display = display;
        this.pomodoro = 3;
        this.session = 25;
        this.updateDisplay();
        this.interval = setInterval(this.runTimer.bind(this), 1);
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
        };
        if (this.remainingTime == 0) {
            clearInterval(this.interval);
            this.newInterval();
        }
    }
    
    newInterval() {
        var next = this.timerSequence();
        this.newTimer(next);
        this.interval = setInterval(this.runTimer.bind(this), 1);
        this.updateDisplay();
    }

    newTimer(minutes) {
        this.session = minutes;
        if (!this.isPaused) {
            this.pauseTimer();
        };
        this.remainingTime = this.minToMs(minutes);
    }

    timerSequence() {
        switch (this.session) {
            case 25:
                this.pomodoro--;
                if (this.pomodoro = 0) {
                    this.pomodoro = 3;
                    return 15;                    
                }
                return 5;
            case 5:
                return 25;
            case 15:
                return 25;
        };
    }

    minToMs(minutes) {
        return minutes * 60 * 1000;
    }
    
    msCalculator(ms) {
        const date = new Date(ms);
        return `${('00'+date.getMinutes()).slice(-2)}:${('00'+date.getSeconds()).slice(-2)}`
    }
}

