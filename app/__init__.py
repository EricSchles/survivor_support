from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import views, models
from .commands import REPL, ScrapeCrisisTextLine

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command("shell", REPL())
manager.add_command("scrape_ctl", ScrapeCrisisTextLine())
