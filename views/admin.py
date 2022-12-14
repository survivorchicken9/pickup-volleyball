import flask
from flask_login import login_user, logout_user

from common.forms import NewEventForm, LoginForm
from models.game import Game
from models.admin import Admin
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.security import check_password_hash, generate_password_hash

admin_blueprint = Blueprint('admin', __name__)  # useful for redirecting


@admin_blueprint.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        games = Game.get_all_games()

        return render_template("admin/home.html", games=games)


def is_safe_url(next):
    pass


@admin_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        user = Admin(
            username=request.form.get("username"),
            password=request.form.get("password")
        )
        login_user(user)
        session["logged_in"] = True

        return redirect(flask.url_for('.home'))

    return flask.render_template('admin/login.html', form=form)


# @admin_blueprint.route("/login", methods=["GET", "POST"])
# def login():
#     # Forget any user info
#     session.clear()
#
#     if request.method == "POST":
#         username = request.form.get("username")
#         password = request.form.get("password")
#
#         check_username = Admin.find_admin(username)
#
#         print(check_username)
#
#         print(check_username)
#
#         return redirect(url_for(".home"))
#
#     else:
#         return render_template("admin/login.html")


@admin_blueprint.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        key = request.form.get("key")
        hashpass = generate_password_hash(password)

        admin = Admin(
            username=username,
            password=hashpass
        )

        print(admin)

        return redirect(url_for(".login"))
    else:
        return render_template("admin/register.html")


@admin_blueprint.route('/new-event', methods=['GET', 'POST'])
def new_event():
    if request.method == 'POST':
        new_game = Game(
            date=request.form.get("date"),
            location=request.form.get("location"),
            start_time=request.form.get("start_time"),
            end_time=request.form.get("end_time"),
            notes=request.form.get("notes"),
            number_of_players=int(request.form.get("number_of_players")),
            number_of_teams=int(request.form.get("number_of_teams"))
        )

        new_game.insert_to_games()

        print(new_game)
        print("success")
        return render_template("admin/success.html")
    else:
        form = NewEventForm()
        return render_template("admin/new-event.html", form=form)


@admin_blueprint.route("/view-events", methods=["GET", "POST"])
def view_events():
    if request.method == "GET":
        games = Game.get_all_games()
        return render_template("admin/view-events.html", games=games)

@admin_blueprint.route("/logout", methods=["GET", "POST"])
def logout():
    if request.method == "GET":
        logout_user()
        session["logged_in"] = False
        return redirect("/")