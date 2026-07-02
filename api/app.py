from flask import Flask, render_template, request, jsonify
from dla import generate_dla

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate")
def generate():
    filename = generate_dla()
    return jsonify({"image": filename})
