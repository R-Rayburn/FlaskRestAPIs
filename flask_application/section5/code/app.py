from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from item import Item, ItemList
from security import authenticate, identity
from user import UserRegister

app = Flask(__name__)
# This should be secure when using prod
app.secret_key = 'Jose'
api = Api(app)
jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

# Only run if app.py is ran directly
if __name__ == '__main__':
    app.run(port=5005, debug=True)
