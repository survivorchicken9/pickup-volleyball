from flask import Blueprint, render_template, request, redirect, url_for, session
from models.game import Game

games_blueprint = Blueprint('games', __name__)  # useful for redirecting


@games_blueprint.route('/')
def index():
    alerts = Game.get_all_games()
    return render_template('index')
