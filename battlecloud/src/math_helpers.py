from typing import Dict


def distance_x(a: Dict, b: Dict):
    return abs(a["x"] - b["x"])


def distance_y(a: Dict, b: Dict):
    return abs(a["y"] - b["y"])


def distance(a: Dict, b: Dict):
    return distance_x(a, b) + distance_y(a, b)

