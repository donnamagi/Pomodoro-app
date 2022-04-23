class Timer {
    constructor(minutes) {
        this.remainingTime = this.minToMs(minutes);
        this.isPaused = true;
        this.pomodoro = 3;
        this.session = minutes;
        this.updateDisplay();
        this.interval = setInterval(this.runTimer.bind(this), 1);
    };

    startTimer() {
        this.isPaused = false;
        counterStartElem.innerHTML = 'Pause';
        counterSkipElem.style.display = 'inline-block';
    }
    
    pauseTimer() {
        this.isPaused = true; 
        counterStartElem.innerHTML = 'Start';
        counterSkipElem.style.display = 'none';
    } 

    updateDisplay() {
        var time = this.msCalculator(this.remainingTime);
        displayElem.innerHTML = time;

        if (this.currentMode[this.session] != currentButton) {
            timerSetup(this.session, this.currentMode(this.session));
        };
    }
    
    runTimer() {
        if (!this.isPaused) {
            this.remainingTime = this.remainingTime - 1000;
            this.updateDisplay();
        };
        if (this.remainingTime == 0) {
            clearInterval(this.interval);

            // Notifying the user of state changes
            notification(this.currentMode(this.session));

            this.newInterval();
        }
    }

    // Runs when cycles naturally complete
    newInterval() {
        this.newTimer(this.timerSequence());
        this.interval = setInterval(this.runTimer.bind(this), 1000);
        this.updateDisplay();
    }

    // Runs on its own when user manually chooses mode
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
                if (this.pomodoro == 0) {
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

    currentMode(sequence) {
        switch (sequence) {
            case 25:
                return workElem;
            case 5:
                return restElem;
            case 15:
                return breakElem;
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

