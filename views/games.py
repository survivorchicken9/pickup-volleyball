from flask import Blueprint, render_template, request, redirect, url_for, session
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
        game_id = request.form.get("game_id")
        name = request.form.get("name")
        position_1 = request.form.get("pos1")
        position_2 = request.form.get("pos2")
        position_3 = request.form.get("pos3")
        years = request.form.get("years")

        if not game_id or not name or not position_1 or not position_2 or not position_3 or not years:
            print("Form not submitted")
            help_msg = "Ensure all fields have been submitted and that your " \
                       "years of experience is inputted as an integer. " \
                       "Make sure you don't have any duplicate positional preferences."
            return render_template("games/fail.html", msg=help_msg)

        else:
            new_player = Player(
                game_id=game_id,
                name=name,
                position_1=pos1,
                position_2=pos2,
                position_3=pos3,
                years=int(years),
            )

            print(new_player)

            new_player.insert_to_players()

            print("success")
            return render_template("games/success.html", player_data=new_player)

@games_blueprint.route('/success', methods=["GET", "POST"])
def success():

@games_blueprint.route('/rsvp', methods=["GET", "POST"])
def rsvp():
    game_id = request.args['game_id']

    if request.method == "GET":
        game_data = Game.find_game(game_id)
        print(game_data)
        return render_template("games/rsvp.html", game_data=game_data, game_id=game_id)
