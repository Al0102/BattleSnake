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
        move_safeties: Dict = BattleAPI.validate_move_safety(state)
        max_safety = max(move_safeties.values())

        move = "down"
        if max_safety <= BattleAPI.UNSAFE:
            return BattleAPI.create_move(move)

        available = []
        for direction, safety in move_safeties.items():
            if safety > BattleAPI.UNSAFE:
                available.append([direction, safety])

        available.sort(key=lambda x: x[1], reverse=True)
        moves = list(map(lambda x: x[0], available))

        move = BattleAPI.asearch(state, moves)
        if move is None:
            move = moves[0]

        print("Available: ", available)
        print("Moves: ", moves)
        print("Move: ", move)
        print("Safeties: ", move_safeties)
        move = BattleAPI.create_move(move)

        return move
