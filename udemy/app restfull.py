from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT
from security import authenticate, identity
from udemy.resources.user import UserRegister
from udemy.resources.itens import Item


app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth

class Students(Resource):
    def get(self, name):
        return {'students': name}

api.add_resource(Students, '/students/<string:name>')
api.add_resource(Item, '/items/<string:name>')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)  #debug=True significa que ira mostrar o erro antes de executar o servidor