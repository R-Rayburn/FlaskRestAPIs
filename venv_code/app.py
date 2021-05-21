from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
items = []


class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {'item': None, 'message': f'{name} was not found'}, 404

    def post(self, name):
        if name in [item['name'] for item in items]:
            return {'message': f'{name} already exists'}, 404
        item = {'name': name, 'price': 10.00}
        items.append(item)
        return item, 201


api.add_resource(Item, '/item/<string:name>')

app.run(port=5005)
