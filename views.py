from flask import jsonify
from script import app

@app.route('/')
def home():
    return jsonify({'message':'Welcome to home page'})