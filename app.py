from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def home():
    return "API is running"

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    response = "You said: " + user_input
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run()