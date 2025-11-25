from flask import Flask, jsonify, request
from http import HTTPStatus

app = Flask(__name__)

@app.route('/api/recipes', methods=['GET'])
def get_recipes():
    return jsonify({'recipes': []}), HTTPStatus.OK