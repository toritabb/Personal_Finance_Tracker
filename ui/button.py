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
from .theme import theme
from .typing import Coordinate



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

        super().__init__(parent, collision.get_rounded_collision_shapes((pos, size), corner_radius))

        self.command = command

        self._inner_shapes = collision.get_rounded_collision_shapes(self.inflate(border_thickness * -2 - (corner_radius > border_thickness), border_thickness * -2 - (corner_radius > border_thickness)), max(0, corner_radius - border_thickness)) if border_thickness else None

        event_manager.add_listener(pygame.MOUSEBUTTONUP, self.activate, self._listener_group_id)

        self._add_listeners()

    def activate(self, event: Event) -> None:
        if self.pressed and self.hovered and event.button == pygame.BUTTON_LEFT:
            self.command()

    def render(self, screen: pygame.Surface) -> None:
        base_color = theme.button_base_pressed if self.pressed else theme.button_base_hovered if self.hovered else theme.button_base_normal

        if self._inner_shapes:
            border_color = theme.button_border_pressed if self.pressed else theme.button_border_hovered if self.hovered else theme.button_border_normal
            
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
            padding: int = 0,
            border_thickness: int = 0, 
            corner_radius: int = 0
        ) -> None:

        offset = padding + border_thickness + min(corner_radius // 5, 5)
        
        text_object = Text(parent, (int(pos[0] + offset), int(pos[1] + offset)), text, font)

        if size is None:
            text_size = text_object.text_surface.size
            offset2 = offset + offset - 1
            size = (text_size[0] + offset2, text_size[1] + offset2)

        super().__init__(parent, pos, size, command, border_thickness=border_thickness, corner_radius=corner_radius)

        self.text_object = text_object

    def render(self, screen: pygame.Surface) -> None:
        super().render(screen)

        self.text_object.render(screen)

    def close(self) -> None:
        self.text_object.close()

        super().close()


