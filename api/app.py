from flask import Flask, render_template, send_file, request
from pathlib import Path
from io import BytesIO
from dla import generate_dla

BASE_DIR = Path(__file__).resolve().parent.parent

app = Flask(
    __name__,
    template_folder=str(BASE_DIR / "templates")
)

@app.route("/generate")
def generate():
    return jsonify({
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Fronalpstock_big.jpg"
    })

    image = generate_dla(particles)

    return send_file(
        image,
        mimetype="image/png"
    )
