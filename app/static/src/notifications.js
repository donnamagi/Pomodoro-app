function notificationSetup() {
    // Checking if the browser supports notifications
    if (!("Notification" in window)) {
      alert("This browser does not support desktop notification");
    }
  
    // Checking whether notification permissions have already been granted
    else if (Notification.permission === "granted") {
      var notification = new Notification("Let's get to work!");
    }
  
    // Asking the user to set preferences
    else if (Notification.permission !== "denied") {

      Notification.requestPermission()
      
      if (Notification.permission === "granted") {
        var notification = new Notification("Let's get to work!");
        }
      }
}

function notification(mode) {

    if (Notification.permission === "granted") {
        switch (mode) {
            case workElem:
                return new Notification('Time for a break!');
            case restElem:
                return new Notification("Back to work!");
            case breakElem:
                return new Notification("Back to work!");
        }
    }
}

