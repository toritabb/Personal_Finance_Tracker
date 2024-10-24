# 3rd party
from pygame import Rect

# local
from .vector import vec2


ColorValue = int | str | tuple[int, int, int]


Coordinate = vec2 | tuple[int, int]
RectValue = Rect | tuple[int, int, int, int] | tuple[Coordinate, Coordinate]

