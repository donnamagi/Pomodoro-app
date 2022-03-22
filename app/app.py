from flask import Flask, render_template, url_for, flash, redirect
from . import pomodoro, main_pages

def register_blueprints(app: Flask):
    app.register_blueprint(pomodoro.routes.blueprint)
    app.register_blueprint(main_pages.routes.blueprint)

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = 'oop'
  app.config.from_object('app.config')
  register_blueprints(app)

  return app

app = create_app() 
