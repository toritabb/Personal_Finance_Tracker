# standard library
from typing import Literal, Optional, Any

# 3rd party
import pygame

# local
from . import draw
from .base import Canvas
from .button import Button
from .misc import Pointer
from .themes import theme
from .typing import Coordinate



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
            corner_radius: int = 0
        ) -> None:

        super().__init__(parent, pos, (size, size), lambda: state.set(not state.get()), border_thickness=border_thickness, corner_radius=corner_radius)

        self.state = state

    def render(self, screen: pygame.Surface) -> None:
        base_color = theme.toggle_pressed if self.pressed else theme.toggle_hovered if self.hovered else theme.toggle

        draw.collision_shapes(screen, base_color, self.collision_shapes)

        if self._inner_shapes and self.state.get():
            fill_color = theme.toggle_fill_pressed if self.pressed else theme.toggle_fill_hovered if self.hovered else theme.toggle_fill

            draw.collision_shapes(screen, fill_color, self._inner_shapes)

    def _render_checkbox(self, surface: pygame.Surface) -> None: ...
    def _render_circle(self, surface: pygame.Surface) -> None: ...
    def _render_switch(self, surface: pygame.Surface) -> None: ...

