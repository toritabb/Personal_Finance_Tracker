# standard library
from typing import Callable, Literal

# 3rd party
import pygame

pygame.key.set_repeat(500, 35) # makes holding a key work

# local
from .base import Canvas
from .button import TextButton
from .event import event_manager
from .misc import Pointer
from .text import FontDescriptor
from ._typing import Coordinate



__all__ = 'Textbox',



class Textbox(TextButton):
    __slots__ = 'text', '_validation_function'

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
            corner_radius: int = 0,
            align: Literal['left', 'center', 'right'] = 'left',
        ) -> None:

        super().__init__(parent, text.get(), font, pos, self._take_attention, size=size, padding=padding, border_thickness=border_thickness, corner_radius=corner_radius, align=align)

        self.text = text

        self._validation_function = validation_function

        event_manager.add_listener(pygame.TEXTINPUT, self._textinput, self.button._listener_group_id)
        event_manager.add_listener(pygame.KEYDOWN, self._keydown, self.button._listener_group_id)
        event_manager.add_listener(pygame.MOUSEMOTION, self._change_cursor, self.button._listener_group_id)

    def _change_cursor(self, _) -> None:
        if self.button.hovered:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)
        
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def _take_attention(self) -> None:
        self.button.pressed = True
        event_manager.mouse_attention = True

    def _revoke_attention(self) -> None:
        self.button.pressed = False
        event_manager.mouse_attention = False

    def _validate_and_update_text(self, text: str) -> None:
        if self._validation_function(text):
            self.text.set(text)

            self.text_object.update_text(text)

    def _textinput(self, event: pygame.Event) -> None:
        if self.button.pressed and event_manager.mouse_attention:
            self._validate_and_update_text(self.text.get() + event.text)

    def _keydown(self, event: pygame.Event) -> None:
        if self.button.pressed and event_manager.mouse_attention:
            match event.key:
                case pygame.K_BACKSPACE:
                    if self.text.get():
                        self._validate_and_update_text(self.text.get()[:-1])
                
                case pygame.K_ESCAPE:
                    self._revoke_attention()
                
                case pygame.K_RETURN:
                    self._revoke_attention()

                case pygame.K_v:
                    if event.mod & pygame.KMOD_CTRL:
                        self._validate_and_update_text(self.text.get() + pygame.scrap.get_text())

