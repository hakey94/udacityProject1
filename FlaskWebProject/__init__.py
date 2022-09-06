"""
The flask application package.
"""
from email import header
import logging
import sys
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)
# TODO: Add any logging levels and handlers with app.logger

streamHandler = logging.StreamHandler(stream=sys.stdout)
streamHandler.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))
app.logger.addHandler(streamHandler)
app.logger.setLevel(logging.INFO)
app.logger.info('App startup')
app.logger.info(header)

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views
