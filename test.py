from models.game import Game
from pprint import pprint

all_games_json = Game.get_all_games()  # games in json
pprint(all_games_json)