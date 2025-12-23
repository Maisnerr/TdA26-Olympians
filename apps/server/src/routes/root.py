from flask import Blueprint, jsonify

root_bp = Blueprint("api", __name__, url_prefix="/api")

@root_bp.route("/", methods=["GET"])
def root():
    return jsonify({"organization": "Student Cyber Games"}), 200