class Timer {
    constructor(minutes) {
        this.remainingTime = minutes * 60 * 1000;
        this.interval;
        this.isPaused = false;
        this.continue = true;
    };

    setTime(minutes) {
        this.remainingTime = minutes * 60 * 1000;
    }

    msCalculator(ms) {
        const date = new Date(ms);
        return `${('00'+date.getMinutes()).slice(-2)}:${('00'+date.getSeconds()).slice(-2)}`
    }
}

