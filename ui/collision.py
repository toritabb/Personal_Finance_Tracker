# standard library
from typing import Sequence, Union

# 3rd party
import pygame
from pygame import Color, Rect, Surface

# local
from .vector import vec2
from ._typing import Coordinate, RectValue



CollisionShape = Union[Rect, 'Circle']



class Circle:
    __slots__ = 'pos', 'rad', '_rad_squared'

    def __init__(self, pos: Coordinate, rad: int) -> None:
        self.pos = vec2(pos)
        self.rad = rad
        self._rad_squared = rad * rad

    def move_ip(self, dx: int, dy: int) -> None:
        self.pos += vec2(dx, dy)

    def collidepoint(self, point: Coordinate) -> bool:
        return self.pos.distance_squared_to(point) <= self._rad_squared

    def get_bounding_box(self) -> Rect:
        return Rect(self.pos - vec2(self.rad), vec2(self.rad + self.rad))



def get_rounded_collision_shapes(rect: RectValue, radius: int) -> tuple[CollisionShape, ...]:
    '''
    Gets the collision shapes for a rect with rounded corners.
    '''

    rect = Rect(rect)
    radius = min(radius, rect.w // 2, rect.h // 2)

    # rect
    if not radius:
        return rect.inflate(1, 1),

    # circle
    if radius * 2 == rect.w == rect.h:
        return Circle(rect.center, radius),

    # horizontal line with rounded ends
    elif radius * 2 == rect.h:
        return (
            rect.inflate(radius * -2, 1),
            Circle((rect.left + radius, rect.top + radius), radius),
            Circle((rect.right - radius, rect.top + radius), radius)
        )

    # vertical line with rounded ends
    elif radius * 2 == rect.w:
        return (
            rect.inflate(1, radius * -2),
            Circle((rect.left + radius, rect.top + radius), radius),
            Circle((rect.left + radius, rect.bottom - radius), radius)
        )

    # rectangle with rounded corners
    else:
        return (
            rect.inflate(radius * -2, 1),
            rect.inflate(1, radius * -2),
            Circle((rect.left + radius, rect.top + radius), radius),
            Circle((rect.right - radius, rect.top + radius), radius),
            Circle((rect.left + radius, rect.bottom - radius), radius),
            Circle((rect.right - radius, rect.bottom - radius), radius)
        )



def draw_shapes(
        surface: Surface,
        color: Color,
        shapes: Sequence[CollisionShape]
    ) -> None:

    '''
    Draws collision shapes.
    '''

    for shape in shapes:
        match shape:
            case Circle():
                pygame.draw.aacircle(surface, color, shape.pos, shape.rad)
            case Rect():
                pygame.draw.rect(surface, color, shape)

