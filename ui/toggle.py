# standard library
from typing import Literal, Optional, Any

# 3rd party
import pygame

# local
from . import collision
from .base import Canvas
from .button import Button
from .misc import Pointer
from .theme import TOGGLE
from .typing import Coordinate



__all__ = 'Toggle',



class Toggle(Button):
    __slots__ = 'state'

    colors = TOGGLE

    def __init__(
            self,
            parent: Canvas,
            pos: Coordinate,
            size: int,
            state: Pointer[bool],
            *,
            border_thickness: int = 0,
            corner_radius: int = 0
        ) -> None:

        super().__init__(parent, pos, (size, size), lambda: state.set(not state.get()), border_thickness=border_thickness, corner_radius=corner_radius)

        self.state = state

    def render(self, screen: pygame.Surface) -> None:
        base_color = self.colors['pressed'] if self.pressed else self.colors['hovered'] if self.hovered else self.colors['normal']
        border_color = self.colors['border_pressed'] if self.pressed else self.colors['border_hovered'] if self.hovered else self.colors['border_normal']
        fill_color = self.colors['fill_pressed'] if self.pressed else self.colors['fill_hovered'] if self.hovered else self.colors['fill_normal']

        if self._inner_shapes:
            collision.draw_shapes(screen, border_color, self.collision_shapes)

            collision.draw_shapes(screen, fill_color if self.state.get() else base_color, self._inner_shapes)

        else:
            collision.draw_shapes(screen, fill_color if self.state.get() else base_color, self.collision_shapes)

