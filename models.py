from inventoryApp import db

class Grocery(db.Model):
	__tablename__ = 'grocery_items'
	
	id = db.Column(db.Integer, primary_key=True)
	description = db.Column(db.String(60), nullable=False)
	last_sold = db.Column(db.Date)
	shelf_life = db.Column(db.String(5), nullable=False)
	department = db.Column(db.String(40))
	price = db.Column(db.String(20), nullable=False)
	unit = db.Column(db.String(10), nullable=False)
	x_for = db.Column(db.Integer, nullable=False)
	cost = db.Column(db.String(20), nullable=False)
	
	def __init__(self, id, description, last_sold, shelf_life, department, price, unit, x_for, cost):
		self.id = int(id)
		self.description = description
		self.last_sold = last_sold
		self.shelf_life = shelf_life
		self.department = department
		self.price = price
		self.unit = unit
		self.x_for = int(x_for)
		self.cost = cost