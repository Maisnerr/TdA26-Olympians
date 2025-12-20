from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = "Content-Type"

@app.route("/", methods=["GET"])
def root():
    return jsonify({"organisation": "Student Cyber Games"}), 200

@app.route("/courses", methods=["GET"])
def get_courses():
    pass
    ## Do after databases

## ...

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=3001)