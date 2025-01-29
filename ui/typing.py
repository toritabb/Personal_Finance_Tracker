# 3rd party
from pygame import Rect

# local
from .vector import vec2



Number = int | float
Coordinate = vec2 | tuple[Number, Number]
RectValue = Rect | tuple[Number, Number, Number, Number] | tuple[Coordinate, Coordinate]

