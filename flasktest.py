from flask import Flask
from flask import request

node = Flask(__name__)
this_nodes_transactions = []

@node.route('/', methods=['POST'])
def transaction():
    if request.method == 'POST'
        newtxion = request.get_json()
        this_nodes_transactions.append(newtxion)

node.run()
