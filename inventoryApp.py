import os
from flask import Flask
inventoryApp = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

@inventoryApp.route('/')
def hello():
	return "Hello World!"
	
@inventoryApp.route('/<name>')
def hello_name(name):
	return "Hello {}!".format(name)

if __name__ == '__main__':
	inventoryApp.run()