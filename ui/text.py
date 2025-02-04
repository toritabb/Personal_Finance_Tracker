# standard library
from math import inf
from typing import Literal, Optional

# 3rd party
from pygame import Rect, Surface

# local
from .base import Canvas, UIElement
from .fonts import FontDescriptor, get_font
from .theme import TEXT
from ._typing import Coordinate



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
            align: Literal['left', 'center', 'right'] = 'center', # only matters for multi-line text
            line_spacing: int = 0                                 # only matters for multi-line text
        ) -> None:

        font_object, base_height, top_pad = get_font(font)

        # all this shit to deal with multi-line text
        lines = text.split('\n')

        surfs: list[Surface] = []
        rects: list[Rect] = []

        for line in lines:
            text_surface, text_rect = font_object.render(line, TEXT)

            surfs.append(text_surface.convert_alpha())
            rects.append(text_rect)

        w = max(r.w for r in rects)
        h = (base_height + line_spacing) * len(rects) - line_spacing + 1

        surface = Surface((w, h)).convert_alpha()
        surface.fill((0, 0, 0, 0))

        divisor = 1 if align == 'right' else 2 if align == 'center' else inf

        for i, (surf, rect) in enumerate(zip(surfs, rects)):
            x = (w - rect.w) // divisor

            surface.blit(surf, (x, i * (base_height + line_spacing) - top_pad))

        new_size = (
            surface.width if (size is None or size[0] == -1) else size[0],
            surface.height if (size is None or size[1] == -1) else size[1]
        )

        super().__init__(parent, (pos, new_size))

        self.font = font_object

        self.text_surface = surface

    def render(self, screen: Surface) -> None:
        screen.blit(self.text_surface, self)

