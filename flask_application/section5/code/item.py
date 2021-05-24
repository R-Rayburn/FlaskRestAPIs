from flask_jwt import jwt_required
from flask_restful import Resource, reqparse

import sqlite3


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='This field cannot be blank.')

    @jwt_required()
    def get(self, name):
        item = self.find_my_name(name)
        if item:
            return item
        return {'message': 'Item not found'}, 404

    @classmethod
    def find_my_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item': {'name': row[0], 'price': row[1]}}
        return None

    def post(self, name):
        if self.find_my_name(name):
            return {'message': f'{name} already exists'}, 400

        data = Item.parser.parse_args()

        item = {'name': name, 'price': data['price']}
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES (?, ?)"
        cursor.execute(query, (item['name'], item['price'],))

        connection.commit()
        connection.close()

        return item, 201

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

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        if self.find_my_name(name):
            query = 'UPDATE items SET price=? where name=?'
            cursor.execute(query, (data['price'], name,))
        else:
            query = 'INSERT INTO items VALUES (?, ?)'
            cursor.execute(query, (name, data['price'],))

        connection.commit()
        connection.close()

        return {'name': name, 'price': data['price']}


class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM items"
        rows = cursor.execute(query)
        items = [{'name': row[0], 'price': row[1]} for row in rows]
        connection.close()
        return {'items': items}
