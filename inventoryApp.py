from flask import Flask
inventoryApp = Flask(__name__)

@inventoryApp.route('/')
def hello():
	return "Hello World!"
	
@inventoryApp.route('/<name>')
def hello_name(name):
	return "Hello {}!".format(name)

if __name__ == '__main__':
	inventoryApp.run()