from flask import Blueprint, render_template, request, redirect, url_for, session

from common.forms import GameRSVPForm
from models.game import Game
from models.player import Player
from datetime import date, datetime

games_blueprint = Blueprint('games', __name__)  # useful for redirecting


@games_blueprint.route('/', methods=["GET"])
def index():
    if request.method == "GET":
        games = Game.get_all_games()

        # Remove all events that have passed
        today = date.today()

        for game in games:
            event_date = game['date']
            event_date_object = datetime.strptime(event_date, '%Y-%m-%d').date()
            if event_date_object < today:
                print(f"{event_date_object} is before today")
            else:
                print(f"{event_date_object} is after today")

        return render_template("games/home.html", games=games)


@games_blueprint.route('/success', methods=["GET", "POST"])
def success():
    if request.method == "POST":
        # game_id = request.form.get("game_id")
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

        print(new_player)


@games_blueprint.route('/rsvp', methods=["GET", "POST"])
def rsvp():
    game_id = request.args['game_id']

    if request.method == "GET":
        game_data = Game.find_game(game_id)
        form = GameRSVPForm()
        return render_template("games/rsvp.html", title="RSVP", form=form, game_data=game_data, game_id=game_id)
