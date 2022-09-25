from flask import Flask, render_template, request, session, flash, redirect
from flask_session import Session
from jinja2 import Template
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime


app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    # If form was submitted
    if request.method == "POST":
        return redirect("/dashboard")

    # If form link was clicked via navbar
    else:
        return render_template("login.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dash():
    if request.method == "GET":
        return render_template("dashboard.html")
