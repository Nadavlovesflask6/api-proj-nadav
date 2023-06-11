from flask import request
from flask_restful import Resource
from models.dish import Dish
from db import db
class DishAll(Resource):
    def get(self):
        #category_id=request.args.get('category_id')
        dishes = Dish.query.filter_by(**request.args).all()
        return [dish.serialize() for dish in dishes]
    def post(self):
        data = request.get_json()
        try:
            dish = Dish(**data)
            # recipe = Recipe(
            #     title=data['title'],
            #     content=data['content'],
            #     imageUrl=data['imageUrl'],
            #     category_id=data['category_id']
            # )
            db.session.add(dish)
            db.session.commit()
            return {'message':f'{dish.title} was added!'}, 201
        except:
            return {'message':'bad request'},400

class DishOne(Resource):
    def get(self,id):
        dish = Dish.query.get(id)
        return dish.serialize()
    def delete(self,id):
        dish = Dish.query.get(id)
        db.session.delete(dish)
        db.session.commit()
        return {'message':'dish was deleted!'}
    
class DishFilter(Resource):
    def get(self,category_id):
        dishes = Dish.query.filter_by(category_id=category_id).all()
        return [dish.serialize() for dish in dishes]