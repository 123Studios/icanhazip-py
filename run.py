from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def index():
    t = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)   
    return (t)

app.run(host='0.0.0.0', port=81)

