import random
from typing import Dict, List

from math_helpers import distance_x, distance_y, distance

AVAILABLE_MOVES = ("up", "down", "left", "right")
UNSAFE = -1.0


def get_turn(state: Dict) -> int: return state["turn"]


def get_width(state: Dict) -> int: return state["board"]["width"]


def get_height(state: Dict) -> int: return state["board"]["height"]


def get_right_bound(state: Dict) -> int: return state["board"]["width"] - 1


def get_top_bound(state: Dict) -> int: return state["board"]["height"] - 1


def get_head(state: Dict) -> Dict: return state["you"]["head"]


def get_tail(state: Dict) -> List: return state["you"]["body"][1::]


def get_neck(state: Dict) -> Dict: return get_tail(state)[0]


def get_all_parts(state: Dict) -> List:
    parts = []
    for snake in state["board"]["snakes"]:
        parts += snake["body"]
    parts += state["board"]["hazards"]
    return parts

def get_foods(state: Dict) -> List:
    return state["board"]["food"]

def create_move(move: str):
    return {"move": move}


def create_safety_check():
    return {move: 0.0 for move in AVAILABLE_MOVES}


def validate_move_safety(state: Dict) -> Dict:
    safety = validate_backwards_move(state)
    validate_bounds(state, safety)
    validate_collision(state, safety)
    print(get_turn(state), safety)
    return safety

def asearch(state: Dict, safety: List) -> str | None:
    foods = get_foods(state)

    sort_foods = list(map(
        lambda x: distance(x, get_head(state)),
        foods
    ))
    closest = foods[sort_foods.index(min(sort_foods))]

    head = get_head(state)
    head_x = get_head(state)["x"]
    head_y = get_head(state)["y"]

    dx = distance_x(head, closest)
    dy = distance_y(head, closest)
    if dx < dy:
        if closest["x"] > head_x and "right" in safety:
            return "right"
        if closest["x"] < head_x and "left" in safety:
            return "left"
    else:
        if closest["y"] > head_y and "up" in safety:
            return "up"
        if closest["y"] < head_y and "down" in safety:
            return "down"
    return None



def validate_backwards_move(state: Dict, safety: Dict | None = None) -> Dict:
    if safety is None: safety = create_safety_check()

    if get_neck(state)["x"] < get_head(state)["x"]:
        safety["left"] += UNSAFE
    elif get_neck(state)["x"] > get_head(state)["x"]:
        safety["right"] += UNSAFE
    elif get_neck(state)["y"] < get_head(state)["y"]:
        safety["down"] += UNSAFE
    elif get_neck(state)["y"] > get_head(state)["y"]:
        safety["up"] += UNSAFE
    return safety


def validate_collision(state: Dict, safety: Dict | None = None) -> Dict:
    if safety is None: safety = create_safety_check()

    all_bodies = get_all_parts(state)
    head_x = get_head(state)["x"]
    head_y = get_head(state)["y"]

    for body in all_bodies:
        part_x = body["x"]
        part_y = body["y"]
        if (head_x - 1, head_y) == (part_x, part_y):
            safety["left"] += UNSAFE
        elif (head_x + 1, head_y) == (part_x, part_y):
            safety["right"] += UNSAFE

        if (head_x, head_y - 1) == (part_x, part_y):
            safety["down"] += UNSAFE
        elif (head_x, head_y + 1) == (part_x, part_y):
            safety["up"] += UNSAFE
    return safety


def validate_bounds(state: Dict, safety: Dict | None = None) -> Dict:
    if safety is None: safety = create_safety_check()
    head_x = get_head(state)["x"]
    head_y = get_head(state)["y"]

    safety["left"] = distance_x_score(state, head_x)
    safety["right"] = distance_x_score(state, get_right_bound(state) - head_x)
    safety["down"] = distance_y_score(state, head_y)
    safety["up"] = distance_x_score(state, get_top_bound(state) - head_y)
    return safety


def shuffle(safety: Dict) -> Dict:
    for k, value in safety:
        safety[k] *= random.random()
    return safety


def distance_x_score(state: Dict, dis: int) -> float:
    return UNSAFE * ((get_width(state) - dis) / get_width(state))


def distance_y_score(state: Dict, dis: int) -> float:
    return UNSAFE * ((get_height(state) - dis) / get_height(state))

if __name__ == "__main__":
    data = {
        "game": {
            "id": "totally-unique-game-id",
            "ruleset": {
                "name": "standard",
                "version": "v1.1.15",
                "settings": {
                    "foodSpawnChance": 15,
                    "minimumFood": 1,
                    "hazardDamagePerTurn": 14
                }
            },
            "map": "standard",
            "source": "league",
            "timeout": 500
        },
        "turn": 14,
        "board": {
            "height": 11,
            "width": 11,
            "food": [
                {"x": 5, "y": 5},
                {"x": 9, "y": 0},
                {"x": 2, "y": 6}
            ],
            "hazards": [
                {"x": 3, "y": 2}
            ],
            "snakes": [
                {
                    "id": "snake-508e96ac-94ad-11ea-bb37",
                    "name": "My Snake",
                    "health": 54,
                    "body": [
                        {"x": 0, "y": 0},
                        {"x": 1, "y": 0},
                        {"x": 2, "y": 0}
                    ],
                    "latency": "111",
                    "head": {"x": 0, "y": 0},
                    "length": 3,
                    "shout": "why are we shouting??",
                    "customizations": {
                        "color": "#FF0000",
                        "head": "pixel",
                        "tail": "pixel"
                    }
                },
                {
                    "id": "snake-b67f4906-94ae-11ea-bb37",
                    "name": "Another Snake",
                    "health": 16,
                    "body": [
                        {"x": 5, "y": 4},
                        {"x": 5, "y": 3},
                        {"x": 6, "y": 3},
                        {"x": 6, "y": 2}
                    ],
                    "latency": "222",
                    "head": {"x": 5, "y": 4},
                    "length": 4,
                    "shout": "I'm not really sure...",
                    "customizations": {
                        "color": "#26CF04",
                        "head": "silly",
                        "tail": "curled"
                    }
                }
            ]
        },
        "you": {
            "id": "snake-508e96ac-94ad-11ea-bb37",
            "name": "My Snake",
            "health": 54,
            "body": [
                {"x": 0, "y": 0},
                {"x": 1, "y": 0},
                {"x": 2, "y": 0}
            ],
            "latency": "111",
            "head": {"x": 0, "y": 0},
            "length": 3,
            "shout": "why are we shouting??",
            "customizations": {
                "color": "#FF0000",
                "head": "pixel",
                "tail": "pixel"
            }
        }
    }
    # print(create_safety_check())
    print(get_all_parts(data))
