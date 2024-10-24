# standard library
from typing import Sequence

# 3rd party
import pygame

# local
from .collision import Circle, Rect, get_rounded_collision_shapes, CollisionShape
from .typing import ColorValue, RectValue



def collision_shape(
        surface: pygame.Surface,
        color: ColorValue,
        shape: CollisionShape
    ) -> None:

    '''
    Draws a collision shape.
    '''

    match shape:
        case Circle():
            pygame.draw.aacircle(surface, color, shape.pos, shape.rad)
        case Rect():
            pygame.draw.rect(surface, color, shape)



def collision_shapes(
        surface: pygame.Surface,
        color: ColorValue,
        shapes: Sequence[CollisionShape]
    ) -> None:

    '''
    Draws multiple collision shapes.
    '''

    for shape in shapes:
        collision_shape(surface, color, shape)



def rounded_rect(
        surface: pygame.Surface,
        color: ColorValue,
        rect: RectValue,
        radius: int
    ) -> None:

    '''
    Draws a rectangle with antialiased rounded corners.

    If `radius` is 0, draws a normal rectangle.
    '''
    
    shapes = get_rounded_collision_shapes(rect, radius)

    collision_shapes(surface, color, shapes)

