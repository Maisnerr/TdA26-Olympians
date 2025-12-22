from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="src", static_url_path="")

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/login")
def test():
    return send_from_directory(app.static_folder, "login.html")

@app.route("/courses")
def courses():
    return send_from_directory(app.static_folder, "test.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3001)