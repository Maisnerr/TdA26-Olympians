from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = "Content-Type"



@app.route("/api/test", methods=["GET"])
def test_endpoint():
    print("Test endpoint was called")
    return jsonify({"message": "This is a test endpoint /test"}), 200


@app.route("/api", methods=["GET"])
def root():
    return jsonify({"organisation": "Student Cyber Games"}), 200

@app.route("/api/courses", methods=["GET"])
def get_courses():
    pass
    ## Do after databases

## ...

if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(debug=True, host="0.0.0.0", port=3000)