from db import db
from datetime import datetime as dt
class Dish(db.Model):
    __tablename__= 'dish'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String(200), nullable=False)
    is_gluten_free = db.Column(db.Boolean, nullable=False, default = False)
    is_vegetarian = db.Column(db.Boolean, nullable=False, default = False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    def serialize(self):
        return {
            "id":self.id,
            "name":self.name,
            "price":self.price,
            "description":self.description,
            "image":self.image,
            "is_gluten_free":self.is_gluten_free,
            "is_vegetarian":self.is_vegetarian,
            "category_id":self.category_id
        }
