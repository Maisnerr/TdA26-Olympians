from flask import Blueprint, jsonify, request
from .. import db as db_module

courses_bp = Blueprint("courses", __name__, url_prefix="/api/courses")

@courses_bp.route("/", methods=["GET"])
def get_courses():
    try:
        return jsonify(db_module.CourseDB.get_all_courses()), 200
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "function": "get_courses"}), 500


@courses_bp.route("/", methods=["POST"])
def post_course():
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 415
    try:
        data = request.get_json()

        if(not data["title"]):
            return jsonify({"error": "Title is a required entry"}), 400
        elif(not data["description"]):
            return jsonify({"error": "Description is a required entry"}), 400

        mezi = db_module.CourseDB.post_course(data["title"], data.get("description"))
        return mezi, 201
    
    except Exception as e:
        print("Error creating course:", e)
        return jsonify({"error": "Internal Server Error",
                        "function": "post_course"}), 500


@courses_bp.route("/<course_id>", methods=["GET"])
def get_specific_course(course_id):
    try:
        mezi = db_module.CourseDB.get_specific_course(course_id)
        return mezi, 200
    except Exception as e:
        if(str(e) == "Course not found"):
            return jsonify({"error": "Course not found"}), 404
        return jsonify({"error":"Internal Server Error",
                        "message": str(e),
                        "function": "post_course"}), 500



@courses_bp.route("/<course_id>", methods=["PUT"])
def put_specific_course(course_id):
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 415
    try:
        data = request.get_json()
        if(not data.get("name") and not data.get("description")):
            return jsonify({"error": "Bad request"}), 400
        db_module.CourseDB.put_specific_course(course_id, data.get("name"), data.get("description"))
    except Exception as e:
        print(str(e))
        if(str(e) == "Course not found"):
            return jsonify({"error": "Course not found"}), 404
        return jsonify({"error":"Internal Server Error",
                        "function": "put_specific_course"}), 500

    return jsonify({"message": "Course updated"}), 200


@courses_bp.route("/<course_id>", methods=["DELETE"])
def delete_specific_course(course_id):
    if(not course_id):
        return jsonify({"error": "Body is empty."}), 404
    if(course_id == "*"):
        db_module.CourseDB.delete_all_courses()
        return jsonify(), 205
    try:
        mezi = db_module.CourseDB.delete_course(course_id)
        return mezi, 204
    except Exception as e:
        if str(e) == "Course not found":
            return jsonify({"message": "The requested resource was not found."}), 404
        else:
            print("Error deleting course:", e)
            return jsonify({"error": "Internal Server Error",
                            "function": "delete_specific_course"}), 500
