from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# ✅ FORCE CORS PROPERLY
CORS(app, origins=["*"])

@app.route("/")
def home():
    return "API is running"

@app.route("/chat", methods=["POST", "OPTIONS"])
def chat():
    if request.method == "OPTIONS":
        return '', 200

    user_input = request.json.get("message", "")
    response = "You said: " + user_input
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run()