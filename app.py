from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "API is running"

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]

    # Simple response (we will upgrade later)
    response = "You said: " + user_input

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run()