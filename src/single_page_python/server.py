# Copyright 2025 Stefan Meisner Larsen
# Licensed under the MIT License.
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html.j2', title='Single Page Web Application')


def start_server():
    app.run(debug=True, host="localhost")
