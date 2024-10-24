# standard library
from typing import Optional

# 3rd party
import pygame

# local
from .base import Canvas, UIElement
from .fonts import FontDescriptor, get_font
from .theme import theme
from .typing import Coordinate



__all__ = 'Text',



class Text(UIElement):
    __slots__ = 'text_surface'

    def __init__(
            self,
            parent: Canvas,
            pos: Coordinate,
            text: str,
            font: FontDescriptor,
            *,
            size: Optional[Coordinate] = None,
        ) -> None:

        text_surface, _ = get_font(font).render(text, theme.text)

        size = text_surface.size if size is None else size

        super().__init__(parent, (pos, size))

        self.text_surface = text_surface.convert_alpha()

    def render(self, screen: pygame.Surface) -> None:
        screen.blit(self.text_surface, self)

