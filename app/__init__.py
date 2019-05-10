from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from .commands import REPL
import os
from flask_bootstrap import Bootstrap
from .nav import nav

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["BOOTSTRAP_SERVE_LOCAL"] = True
#app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://eric_s:1234@localhost/testing"
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
migrate = Migrate(app,db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command("shell", REPL())
nav.init_app(app)

from app import views, models
