from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_restful import Api

from resources.item import Item, ItemList
from resources.user import User, UserRegister, UserLogin, TokenRefresh
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
# This should be secure when using prod
app.secret_key = 'Jose'  # app.config['JWT_SECRET_KEY']
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWTManager(app)


@jwt.additional_claims_loader
def add_claims_to_jwt(identity):
    if identity == 1:  # value to check should be read from config or db.
        return {'is_admin': True}
    return {'is_admin': False}


@jwt.expired_token_loader
def expired_token_callback():
    return jsonify({
        'description': 'The token has expired.',
        'error': 'token_expired'
    }), 401


@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({
        'description': 'Signature verification failed.',
        'error': 'invalid_token'
    }), 401


@jwt.unauthorized_loader
def unauthorized_callback():
    return jsonify({
        'description': 'Request does not have access token.',
        'error': 'unauthorized'
    }), 401


@jwt.needs_fresh_token_loader
def needs_fresh_token_callback():
    return jsonify({
        'description': 'Token is not fresh.',
        'error': 'fresh_token_required'
    }), 401


@jwt.revoked_token_loader
def revoked_token_callback():
    return jsonify({
        'description': 'This token has been revoked.',
        'error': 'revoked_token'
    }), 401


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(TokenRefresh, '/refresh')

# Only run if app.py is ran directly
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5005, debug=True)
