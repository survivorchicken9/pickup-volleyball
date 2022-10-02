from flask import Blueprint, render_template, request, redirect, url_for, session
from models.game import Game
from models.player import Player

games_blueprint = Blueprint('games', __name__)  # useful for redirecting


@games_blueprint.route('/', methods=["GET"])
def index():
    if request.method == "GET":
        games = Game.get_all_games()
        return render_template("games/home.html", games=games)


@games_blueprint.route('/success', methods=["GET", "POST"])
def success():
    if request.method == "GET":
        return render_template("games/success.html")


@games_blueprint.route('/rsvp/<game_id>', methods=["GET", "POST"])
def rsvp(game_id):
    game_data = Game.find_game(game_id)

    print(game_data)

    if request.method == "GET":
        return render_template("games/rsvp.html", game_data=game_data, game_id=game_id)

    if request.method == "POST":
        print(request.form.get)
        new_player = Player(
            game_id=request.form.get(game_id),
            name=request.form.get("name"),
            position_1=request.form.get("pos1"),
            position_2=request.form.get("pos2"),
            position_3=request.form.get("pos3"),
            years=int(request.form.get("years"))
        )

        new_player.insert_to_players()

        print("success")
        return redirect(url_for(".success"))


@games_blueprint.route('/games/rsvp', methods=["GET", "POST"])
def rsvp_t(game_id):
    if request.method == "POST":
        print(request.form.get("name"))
        return render_template("games/home.html")