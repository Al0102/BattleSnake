import random
from typing import Dict

import SnAkePI as BattleAPI


class BattleSnakeHandlers:
    def __init__(self,
                 version: int,
                 author: str = "",
                 colour: str = "#888888",
                 head: str = "default",
                 tail: str = "default"
                 ):
        self.api_version = version
        self.author = author
        self.colour = colour
        self.head = head
        self.tail = tail

    def info(self) -> Dict:
        return {
            "apiversion": str(self.api_version),
            "author": self.author,
            "color": self.colour,
            "head": self.head,
            "tail": self.tail,
        }

    def start(self, state: Dict):
        print("Game START")

    def stop(self, state: Dict):
        print("Game STOPPED")

    def get_move(self, state: Dict) -> Dict:
        move = BattleAPI.create_move(random.choice(BattleAPI.AVAILABLE_MOVES))
        return move
