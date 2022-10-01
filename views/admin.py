from flask import Blueprint, render_template, request, redirect, url_for, session
from models.game import Game

admin_blueprint = Blueprint('admin', __name__)  # useful for redirecting


@admin_blueprint.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        return redirect(url_for(".dashboard"))

    else:
        return render_template("admin/login.html")


@admin_blueprint.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    # flow for creating a new game
    if request.method == "POST":
        new_game = Game(
            date=request.form.get("date"),
            location=request.form.get("location"),
            start_time=request.form.get("start"),
            end_time=request.form.get("end"),
            notes=request.form.get("notes")
        )
        new_game.insert_to_games()

        message = "Form Successfully Submitted!"
        return render_template("success.html", message=message)

    # admin home page (dashboard)
    if request.method == "GET":
        all_games_json = Game.get_all_games()  # games in json
        return render_template("dashboard.html")
