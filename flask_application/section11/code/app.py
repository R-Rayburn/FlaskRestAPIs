from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api

from resources.item import Item, ItemList
from resources.user import User, UserRegister
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
# This should be secure when using prod
app.secret_key = 'Jose'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWTManager(app)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserRegister, '/register')

# Only run if app.py is ran directly
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5005, debug=True)
