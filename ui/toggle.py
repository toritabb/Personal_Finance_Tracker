# standard library
from typing import Literal, Optional, Any

# 3rd party
import pygame

# local
from . import collision
from .base import Canvas
from .button import Button
from .misc import Pointer
from .theme import COLOR_MAP
from ._typing import Coordinate



__all__ = 'Toggle',



class Toggle(Button):
    __slots__ = 'state'

    def __init__(
            self,
            parent: Canvas,
            pos: Coordinate,
            size: int,
            state: Pointer[bool],
            *,
            border_thickness: int = 0,
            corner_radius: int = 0,
            colors: Literal['toggle', 'toggle_accent'] = 'toggle'
        ) -> None:

        super().__init__(parent, pos, (size, size), lambda: state.set(not state.get()), border_thickness=border_thickness, corner_radius=corner_radius, colors=colors)

        self.state = state

    def render(self, screen: pygame.Surface) -> None:
        colors = COLOR_MAP[self.colors]

        base_color = colors['pressed'] if self.pressed else colors['hovered'] if self.hovered else colors['normal']
        border_color = colors['border_pressed'] if self.pressed else colors['border_hovered'] if self.hovered else colors['border_normal']
        fill_color = colors['fill_pressed'] if self.pressed else colors['fill_hovered'] if self.hovered else colors['fill_normal']

        if self._inner_shapes:
            collision.draw_shapes(screen, border_color, self.collision_shapes)

            collision.draw_shapes(screen, fill_color if self.state.get() else base_color, self._inner_shapes)

        else:
            collision.draw_shapes(screen, fill_color if self.state.get() else base_color, self.collision_shapes)

