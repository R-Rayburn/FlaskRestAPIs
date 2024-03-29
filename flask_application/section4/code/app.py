from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

app = Flask(__name__)
# This should be secure when using prod
app.secret_key = 'Jose'
api = Api(app)
jwt = JWT(app, authenticate, identity)  # /auth

items = []


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help='This field cannot be blank.')

    @jwt_required()
    def get(self, name):
        item = next(filter(lambda i: i['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        # get_json params:
        # force -> True means content header doesn't need to be specified
        # silent -> True means it will give you none instead of error
        if next(filter(lambda i: i['name'] == name, items), None) is not None:
            return {'message': f'{name} already exists'}, 400

        data = Item.parser.parse_args()

        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': f'{name} deleted'}

    def put(self, name):
        data = Item.parser.parse_args()

        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {"name": name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item


class ItemList(Resource):
    def get(self):
        return {'items': items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5005, debug=True)
