from flask import Blueprint, jsonify, request
from .. import db as db_module

materials_bp = Blueprint("materials", __name__, url_prefix="/api/courses/<course_id>/materials")

@materials_bp.route("/", methods=["GET"])
def get_materials(course_id):
    try:
        materials = db_module.MaterialDB().materials_from_id(course_id)
        return jsonify(materials), 200
    except Exception as e:
        if(str(e)=="Error while looking for course"):
            return jsonify({"error": "Course not found"}), 404
        return jsonify({"error": "Internal Server Error",
                        "message": str(e),
                        "function": "get_materials"}), 500
    
@materials_bp.route("/", methods=["POST"])
def post_materials(course_id):
    content_type = request.content_type or ""

    if request.is_json:
        data = request.get_json()

        try:
            mezi = db_module.MaterialDB().post_materials_url(course_id, data)
        except Exception as e:
            if(str(e) == "Course not found"):
                return jsonify({"error": "Course Not Found"}), 404
            return jsonify({"error": "Internal Server Error",
                            "message": str(e),
                            "function": "post_materials (URL)"})

        return jsonify(mezi), 201
    elif content_type.startswith("multipart/form-data"):
        data = request.form
        files = request.files
    else:
        return jsonify({"error": "Unsupported Content-Type"}), 415