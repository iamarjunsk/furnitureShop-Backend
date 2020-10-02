from flask import Flask
from api import api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
ma = Marshmallow(app)

app.register_blueprint(api)


mode = 'dev'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= True

db = SQLAlchemy(app)


if mode == 'dev':
    app.debug = True
else:
    app.debug = False



if __name__ == "__main__":
    app.run()