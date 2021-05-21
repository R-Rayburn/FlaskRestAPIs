##Some HTTP Terms and info:

**Web Server** is software designed to accept
incoming web requests.

GET request: **GET / HTTP/1.1**
- **Get**: verb
- **/**: path
- **HTTP/1.1**: Protocol


For twitter login, https://twitter.com/login
the request looks like this:
- GET /login HTTP/1.1
- Host: https://twitter.com

HTTP Verbs:

| verb   | meaning | example |
| ------ | --------- | ------- |
| GET    | Retrieve something | GET /item/1 |
| POST   | Receive data and use it. Could pass in data like { 'name': 'Chair', 'price': 9.99 } | POST /item |
| PUT    | Make sure something is there.Could pass in something like {'name': 'Chair', 'price': 7.99}, if it exists could update it, if not, then create it | PUT /item |
| DELETE | Remove something | DELETE /item/1 |

REST APIs give us resources when we make requests

Item Resource
- GET /item/chair
- POST /item/chair with extra data
- PUT /item/chair with extra data
- DELETE /item/chair

ItemList Resource
- GET /items

REST is Stateless
- one request cannot depend on other requests
- server only knows about current request and not previous ones
- Example:
  - POST /item/chair creates an item
  - server does not know the item exists
  - GET /item/chair then checks the database to see if the item is there.
- Example 2:
  - user logs into application
  - server doesn't know the user is logged in
  - application must send enough data to identify the user
    in every request, or else the server won't associate the request
    with the user.

## Using virtual environment
- Install virtualenv with the version of pip you would like
- Set python version in env by running _virtualevn venv --python=pythonX.X_
- Activate with source venv/bin/activate
- deactivate with _deactivate_
- Note: Might need to run pip install under sudo if not root user.
