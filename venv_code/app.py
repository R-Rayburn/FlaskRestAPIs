from flask import Flask, request
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
        # get_json params:
        # force -> True means content header doesn't need to be specified
        # silent -> True means it will give you none instead of error
        request_data = request.get_json()
        if name in [item['name'] for item in items]:
            return {'message': f'{name} already exists'}, 404
        item = {'name': name, 'price': request_data['price']}
        items.append(item)
        return item, 201


class ItemList(Resource):
    def get(self):
        return {'items': items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5005, debug=True)
