from typing import Dict, List

AVAILABLE_MOVES = ("up", "down", "left", "right")
UNSAFE = -1.0

def get_right_bound(state: Dict) -> int: return state["width"] - 1
def get_top_bound(state: Dict) -> int: return state["height"] - 1

def get_head(state: Dict) -> Dict: return state["you"]["head"]
def get_tail(state: Dict) -> List: return state["you"]["body"][1::]
def get_neck(state: Dict) -> Dict: return get_tail(state)[0]

def create_move(move: str):
    return {"move": move}

def create_safety_check():
    return {move: 0.0 for move in AVAILABLE_MOVES}

def validate_move_safety(state: Dict) -> Dict:
    safety = validate_backwards_move(state)
    validate_bounds(state, safety)
    return safety

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

def validate_bounds(state: Dict, safety: Dict | None = None) -> Dict:
    if safety is None: safety = create_safety_check()

    if get_head(state)["x"] == 0:
        safety["left"] += UNSAFE
    elif get_head(state)["x"] == get_right_bound(state):
        safety["right"] += UNSAFE
    elif get_head(state)["y"] == 0:
        safety["down"] += UNSAFE
    elif get_head(state)["y"] == get_top_bound(state):
        safety["up"] += UNSAFE

    return safety


