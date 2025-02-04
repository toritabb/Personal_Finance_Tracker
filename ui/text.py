# standard library
from typing import Literal, Optional

# 3rd party
import pygame
from pygame import Rect, Surface

# local
from .base import Canvas, UIElement
from .fonts import FontDescriptor, get_font
from .theme import TEXT
from ._typing import Coordinate



__all__ = 'Text',



class Text(UIElement):
    __slots__ = 'font', 'multiplier', 'line_spacing', 'y_off', 'surface'

    def __init__(
            self,
            parent: Canvas,
            pos: Coordinate,
            text: str,
            font: FontDescriptor,
            *,
            size: Optional[Coordinate] = None,
            align: Literal['left', 'center', 'right'] = 'left',
            line_spacing: int = 0 # only matters for multi-line text
        ) -> None:

        font_object, base_height, _ = get_font(font)

        # all this shit to deal with multi-line text
        lines = text.split('\n')

        size = (
            max(font_object.get_rect(line).width for line in lines) if (size is None or size[0] == -1) else size[0],
            (base_height + line_spacing) * len(lines) - line_spacing + 1 if (size is None or size[1] == -1) else size[1]
        )

        super().__init__(parent, (pos, size))

        self.font = font
        self.multiplier = 1 if align == 'right' else 0.5 if align == 'center' else 0
        self.line_spacing = line_spacing
        self.y_off = int((self.height - ((base_height + self.line_spacing) * len(lines) - self.line_spacing + 1)) * 0.5)
        self.surface = Surface(self.size).convert_alpha()

        self.update_text(text)

    def update_text(self, text: str) -> None:
        # all this shit to deal with multi-line text
        font_object, base_height, top_pad = get_font(self.font)

        lines = text.split('\n')

        surfs: list[Surface] = []
        rects: list[Rect] = []

        for line in lines:
            text_surface, text_rect = font_object.render(line, TEXT)

            surfs.append(text_surface)
            rects.append(text_rect)

        self.surface.fill((0, 0, 0, 0))

        for i, (surf, rect) in enumerate(zip(surfs, rects)):
            pos = (
                int((self.w - rect.w) * self.multiplier),
                i * (base_height + self.line_spacing) - top_pad + self.y_off
            )

            self.surface.blit(surf, pos)

    def render(self, screen: Surface) -> None:
        screen.blit(self.surface, self, ((0, 0), self.size))

