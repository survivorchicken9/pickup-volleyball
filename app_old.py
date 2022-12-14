from flask import Flask, render_template, request, redirect
from flask_session import Session
from models.game import Game
from models.player import Player
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/", methods=["GET", "POST"])
def index():
    # If button was clicked to redirect
    if request.method == "POST":
        return redirect("/pickup")
    # If page was navigated to normally
    else:
        return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        key = request.form.get("key")

        print(f"Username: {username}\nPassword: {password}\nConfirmation: {confirmation}\nKey:{key}")

        return render_template("register.html")
    else:
        return render_template("register.html")


@app.route("/pickup", methods=["GET", "POST"])
def pickup():
    if request.method == "POST":
        new_player = Player(
            game_id=request.form.get("name"),
            position_1=request.form.get("pos1"),
            position_2=request.form.get("pos2"),
            position_3=request.form.get("pos3"),
            years=int(request.form.get("years"))
        )
        new_player.insert_to_players()

        return render_template("rsvp.html")

    # If page link was clicked via homepage
    if request.method == "GET":
        positions = ['Outside Hitter', 'Opposite Hitter', 'Libero', 'Middle Blocker', 'Setter']

        return render_template("rsvp.html", positions=positions)


@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "GET":
        return render_template("home.html")
