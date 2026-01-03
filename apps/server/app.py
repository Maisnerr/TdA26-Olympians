from flask import Flask, jsonify, request, send_from_directory, abort
from flask_cors import CORS
import json
import os

import src.db as db_module

## APP initialization
app = Flask(__name__)
app.url_map.strict_slashes = False

## CORS
CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)
app.config['CORS_HEADERS'] = "Content-Type"

## Database Connection
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:heslo@localhost:{os.getenv("PORT", 5432)}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db_module.db.init_app(app)

""""
GET /api/                           """
from src.routes.root import root_bp
app.register_blueprint(root_bp)

""""
Blueprints for:
TYPE   | ENDPOINT
-----------------------------
GET    | /Courses
POST   | /Courses
GET    | /Courses/{CourseId}
PUT    | /Courses/{CourseId}
DELETE | /Courses/{CourseId}          """
from src.routes.courses import courses_bp
app.register_blueprint(courses_bp)

from src.routes.materials import materials_bp
app.register_blueprint(materials_bp)

## CUSTOM ENDPOINTS
@app.route("/api/getstudies/<courses_id>", methods=["GET"])
def getstudies(courses_id):
    return db_module.CustomDB.get_studies(courses_id)
@app.route("/api/getfile/<uuid>", methods=["GET"])
def getfiles(uuid):
    for filename in os.listdir("uploads"):
        if filename.startswith("."):
            continue
        name, ext = os.path.splitext(filename)
        if name == uuid:
            return send_from_directory("uploads", filename)
    
    abort(404, description="File not found")

if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(debug=True, host="0.0.0.0", port=3000)