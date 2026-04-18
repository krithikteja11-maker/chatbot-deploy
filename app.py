from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os

app = Flask(__name__)

# Enable CORS (safe for now)
CORS(app, resources={r"/*": {"origins": "*"}})

# 🔐 Use environment variable (DO NOT hardcode key)
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# Load model
model = genai.GenerativeModel("gemini-pro")

@app.route("/")
def home():
    return "API is running"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_input = data.get("message", "")

        if not user_input:
            return jsonify({"response": "Please send a message."})

        # 🤖 Get AI response
        response = model.generate_content(user_input)
        reply = response.text

        return jsonify({"response": reply})

    except Exception as e:
        return jsonify({"response": "Error: " + str(e)})

if __name__ == "__main__":
    app.run()