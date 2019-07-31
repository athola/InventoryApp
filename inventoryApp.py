import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

inventoryApp = Flask(__name__)
inventoryApp.config.from_object(os.environ['APP_SETTINGS'])
inventoryApp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(inventoryApp)

from models import Grocery

@inventoryApp.route('/')
def hello():
	return "Hello World!"
	
@inventoryApp.route('/<name>')
def hello_name(name):
	return "Hello {}!".format(name)

if __name__ == '__main__':
	inventoryApp.run()