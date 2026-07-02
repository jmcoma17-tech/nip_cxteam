from flask import Flask, render_template, send_file
from pathlib import Path

from dla import generate_dla

BASE_DIR = Path(__file__).resolve().parent.parent

app = Flask(
    __name__,
    template_folder=str(BASE_DIR / "templates")
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate")
def generate():
    image = generate_dla(100)
    return send_file(image, mimetype="image/png")
