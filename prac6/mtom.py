from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)

folder = "uploads"
os.makedirs(folder, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['file']
    path = os.path.join(folder, f.filename)
    f.save(path)
    return {"message": "File uploaded"}

@app.route('/download/<name>', methods=["GET"])
def download(name):
    return send_from_directory(folder, name, as_attachment=True)

app.run(port=5002)