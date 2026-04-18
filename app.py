from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os

app = Flask(__name__)

# ✅ Allow your Vercel site ONLY
CORS(app, origins=["*"])   # keep * for now (simple fix)

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/")
def home():
    return "API is running"

@app.route("/chat", methods=["POST", "OPTIONS"])  # 👈 ADD OPTIONS
def chat():
    if request.method == "OPTIONS":
        return jsonify({}), 200

    data = request.get_json()
    user_input = data.get("message", "")

    try:
        response = model.generate_content(user_input)
        reply = response.text
    except Exception as e:
        reply = "Error: " + str(e)

    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run()