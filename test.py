from models.game import Game
from pprint import pprint

all_games_json = Game.get_all_games()  # games in json
newlist = sorted(all_games_json, key=lambda d: d['date'], reverse=True)

pprint(newlist)
