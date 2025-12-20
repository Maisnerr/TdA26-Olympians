from flask import Blueprint, jsonify
from src.db import get_connection

user_routes = Blueprint("users", __name__)


@user_routes.route("/", methods=["GET"])
def get_users():
    try:
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(users), 200
    except Exception as error:
        print(f"Error fetching users: {error}")
        return jsonify({"error": "Failed to fetch users"}), 500
