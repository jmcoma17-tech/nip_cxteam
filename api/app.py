from flask import Flask, render_template, jsonify
from dla import generate_dla

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

app = Flask(
    __name__,
    template_folder=str(BASE_DIR / "templates"),
    static_folder=str(BASE_DIR / "static")
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate")
def generate():
    return jsonify({
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Fronalpstock_big.jpg"
    })
