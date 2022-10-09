from flask import Blueprint, render_template, request, redirect, url_for, session

from common.forms import GameRSVPForm
from models.game import Game
from models.player import Player
from datetime import date, datetime
from common.gifs import get_random_gif

games_blueprint = Blueprint('games', __name__)  # useful for redirecting


@games_blueprint.route('/', methods=["GET"])
def index():
    if request.method == "GET":
        games = Game.get_all_games()

        # Remove all events that have passed
        today = date.today()

        for game in games:
            game['gif'] = get_random_gif()

        return render_template("games/home.html", games=games)


@games_blueprint.route('/rsvp/<string:game_id>', methods=['GET', 'POST'])
def rsvp(game_id):
    if request.method == 'POST':
        game_id = request.args.get('game_id')
        name = request.form.get("name")
        position_1 = request.form.get("position_1")
        position_2 = request.form.get("position_2")
        position_3 = request.form.get("position_3")
        years = request.form.get("years")

        new_player = Player(
            game_id=game_id,
            name=name,
            position_1=position_1,
            position_2=position_2,
            position_3=position_3,
            years=int(years),
        )

        new_player.insert_to_players()

        print(new_player)
        print("success")
        return render_template("games/success.html")

    else:
        game_data = Game.find_game(game_id)
        form = GameRSVPForm()
        return render_template("games/rsvp.html", title="RSVP", form=form, game_data=game_data, game_id=game_id)
