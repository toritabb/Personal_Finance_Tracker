# standard library
from typing import Callable, Literal, Optional, Any

# 3rd party
import pygame
from pygame import Event, Surface

# local
from . import collision
from .base import Canvas, Interactable
from .event import Event, event_manager
from .text import Text, FontDescriptor
from .theme import COLOR_MAP
from .vector import vec2
from ._typing import Coordinate



__all__ = 'Button', 'TextButton'



class Button(Interactable):
    __slots__ = 'command', 'colors', '_inner_shapes'

    def __init__(
            self,
            parent: Canvas,
            pos: Coordinate,
            size: Coordinate,
            command: Callable[..., Any],
            *,
            border_thickness: int = 0,
            corner_radius: int = 0,
            colors: Literal['button', 'button_accent', 'toggle', 'toggle_accent'] = 'button',
            cursor: Literal['pointer', 'hand', 'i-beam'] = 'hand'
        ) -> None:

        if corner_radius == -1:
            corner_radius = int(min(*size) // 2 + 1)

        super().__init__(parent, collision.get_rounded_collision_shapes((pos, size), corner_radius), cursor=cursor)

        self.command = command

        self.colors = COLOR_MAP[colors]

        self._inner_shapes = collision.get_rounded_collision_shapes(self.inflate(vec2(border_thickness * -2 - (corner_radius > border_thickness) - (corner_radius == 0))), max(0, corner_radius - border_thickness)) if border_thickness else []

    def _get_unpressed(self, event: Event) -> None:
        if super()._get_unpressed(event) and self._mouse_collides():
            self.command()

    def move_offset(self, dx: int, dy: int) -> None:
        super().move_offset(dx, dy)

        if self._inner_shapes:
            for shape in self._inner_shapes:
                shape.move_ip(dx, dy)

    def set_command(self, new_command: Callable[..., Any]) -> None:
        self.command = new_command

    def render(self, screen: Surface) -> None:
        base_color = self.colors['pressed'] if self.pressed else self.colors['hovered'] if self.hovered else self.colors['normal']
        border_color = self.colors['border_pressed'] if self.pressed else self.colors['border_hovered'] if self.hovered else self.colors['border_normal']

        if self._inner_shapes and base_color != border_color:
            collision.draw_shapes(screen, border_color, self.collision_shapes)
            collision.draw_shapes(screen, base_color, self._inner_shapes)

        else:
            collision.draw_shapes(screen, base_color, self.collision_shapes)



class TextButton(Canvas):
    __slots__ = 'text_object', 'button'

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
            border_thickness: int = 4,
            corner_radius: int = -1,
            align_x: Literal['left', 'center', 'right'] = 'center',
            align_y: Literal['top', 'center', 'bottom'] = 'center',
            line_spacing: int = 0,
            colors: Literal['button', 'button_accent'] = 'button',
            cursor: Literal['pointer', 'hand', 'i-beam'] = 'hand'
        ) -> None:

        super().__init__(parent, (pos, (100, 100)))

        offset = vec2(padding) + vec2(border_thickness) + vec2(max(0, min(corner_radius // 5, 5)))
        padding = offset * 2

        self.text_object = Text(
            self,
            offset,
            text,
            font,
            size=None if size is None else (-1 if size[0] == -1 else size[0] - padding[0], -1 if size[1] == -1 else size[1] - padding[1]),
            align_x=align_x,
            align_y=align_y,
            line_spacing=line_spacing
        )

        text_size = self.text_object.size
        button_size = (text_size[0] + padding[0] - 1 if (size is None or size[0] == -1) else size[0], text_size[1] + padding[1] - 3 if (size is None or size[1] == -1) else size[1])

        self.button = Button(
            self,
            (0, 0),
            button_size,
            command,
            border_thickness=border_thickness,
            corner_radius=corner_radius,
            colors=colors,
            cursor=cursor
        )

        self.size = button_size + vec2(1)
        self.surface = Surface(button_size + vec2(1))

    def set_command(self, new_command: Callable[..., Any]) -> None:
        self.button.set_command(new_command)

    def render(self, surface: Surface) -> None:
        self.surface.fill(self.parent.fill_color)

        self.button.render(self.surface)
        self.text_object.render(self.surface)

        surface.blit(self.surface, self)

