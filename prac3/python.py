from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    rs = data['rs']
    dollar = rs * 0.012
    return jsonify({"Result": f"Rs{rs} => ${dollar:.2f}"})

app.run(port=8796)