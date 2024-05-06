"""first configs"""
from flask import Flask
from flask_cors import CORS
from flask import make_response, jsonify



app = Flask(__name__)
CORS(app)

@app.get("/")
def response_api():
    return make_response(
        jsonify({
            "msg": "api record video on air"
        }),
        
    )
