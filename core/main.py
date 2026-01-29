from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # <-- THIS LINE FIXES THE PROBLEM

@app.route("/status")
def status():
    return jsonify({
        "assistant": "VAJRA",
        "state": "Idle",
        "message": "VAJRA brain is online and ready"
    })

if __name__ == "__main__":
    print("Starting VAJRA brain server...")
    app.run(host="127.0.0.1", port=5000, debug=False)
