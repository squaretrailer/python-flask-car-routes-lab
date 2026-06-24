#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

@app.route("/")
def index():
    return '<h1>Welcome to Flatiron Cars</h1>'

@app.route("/<string:model>")
def model_lookup(model):
    if model in existing_models:
        return f'<h1>Flatiron {model} is in our fleet!</h1>'
    return f'<h1>No models called {model} exists in our catalog</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)