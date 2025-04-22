import json
import re

from geom2d import Point
import importlib.resources # instead of pkg_resources that was deprecated in python 3.12

def read_config():
    ref = importlib.resources.files(__name__).joinpath('config.json')
    config = ref.read_bytes()
    return json.loads(config)

def parse_points():
    return (
        __point_from_string(input()),
        __point_from_string(input()),
        __point_from_string(input()),
    )


def __point_from_string(string: str):
    matches = re.match(r"(?P<x>\d+)\s(?P<y>\d+)", string)
    return Point(
        int(matches.group("x")),
        int(matches.group("y"))
    )