from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Initialize application
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    

# Initialize database
db = SQLAlchemy(app)
ma = Marshmallow(app)


# Product class model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    def __init__(self, name, description, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty

# Product schema
class ProductSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "description", "price", "qty")

# Initialize schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)


# craete a product 
@app.route(`/product`,mehods=[`POST`])
def add_product():
    name = request.json[`name`]
    description = request.json[`description`]
    price = request.json[`price`]
    qty = request.json[`qty`]
 

# Create database tables - modern approach
with app.app_context():
    db.create_all()

# Run server
if __name__ == '__main__':
    app.run(debug=True)