from flask import Flask, request, jsonify
import time  # Import time module for delay

app = Flask(__name__)

latest_data = {"slope": None, "peak": None}  # Store latest values

@app.route('/receive_data', methods=['POST'])
def receive_data():
    global latest_data
    data = request.get_json()
    latest_data["slope"] = data.get("slope")
    latest_data["peak"] = data.get("peak")

    print(f"Received Slope: {latest_data['slope']}, Peak: {latest_data['peak']}")  
    
    time.sleep(5)  # Introduce a 5-second delay before responding

    return jsonify({"message": "Data received", "slope": latest_data["slope"], "peak": latest_data["peak"]})

@app.route('/get_latest_data', methods=['GET'])
def get_latest_data():
    return jsonify(latest_data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)



