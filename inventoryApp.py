from flask import Flask
inventoryApp = Flask(__name__)

@inventoryApp.route('/')
def hello():
	return "Hello World!"

if __name__ == '__main__':
	inventoryApp.run()