# Copyright 2025 Stefan Meisner Larsen
# Licensed under the MIT License.
import os
from flask import Flask, make_response, render_template, send_file

NODE_MODULES = "npm"
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html.j2', title='Single Page Web Application')


@app.route('/npm/<path:filename>', methods=['GET'])
def npm(filename):
    try:
        if '..' in filename:
            return make_response('Illegal path', 401)
        filepath = os.path.join(NODE_MODULES, filename)
        return send_file(filepath)
    except Exception as e:
        return make_response(f'Error: {str(e)}', 500)
    

def start_server():
    app.run(debug=True, host="localhost")
