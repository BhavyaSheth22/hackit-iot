from app import app
from flask import render_template


@app.route("/home")
def home():
    return "Server works"
