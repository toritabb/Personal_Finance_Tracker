# standard library
from typing import Callable, Literal, Optional, Any

# 3rd party
import pygame

pygame.key.set_repeat(500, 35)

# local
from .base import Canvas
from .button import TextButton
from .event import event_manager
from .misc import Pointer
from .text import Text, FontDescriptor
from .theme import TEXTBOX
from .typing import Coordinate



__all__ = 'Textbox',



class Textbox(TextButton):
    __slots__ = 'text', '_validation_function'

    colors = TEXTBOX

    def __init__(
            self,
            parent: Canvas,
            text: Pointer[str],
            font: FontDescriptor,
            pos: Coordinate,
            size: Coordinate,
            *,
            validation_function: Callable[[str], bool] = lambda _: True,
            padding: float | Coordinate = 0,
            border_thickness: int = 0, 
            corner_radius: int = 0
        ) -> None:

        super().__init__(parent, text.get(), font, pos, self._take_attention, size=size, padding=padding, border_thickness=border_thickness, corner_radius=corner_radius)

        self.text = text

        self._validation_function = validation_function

        event_manager.add_listener(pygame.TEXTINPUT, self._textinput, self._listener_group_id)
        event_manager.add_listener(pygame.KEYDOWN, self._keydown, self._listener_group_id)

    def _get_hovered(self, _) -> None:
        super()._get_hovered(None)

        if self.hovered:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)
        
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def _take_attention(self) -> None:
        self.pressed = True
        event_manager.mouse_attention = True

    def _revoke_attention(self) -> None:
        self.pressed = False
        event_manager.mouse_attention = False

    def _update_text(self, text: str) -> None:
        if self._validation_function(text):
            self.text.set(text)
                
            self.text_object.update(text)

    def _textinput(self, event: pygame.Event) -> None:
        self._update_text(self.text.get() + event.text)

    def _keydown(self, event: pygame.Event) -> None:
        match event.key:
            case pygame.K_BACKSPACE:
                if self.text.get():
                    self._update_text(self.text.get()[:-1])
            
            case pygame.K_ESCAPE:
                self._revoke_attention()
            
            case pygame.K_RETURN:
                self._revoke_attention()

            case pygame.K_v:
                if event.mod & pygame.KMOD_CTRL:
                    self._update_text(self.text.get() + pygame.scrap.get_text())

