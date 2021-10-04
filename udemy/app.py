# Aprendendo a criar uma api de loja com flask
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [{'name': 'my wonderful Store', 'items': [{'name': 'My item', 'price': 15.99}]}]


# POST - used to receive data
# GET  - used to send data back only
@app.route('/')
def home():
    return render_template('index.html')

# ENDPOINTS

# POST    /store data {name}                        vai criar uma nova loja com determinado nome
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {'name': request_data['name'], 'items': []}
    stores.append(new_store)
    return jsonify(new_store)


# GET    /store/<string:name>                       vai pegar uma loja com determinado nome e retornar dados sobre ela
@app.route('/store/<string:name>', methods=['GET'])
def get_store_information_data(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'não achamos nenhuma loja store not found'})


# GET   /store                                      retornara uma lista de lojas
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})


# POST /store/<string:name>/item {name:, price:}    Criara um item dentro de uma loja especifica
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {'name': request_data['name'], 'price': request_data['price']}
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'item nao criado store not found'})

# GET /store/<string:name>/item                     ira pegar todos os itens de uma loja especifica
@app.route('/store/<string:name>/item', methods=['GET'])
def get_all_items_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'não achamos itens items not found'})

app.run(port=5000)
