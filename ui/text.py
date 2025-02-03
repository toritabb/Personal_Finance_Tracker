# standard library
from math import inf
from typing import Literal, Optional

# 3rd party
from pygame import Rect, Surface

# local
from .base import Canvas, UIElement
from .fonts import FontDescriptor, get_font
from .theme import TEXT
from .typing import Coordinate



__all__ = 'Text',



class Text(UIElement):
    __slots__ = 'font', 'text_surface'

    def __init__(
            self,
            parent: Canvas,
            pos: Coordinate,
            text: str,
            font: FontDescriptor,
            *,
            size: Optional[Coordinate] = None,
            align: Literal['left', 'center', 'right'] = 'center' # only matters for multi-line text
        ) -> None:

        font_object = get_font(font)
        
        # all this shit to deal with multi-line text
        lines = text.split('\n')

        surfs: list[Surface] = []
        rects: list[Rect] = []

        for line in lines:
            text_surface, text_rect = font_object.render(line, TEXT)

            surfs.append(text_surface)
            rects.append(text_rect)

        w = max(r.w for r in rects)
        h = sum(r.h for r in rects) + 2 * (len(rects) - 1)

        surface = Surface((w, h)).convert_alpha()
        surface.fill((0, 0, 0, 0))

        divisor = 1 if align == 'right' else 2 if align == 'center' else inf

        y = 0

        for surf, rect in zip(surfs, rects):
            x = (w - rect.w) // divisor

            surface.blit(surf, (x, y))

            y += rect.h + 2

        new_size = (
            surface.width if (size is None or size[0] == -1) else size[0],
            surface.height if (size is None or size[1] == -1) else size[1]
        )

        super().__init__(parent, (pos, new_size))

        self.font = font_object

        self.text_surface = surface.convert_alpha()

    def render(self, screen: Surface) -> None:
        screen.blit(self.text_surface, self)

    def update(self, text: str) -> None:
        text_surface, _ = self.font.render(text, TEXT)

        self.text_surface = text_surface.convert_alpha()

