# standard library
from typing import Callable, Optional, Any

# 3rd party
import pygame
from pygame import Event

# local
from . import collision
from .base import Canvas, Interactable
from .text import Text, FontDescriptor
from .theme import BUTTON
<<<<<<< HEAD
=======
from ._typing import Coordinate
>>>>>>> 293e10240456ca6547c46b9e4c2b81fd2a924461
from .vector import vec2
from ._typing import Coordinate



__all__ = 'Button', 'TextButton'



class Button(Interactable):
    __slots__ = 'command', '_accent', '_inner_shapes'

    colors = BUTTON

    def __init__(
            self,
            parent: Canvas,
            pos: Coordinate,
            size: Coordinate,
            command: Callable[..., Any],
            *,
            border_thickness: int = 0,
            corner_radius: int = 0,
            use_accent_colors: bool = False
        ) -> None:

        if corner_radius == -1:
            corner_radius = int(min(*size) // 2 + 1)

        super().__init__(parent, collision.get_rounded_collision_shapes((pos, size), corner_radius))

        self.command = command

        self._accent = use_accent_colors

        self._inner_shapes = collision.get_rounded_collision_shapes(self.inflate(vec2(border_thickness * -2 - (corner_radius > border_thickness) - (corner_radius == 0))), max(0, corner_radius - border_thickness)) if border_thickness else None

    def _get_unpressed(self, event: Event) -> None:
        if super()._get_unpressed(event) and self.hovered:
            self.command()

    def render(self, screen: pygame.Surface) -> None:
        if self._accent:
            base_color = self.colors['accent_pressed'] if self.pressed else self.colors['accent_hovered'] if self.hovered else self.colors['accent_normal']
            border_color = self.colors['accent_border_pressed'] if self.pressed else self.colors['accent_border_hovered'] if self.hovered else self.colors['accent_border_normal']

        else:
            base_color = self.colors['pressed'] if self.pressed else self.colors['hovered'] if self.hovered else self.colors['normal']
            border_color = self.colors['border_pressed'] if self.pressed else self.colors['border_hovered'] if self.hovered else self.colors['border_normal']

        if self._inner_shapes and base_color != border_color:
            collision.draw_shapes(screen, border_color, self.collision_shapes)
            collision.draw_shapes(screen, base_color, self._inner_shapes)

        else:
            collision.draw_shapes(screen, base_color, self.collision_shapes)



class TextButton(Button):
    __slots__ = 'text_object', '_topleft', '_font'

    def __init__(
            self,
            parent: Canvas,
            text: str,
            font: FontDescriptor,
            pos: Coordinate,
            command: Callable[..., Any] = lambda: None,
            *,
            size: Optional[Coordinate] = None,
            padding: float | Coordinate = 4,
            border_thickness: int = 0, 
            corner_radius: int = -1,
            use_accent_colors: bool = False
        ) -> None:

        offset = vec2(padding) + vec2(border_thickness) + vec2(max(0, min(corner_radius // 5, 5)))

        topleft = (pos + offset) // 1

        text_object = Text(parent, topleft, text, font)

        text_size = text_object.text_surface.size
        offset2 = offset + offset - vec2(1)
        new_size = (text_size[0] + offset2[0] if (size is None or size[0] == -1) else size[0], text_size[1] + offset2[1] - 3 if (size is None or size[1] == -1) else size[1])

        super().__init__(parent, pos, new_size, command, border_thickness=border_thickness, corner_radius=corner_radius, use_accent_colors=use_accent_colors)

        self.text_object = text_object

        self._topleft = topleft
        self._font = font

    def update_text(self, text: str) -> None:
        self.text_object.close()

        self.text_object = Text(
            self.parent,  # type: ignore
            self._topleft,
            text,
            self._font
        )

    def render(self, screen: pygame.Surface) -> None:
        super().render(screen)

        self.text_object.render(screen)

    def close(self) -> None:
        self.text_object.close()

        super().close()

