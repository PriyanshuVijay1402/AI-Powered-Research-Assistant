from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from main import crew
import os

app = Flask(__name__, static_folder="frontend", static_url_path="")
CORS(app)

# Serve index.html
@app.route("/")
def serve_index():
    return send_from_directory("frontend", "index.html")

# Serve other static assets (CSS, JS)
@app.route("/<path:path>")
def serve_static(path):
    return send_from_directory("frontend", path)

# API endpoint for research report
@app.route("/generate-report", methods=["POST"])
def generate_report():
    try:
        data = request.get_json()
        user_input = data.get("user_input", "")

        if not user_input:
            return jsonify({"error": "No input provided"}), 400

        result = crew.kickoff(inputs={"user_input": user_input})
        
        # Extract the final result string
        final_output = str(result) if not isinstance(result, str) else result

        return jsonify({"report": final_output})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
