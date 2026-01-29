from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # <-- THIS LINE FIXES THE PROBLEM
assistant_state = {
    "assistant": "VAJRA",
    "state": "idle",
    "message": "Friday is ready"
}

@app.route("/status")
def status():
    return jsonify(assistant_state)


if __name__ == "__main__":
    print("Starting VAJRA brain server...")
    app.run(host="127.0.0.1", port=5000, debug=False)
