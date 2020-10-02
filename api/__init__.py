from flask import Flask,Blueprint
api = Blueprint('api',__name__)

from api import views


