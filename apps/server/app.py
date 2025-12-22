from flask import Flask, jsonify, request
from flask_cors import CORS
import json

import src.db as db_module

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)
app.config['CORS_HEADERS'] = "Content-Type"

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:heslo@localhost:65432' ## OPRAVIT NA 5432
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db_module.db.init_app(app)

@app.route("/api", methods=["GET"])
def root1():
    return jsonify({"organization": "Student Cyber Games"}), 200

@app.route("/api/", methods=["GET"])
def root2():
    return jsonify({"organization": "Student Cyber Games"}), 200

@app.route("/api/courses", methods=["GET"])
def get_courses():
    try:
        return db_module.CourseDB.get(), 200
    except Exception as e:
        print("Error fetching courses:", e)
        return jsonify({"error": "Internal Server Error", "function": "get_courses"}), 500

@app.route("/api/courses", methods=["POST"])
def post_course():
    try:
        data = request.get_json()
        mezi = db_module.CourseDB.post(data["title"], data.get("description"))
        return mezi, 201
    except Exception as e:
        print("Error creating course:", e)
        return jsonify({"error": "Internal Server Error",
                        "function": "post_course"}), 500
    

def get_specific_course():
    pass


def put_specific_course():
    pass

@app.route("/api/courses/<course_id>", methods=["DELETE"])
def delete_specific_course(course_id):
    print("[X] - Pokus o DELETE_COURSE")
    try:
        print("[X] - Try DELETE_COURSE")
        mezi = db_module.CourseDB.delete(course_id)
        print("[X] - return DELETE_COURSE")
        return mezi, 204
    except Exception as e:
        print("[X] - Nastal error")
        if str(e) == "Course not found":
            print("[X] - Ocekavany error")
            return jsonify({"message": "The requested resource was not found."}), 404
        else:
            print("[X] - Neocekavany error")
            print("Error deleting course:", e)
            return jsonify({"error": "Internal Server Error",
                            "function": "delete_specific_course"}), 500

if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(debug=True, host="0.0.0.0", port=3000)