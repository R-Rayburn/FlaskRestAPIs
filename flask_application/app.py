from flask import Flask

app = Flask(__name__)


# POST /store data: {name:} creates store
@app.route('/store', methods=['POST'])
def create_store():
    pass


# GET /store/<string:name> gets store and return data
@app.route('/store/<string:name>')  # http://127.0.0.1:5005/store/some_name
def get_store(name):
    pass


# GET /store return list of stores
@app.route('/store')
def get_stores():
    pass


# POST /store/<string:name>/item {name:, price:} creates item in store
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass


# GET /store/<string:name>/item  gets items in store
@app.route('/store/<string:name>/item')
def get_items_in_store():
    pass


app.run(port=5005)
