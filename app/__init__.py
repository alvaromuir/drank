from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
db  = SQLAlchemy(app)
lm  = LoginManager()

app.config.from_object('config')
lm.init_app(app)
lm.login_view = 'login'

from app import routes, db
from app.views import helpers

app.jinja_env.filters['datetime']   = helpers.datetime
app.jinja_env.filters['human_time'] = helpers.human_time