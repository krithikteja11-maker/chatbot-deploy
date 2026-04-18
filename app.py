from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os

app = Flask(__name__)
CORS(app)

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# ✅ Correct modern model
model = genai.GenerativeModel("models/gemini-1.5-flash")

print("🔥 USING GEMINI 1.5 FLASH (FIXED)")

@app.route("/")
def home():
    return "API is running"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_input = request.json.get("message", "")

        response = model.generate_content(user_input)

        return jsonify({
            "response": response.text
        })

    except Exception as e:
        return jsonify({
            "response": "Error: " + str(e)
        })

if __name__ == "__main__":
    app.run()