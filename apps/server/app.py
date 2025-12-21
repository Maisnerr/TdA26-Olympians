from flask import Flask, jsonify, request
from flask_cors import CORS
import json

import src.db as db_module

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)
app.config['CORS_HEADERS'] = "Content-Type"

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:heslo@localhost:5431'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db_module.db.init_app(app)

@app.route("/api/test", methods=["GET"])
def test_endpoint():
    print("Test endpoint was called")
    return jsonify({"message": "This is a test endpoint /test"}), 200


@app.route("/api", methods=["GET"])
def root1():
    return jsonify({"organization": "Student Cyber Games"}), 200

@app.route("/api/", methods=["GET"])
def root2():
    return jsonify({"organization": "Student Cyber Games"}), 200

@app.route("/api/courses", methods=["GET"])
def get_courses():
    return db_module.CourseDB.get(), 200

@app.route("/api/courses", methods=["POST"])
def post_course():
    data = request.get_json()
    mezi = db_module.CourseDB.post(data["title"], data.get("description"))
    return mezi, 201

if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(debug=True, host="0.0.0.0", port=3000)