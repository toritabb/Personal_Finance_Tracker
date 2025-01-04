# standard library
from typing import Literal, Optional, Any

# 3rd party
import pygame

# local
from . import draw
from .base import Canvas, Interactable
from .button import Button
from .misc import Pointer
from .text import Text, FontDescriptor
from .themes import theme
from .typing import Coordinate



__all__ = 'Textbox',



class Textbox(Interactable):
    __slots__ = 'text_pointer', 'font'

    def __init__(
            self,
            parent: Canvas,
            text: Pointer[str],
            font: FontDescriptor,
            pos: Coordinate,
            size: Coordinate,
            *,
            padding: int = 0,
            border_thickness: int = 0, 
            corner_radius: int = 0
        ) -> None:

        super().__init__(parent, (self,), self)
        
        offset = padding + border_thickness + min(corner_radius // 5, 5)
        self.text_pos = (self.top + offset, self.left + offset)

        self.text_pointer = text
        self.font = font

        self.update_text()

    def render(self, screen: pygame.Surface) -> None:
        base_color = theme.toggle_pressed if self.pressed else theme.toggle_hovered if self.hovered else theme.toggle

        draw.collision_shapes(screen, base_color, self.collision_shapes)

    def update_text(self) -> None:
        self.text_object = Text(self.parent, self.text_pos, self.text_pointer.get(), self.font) # type: ignore

    def _render_checkbox(self, surface: pygame.Surface) -> None: ...
    def _render_circle(self, surface: pygame.Surface) -> None: ...
    def _render_switch(self, surface: pygame.Surface) -> None: ...

