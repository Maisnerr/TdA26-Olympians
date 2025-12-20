from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = "Content-Type"



@app.route("/test", methods=["GET"])
def test_endpoint():
    return jsonify({"message": "This is a test endpoint /test"}), 200



@app.route("/", methods=["GET"])
def root():
    return jsonify({"organisation": "Student Cyber Games"}), 200

@app.route("/courses", methods=["GET"])
def get_courses():
    pass
    ## Do after databases

## ...

if __name__ == '__main__':
    app.run(debug=True, port=3001)