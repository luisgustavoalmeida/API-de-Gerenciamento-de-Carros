from flask import Flask
from bd import Carros

app = Flask(__name__)

@app.route('/carros', methods=['GET'])
def get_carros():
    return Carros

app.run()
