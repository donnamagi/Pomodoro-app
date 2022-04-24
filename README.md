# Pomodoro app

I coded a simple Pomodoro-style productivity tool. This has the basic functionality of a Pomodoro timer, as well as a personal todo list. Users can save and delete (complete) their tasks from the database, with the added benefit of coming back to finish them the next time they log in to their Pomodoro app.

A crucial functionality I implemented are the push notifications in the OS, so that the user will get notified about breaks without having to constantly look at the timer. The app will run according to the renowned Pomodoro scheme:

1. Working sequence starts (25 minutes).
2. App encourages user to end work and take a short break (5 minutes).
3. This will have completed one pomodoro. With fewer than three pomodoros, app loops back to Step 1.
4. After the fourth pomodoro the app sets a long break (25 minutes). Once the long break is finished, return to step 1.

But the user is still free to stop, skip or choose the mode they currently wish.

[More info on the Pomodoro technique](https://todoist.com/productivity-methods/pomodoro-technique)

## Technical setup 

This project is additionally [deployed through Heroku](https://murmuring-citadel-73709.herokuapp.com) and uses the python framework Flask with a Postgres database. However, when run locally, the database will be SQLite.

### Website architecture

![Click me to see the architecture](https://github.com/donnamagi/Pomodoro-app/blob/main/diagram.pdf "Diagram")

### To set up a local development environment: 

1. Download the repository from Github
2. Set up a new virtual environment 
3. Install packages:      __pip install -r requirements.txt__

> This will install all packages required to run the application. You will still need to set some config variables.

4. Locate the folder .envexample and follow the instructions there
5. Initialize the database:      __flask db init__

> You should now be all set to run the application locally. To launch the app, run __flask run__ in the terminal.

### Have fun!



