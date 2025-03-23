from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
#initialize application
app = Flask(__name__)

basedir = os.path.dirname(os.path.dirname(__file__))

#Database
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    

#nitialze database
db = SQLAlchemy(app)
ma = Marshmallow(app)


# products class model
class Products(db.Model):
    id = db.column(db.Integer, primary_key=True)
    name = db.column(db.String(100),unique=True)
    description = db.column(db.String(200))
    price = db.column(db.Float)
    qty = db.column(db.Integer)

    def __nint__(self,name,description,price,qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty

# product schema
class ProductSchema(ma.schema):
    class meta:
        fields = ("id","name","description","price", "qty")

#init schema

product_schema = ProductSchema(strict=True)
products_schema = roductSchema(many=True,strict=True)

#Run server
if __name__ == '__main__':
    app.run(debug=True)