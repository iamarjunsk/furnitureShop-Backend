from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import app
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from api.models import db,Item,Image

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()