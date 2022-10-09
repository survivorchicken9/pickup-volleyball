from flask import Blueprint, flash, render_template, request, redirect, url_for, session
from models.game import Game
from flask import Blueprint, render_template, request, redirect, url_for, session
from werkzeug.security import check_password_hash, generate_password_hash

admin_blueprint = Blueprint('admin', __name__)  # useful for redirecting


@admin_blueprint.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        games = Game.get_all_games()
        return render_template("admin/home.html", games=games)


@admin_blueprint.route("/login", methods=["GET", "POST"])
def login():

    # Forget any user info
    session.clear()

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        return redirect(url_for(".home"))

    else:
        return render_template("admin/login.html")


@admin_blueprint.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        key = request.form.get("key")
        hashpass = generate_password_hash(password)

        admin = admin(
            username=username,
            password=hashpass
        )

        print(admin)

        return redirect(url_for(".login"))
    else:
        return render_template("admin/register.html")


@admin_blueprint.route("/new-event", methods=["GET", "POST"])
def new_event():
    # flow for creating a new game
    if request.method == "POST":
        date = request.form.get("date")
        location = request.form.get("location")
        start_time = request.form.get("start")
        end_time = request.form.get("end")
        notes = request.form.get("notes")
        number_of_teams = request.form.get("number_of_teams")

        if not date:
            print("No date was entered")
        if not location:
            print("No date was entered")
        if not start_time or not end_time:
            print("No time")
        if not notes:
            print("No notes")
        if not number_of_teams:
            print("No teams")
        else:
            new_game = Game(
                date=date,
                location=location,
                start_time=start_time,
                end_time=end_time,
                notes=notes,
                number_of_teams=number_of_teams,
            )
            new_game.insert_to_games()
            flash("Success")
            message = "Form Successfully Submitted!"
            return render_template("admin/success.html", message=message)

    # admin home page (dashboard)
    if request.method == "GET":
        all_games_json = Game.get_all_games()  # games in json

        return render_template("admin/new-event.html")


@admin_blueprint.route("/view-events", methods=["GET", "POST"])
def view_events():
    if request.method == "GET":
        games = Game.get_all_games()
        return render_template("admin/view-events.html", games=games)
