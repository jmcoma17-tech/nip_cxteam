from flask import Flask, render_template, send_file, request
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

    grid_size = int(request.args.get("grid", 601))
    particles = int(request.args.get("particles", 3600))

    return send_file(
        generate_dla(grid_size, particles),
        mimetype="image/png"
    )
