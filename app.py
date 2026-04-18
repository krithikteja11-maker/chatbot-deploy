from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os

app = Flask(__name__)

# ✅ Allow all origins (fixes CORS)
CORS(app, resources={r"/*": {"origins": "*"}})

# 🔐 Load API key from environment variable
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# ✅ Correct working model
model = genai.GenerativeModel("gemini-1.5-flash")

# 🔥 Debug line to confirm deployment
print("🔥 NEW CODE DEPLOYED — GEMINI 1.5 FLASH")

@app.route("/")
def home():
    return "API is running"

@app.route("/chat", methods=["POST", "OPTIONS"])
def chat():
    # Handle preflight request (CORS)
    if request.method == "OPTIONS":
        return jsonify({}), 200

    try:
        data = request.get_json()
        user_input = data.get("message", "")

        if not user_input:
            return jsonify({"response": "Please enter a message."})

        # 🤖 Get AI response
        response = model.generate_content(user_input)

        # Some responses may not have .text (safety)
        reply = response.text if hasattr(response, "text") else "No response from AI."

        return jsonify({"response": reply})

    except Exception as e:
        return jsonify({"response": "Error: " + str(e)})

if __name__ == "__main__":
    app.run()