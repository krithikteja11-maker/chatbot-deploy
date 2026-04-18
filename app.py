from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app, origins=["*"])

# 🔑 ADD YOUR API KEY HERE
genai.configure(api_key="AIzaSyBUBzYM6a872pdwVR0MeYXkhkrWoncUcH8")

model = genai.GenerativeModel("gemini-pro")

@app.route("/")
def home():
    return "API is running"

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")

    try:
        response = model.generate_content(user_input)
        reply = response.text
    except Exception as e:
        reply = "Error: " + str(e)

    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run()