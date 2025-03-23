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


#Run server
if __name__ == '__main__':
    app.run(debug=True)