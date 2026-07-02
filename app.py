from flask import Flask, render_template

app = Flask(name)

@app.route("/")

def home():

return "<h1>DLA Physics App</h1><p>Hello from Vercel!</p>"
