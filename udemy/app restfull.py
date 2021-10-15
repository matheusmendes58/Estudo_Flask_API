from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
from user import UserRegister

app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth

items = []
class Students(Resource):
    def get(self, name):
        return {'students': name}

api.add_resource(Students, '/students/<string:name>')

class Items(Resource):
    @jwt_required()
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {'item': None}, 404

    def post(self, name):
        item = {'name': name, 'price': 12.00}
        items.append(item)
        return item, 201

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument('price', type=float, required=True, help='este campo não pode ficar em branco')
        data = parser.parse_args()
        item = next(filter(lambda x: x[name] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item

api.add_resource(Items, '/items/<string:name>')
api.add_resource(UserRegister, '/register')

app.run(port=5000, debug=True)  #debug=True significa que ira mostrar o erro antes de executar o servidor