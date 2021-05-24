from flask_jwt import jwt_required
from flask_restful import Resource, reqparse

from ..models.item import ItemModel

import sqlite3


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
            item.insert()
        except:
            return {'message': 'An error occurred inserting the item'}, 500  # internal server error

        return item.json(), 201

    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'DELETE FROM items WHERE name=?'
        cursor.execute(query, (name,))

        connection.commit()
        connection.close()

        return {'message': f'{name} deleted'}

    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_my_name(name)
        updated_item = ItemModel(name, data['price'])

        if item:
            try:
                updated_item.update()
            except:
                return {'message': 'An error occurred updating the item'}, 500
        else:
            try:
                updated_item.insert()
            except:
                return {'message': 'An error occurred inserting the item'}, 500

        return updated_item.json()


class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items"
        rows = cursor.execute(query)
        items = [{'name': row[0], 'price': row[1]} for row in rows]

        connection.close()

        return {'items': items}
