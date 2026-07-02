from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>DLA Physics App</h1>
    <p>Your Vercel deployment is working! 🎉</p>
    """
