from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = "Content-Type"

API = "/api"

@app.route(API+"/", methods=["GET"])
def root():
    return jsonify({"organisation": "Student Cyber Games"}), 200

@app.route(API+"/courses", methods=["GET"])
def get_courses():
    pass
    ## Do after databases

## ...

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=3000)