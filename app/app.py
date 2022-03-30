from flask import Flask, render_template, url_for, flash, redirect
from . import pomodoro, main_pages
from log import logger
from app.extensions.database import db, migrate

def page_not_found(e):
  logger.error('Page not found')
  return render_template('404.html', title = 'Page not found'), 404

def register_blueprints(app: Flask):
    app.register_blueprint(pomodoro.routes.blueprint)
    app.register_blueprint(main_pages.routes.blueprint)

def register_extensions(app: Flask):
  db.init_app(app)
  migrate.init_app(app, db)

def create_app():
  app = Flask(__name__)

  #Config 
  app.config.from_object('app.config')

  #Routes
  register_extensions(app)
  register_blueprints(app)
  app.register_error_handler(404, page_not_found)

  return app

app = create_app() 

# Used once to initialize the database:
# db.create_all(app=create_app())