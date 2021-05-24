from flask_jwt import jwt_required
from flask_restful import Resource, reqparse

from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='This field cannot be blank.')

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_my_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    def post(self, name):
        if ItemModel.find_my_name(name):
            return {'message': f'{name} already exists'}, 400

        data = Item.parser.parse_args()

        item = ItemModel(name, data['price'])

        try:
            item.save_to_db()
        except:
            return {'message': 'An error occurred inserting the item'}, 500  # internal server error

        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_my_name(name)
        if item:
            item.delete_from_db()

        return {'message': f'{name} deleted'}

    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_my_name(name)

        if item:
            item.price = data['price']
        else:
            item = ItemModel(name, data['price'])

        item.save_to_db()

        return item.json()


class ItemList(Resource):
    def get(self):
        # list(map(lambda x: x.json(), ItemModel.query.all()))
        return {'item': [item.json() for item in ItemModel.query.all()]}
