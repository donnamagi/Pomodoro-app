from dotenv import load_dotenv
from os import environ

load_dotenv()

SECRET_KEY = b'_5#y2L"F4Q8zlkj2w23&0FGHnx0/ec]/'
SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = False