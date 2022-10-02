import uuid
from common.database import Database
from dataclasses import dataclass, field


@dataclass(eq=False)
class Team:
    collection: str = field(init=False, default="players")
    game_id: str
    outside_hitter_1: str
    outside_hitter_2: str
    middle_blocker_1: str
    opposite_hitter: str
    setter: str
    libero: str
    middle_blocker_2: str
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    def json(self) -> dict:
        return {
            "_id": self._id,
            "game_id": self.game_id,
            "outside_hitter_1": self.outside_hitter_1,
            "outside_hitter_2": self.outside_hitter_2,
            "middle_blocker_1": self.middle_blocker_1,
            "middle_blocker_2": self.middle_blocker_2,
            "opposite_hitter": self.opposite_hitter,
            "setter": self.setter,
            "libero": self.libero,
        }

    def insert_to_teams(self):
        Database.insert_one(self.collection, self.json())

    def _assign_players_to_teams(self) -> dict:
        # logic is something like this
        # finished_team = {
        #     "outside_hitter_1": "",
        #     "outside_hitter_2": "",
        #     "middle_blocker_1": "",
        #     "middle_blocker_2": "",
        #     "setter": "",
        #     "opposite_hitter": "",
        # }
        #
        # choices = ["primary position", "secondary position", "tertiary position"]
        #
        # players_df = df.copy()
        # next_team = finished_team.copy()
        #
        # for position in next_team:
        #     for choice in choices:
        #         try:
        #             next_player_df = players_df[
        #                 players_df[choice].str.contains(position.split("_", 1)[0], case=False)].head(1)
        #             next_player_name = next_player_df["name"].values[0]
        #         except:
        #             continue
        #         else:
        #             next_team[position] = next_player_name
        #             players_df = players_df[players_df["name"] != next_player_name]  # removing added player
        #             break
        return dict()
