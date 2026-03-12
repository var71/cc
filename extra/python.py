from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    f = data['fahrenheit']

    celsius = (f - 32) * 5/9

    return jsonify({"Result": f"{f}F => {celsius:.2f}C"})

app.run(port=8796)
