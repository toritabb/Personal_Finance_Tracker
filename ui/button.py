# standard library
from typing import Callable, Optional, Any

# 3rd party
import pygame
from pygame import Event

# local
from . import collision, draw
from .base import Canvas, Interactable
from .event import event_manager
from .text import Text, FontDescriptor
from .themes import theme
from .typing import Coordinate
from .vector import vec2



__all__ = 'Button', 'TextButton'



class Button(Interactable):
    __slots__ = 'command', '_inner_shapes'

    def __init__(
            self,
            parent: Canvas,
            pos: Coordinate,
            size: Coordinate,
            command: Callable[..., Any],
            *,
            border_thickness: int = 0,
            corner_radius: int = 0
        ) -> None:

        if corner_radius == -1:
            corner_radius = int(min(*size) // 2 + 1)

        super().__init__(parent, collision.get_rounded_collision_shapes((pos, size), corner_radius))

        self.command = command

        self._inner_shapes = collision.get_rounded_collision_shapes(self.inflate(border_thickness * -2 - (corner_radius > border_thickness), border_thickness * -2 - (corner_radius > border_thickness)), max(0, corner_radius - border_thickness)) if border_thickness else None

        event_manager.add_listener(pygame.MOUSEBUTTONUP, self.activate, self._listener_group_id)

        self._add_listeners()

    def activate(self, event: Event) -> None:
        if self.pressed and self.hovered and event.button == pygame.BUTTON_LEFT:
            self.command()

    def render(self, screen: pygame.Surface) -> None:
        base_color = theme.button_pressed if self.pressed else theme.button_hovered if self.hovered else theme.button
        border_color = theme.button_border_pressed if self.pressed else theme.button_border_hovered if self.hovered else theme.button_border

        if self._inner_shapes:
            draw.collision_shapes(screen, border_color, self.collision_shapes)
            draw.collision_shapes(screen, base_color, self._inner_shapes)

        else:
            draw.collision_shapes(screen, base_color, self.collision_shapes)



class TextButton(Button):
    __slots__ = 'text_object'

    def __init__(
            self,
            parent: Canvas,
            text: str,
            font: FontDescriptor,
            pos: Coordinate,
            size: Optional[Coordinate],
            command: Callable[..., Any],
            *,
            padding: float | Coordinate = 0,
            border_thickness: int = 0, 
            corner_radius: int = 0
        ) -> None:

        offset = vec2(padding) + vec2(border_thickness) + vec2(max(0, min(corner_radius // 5, 5)))
        print(text, offset)

        text_object = Text(parent, (pos + offset) // 1, text, font)

        if size is None:
            text_size = text_object.text_surface.size
            offset2 = offset + offset - vec2(1)
            size = text_size + offset2

        super().__init__(parent, pos, size, command, border_thickness=border_thickness, corner_radius=corner_radius)

        self.text_object = text_object

    def render(self, screen: pygame.Surface) -> None:
        super().render(screen)

        self.text_object.render(screen)

    def close(self) -> None:
        self.text_object.close()

        super().close()

