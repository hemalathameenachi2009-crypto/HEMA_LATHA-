from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/sos', methods=['POST'])
def sos():
    data = request.json
    print("SOS:", data)
    return jsonify({"status":"ok"})

@app.route('/report', methods=['POST'])
def report():
    data = request.json
    print("Report:", data)
    return jsonify({"status":"saved"})

if __name__ == '__main__':
    app.run(debug=True)
