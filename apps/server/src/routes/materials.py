from flask import Blueprint, jsonify, request
from .. import db as db_module
import os

materials_bp = Blueprint("materials", __name__, url_prefix="/api/courses/<course_id>/materials")

ALLOWED_EXTENSIONS = {
    "pdf", "docx", "txt",
    "png", "jpg", "jpeg", "gif",
    "mp4",
    "mp3",
}

UPLOADS = "uploads"
os.makedirs(UPLOADS, exist_ok=True)

@materials_bp.route("/", methods=["GET"])
def get_materials(course_id):
    try:
        materials = db_module.MaterialDB().materials_from_id(course_id)
        return jsonify(materials), 200
    except Exception as e:
        print(str(e))
        if(str(e)=="Error while looking for course"):
            return jsonify({"error": "Course not found"}), 404
        return jsonify({"error": "Internal Server Error",
                        "function": "get_materials"}), 500
    
@materials_bp.route("/", methods=["POST"])
def post_materials(course_id):
    content_type = request.content_type or ""

    if request.is_json:
        data = request.get_json()
        name, description, url = data["name"], data["description"], data["url"]
        try:
            mezi = db_module.MaterialDB().post_materials_url(course_id, name, description, url)
            return jsonify(mezi), 201
        except Exception as e:
            if(str(e) == "Course not found"):
                return jsonify({"error": "Course Not Found"}), 404
            return jsonify({"error": "Internal Server Error",
                            "function": "post_materials (URL)"}),500
        
    elif content_type.startswith("multipart/form-data"):
        data = request.form
        file = request.files.get("file")

        name, description = data["name"], data["description"]

        if not name or name == "":
            return {"error": "name is required"}, 400

        if not file or file.filename == "":
            return {"error": "file is required"}, 400

        try:
            mezi = db_module.MaterialDB().post_materials_file(course_id, name, description)
            if(mezi["message"] == "ok"):
                print("OK", mezi["uuid"])
                uuid = mezi["uuid"]
            else:
                print("NOK")
                raise Exception
        except Exception as e:
            print(str(e))
            return jsonify({"error": "Internal server error",
                            "message": str(e),
                            "function": "post_materials (FILE)"}), 500

        extension = os.path.splitext(file.filename)[1]
        if (extension.replace(".", "") not in ALLOWED_EXTENSIONS):
            db_module.MaterialDB().stop_post_file(uuid)
            return jsonify({"error": "Extension mismatch"}), 400

        file.seek(0, 2)
        size_bytes = file.tell()
        file.seek(0)

        if(size_bytes > (30*1024*1024)):
            db_module.MaterialDB().stop_post_file(uuid)
            return jsonify({"error": "File too large (>30MB)"}), 400
        
        mimeType = file.mimetype.split(";")[0]

        try:
            mezi = db_module.MaterialDB().complete_post_file(uuid, size_bytes, extension, mimeType)
        except Exception as e:
            print(str(e))
            db_module.MaterialDB().stop_post_file(uuid)
            return jsonify({"error": "Internal server error",
                            "function": "post_materials (FILE)"}), 500

        path = os.path.join(UPLOADS, f"{uuid}{extension}")
        file.save(path)

        return jsonify(mezi), 200
    else:
        return jsonify({"error": "Unsupported Content-Type"}), 415
    
@materials_bp.route("/<material_id>", methods=["PUT"])
def put_materials(course_id, material_id):
    content_type = request.content_type or ""

    if request.is_json:
        data = request.get_json()
        name = data["name"]
        description = data["description"]
        url = data["url"]

        if(not name and not description and not url):
            return jsonify({"error": "No parameter was given"}), 400
        
        mezi = db_module.MaterialDB().put_materials_url(course_id, material_id, name, description, url)

        return mezi
    elif content_type.startswith("multipart/form-data"):
        print("FILE")
    else:
        return jsonify({"error": "Unsupported Content-Type"}), 415

    return jsonify({"message": "ok"}), 200

@materials_bp.route("/<material_id>", methods=["DELETE"])
def delete_materials(course_id, material_id):
    try:
        db_module.MaterialDB().delete_material(course_id, material_id)
    except Exception as e:
        if(str(e) == "Material not found"):
            return jsonify({"error": "Material not found"}), 404
        print(str(e))
        return jsonify({"error": "Internal server error"}), 500
    
    return jsonify(), 204