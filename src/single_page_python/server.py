# Copyright 2025 Stefan Meisner Larsen
# Licensed under the MIT License.
import os
from flask import Flask, make_response, render_template, send_file

NODE_MODULES = "../.."
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html.j2', title='Single Page Web Application')


def start_server():
    app.run(debug=True, host="localhost")
