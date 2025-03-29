# standard library
from typing import Callable, Literal, Optional

# 3rd party
import pygame

pygame.key.set_repeat(500, 35) # makes holding a key work

# local
from .base import Canvas
from .button import TextButton
from .event import Event, event_manager
from .misc import Pointer
from .text import FontDescriptor
from ._typing import Coordinate



__all__ = 'Textbox',



class Textbox(TextButton):
    __slots__ = 'text', 'multiline', '_validation_function'

    def __init__(
            self,
            parent: Canvas,
            text: Pointer[str],
            font: FontDescriptor,
            pos: Coordinate,
            size: Coordinate,
            *,
            validation_function: Callable[[str], Optional[str]] = lambda x: x,
            padding: float | Coordinate = 0,
            border_thickness: int = 4, 
            corner_radius: int = -1,
            align_x: Literal['left', 'center', 'right'] = 'left',
            align_y: Literal['top', 'center', 'bottom'] = 'center',
            multiline: bool = False,
            line_spacing: int = 5,
        ) -> None:

        super().__init__(parent, text.get(), font, pos, self._take_attention, size=size, padding=padding, border_thickness=border_thickness, corner_radius=corner_radius, align_x=align_x, align_y=align_y, line_spacing=line_spacing, cursor='i-beam')

        self.text = text

        self.multiline = multiline

        self._validation_function = validation_function

        event_manager.add_listener(pygame.TEXTINPUT, self._text_input, self.button._listener_group_id)
        event_manager.add_listener(pygame.KEYDOWN, self._key_down, self.button._listener_group_id)
        event_manager.add_listener(pygame.MOUSEBUTTONDOWN, self._click_outside, self.button._listener_group_id)

    def _take_attention(self) -> None:
        self.button.pressed = True
        event_manager.textbox_selected = self # type: ignore

    def _revoke_attention(self) -> None:
        self.button.pressed = False
        event_manager.textbox_selected = None

    def _click_outside(self, event: Event) -> None:
        if event_manager.textbox_selected is self:
            self._revoke_attention()

    def _validate_and_update_text(self, text: str) -> None:
        validation = self._validation_function(text)

        if validation is None:
            return

        elif validation is True:
            self.text.set(text)
        if isinstance(validation, str):
            self.text.set(validation)

            self.text_object.update_text(self.text.get())

        elif validation:

            self.text_object.update_text(self.text.get())

    def _add_str_to_text(self, str_to_add: str) -> None:
        self._validate_and_update_text(self.text.get() + str_to_add)

    def _text_input(self, event: pygame.Event) -> None:
        if event_manager.textbox_selected is self:
            self._add_str_to_text(event.text)

    def _key_down(self, event: pygame.Event) -> None:
        if event_manager.textbox_selected is self:
            match event.key:
                case pygame.K_BACKSPACE:
                    if self.text.get():
                        self._validate_and_update_text(self.text.get()[:-1])
                
                case pygame.K_ESCAPE:
                    self._revoke_attention()
                
                case pygame.K_RETURN if self.multiline:
                    self._add_str_to_text('\n')
                
                case pygame.K_RETURN:
                    self._revoke_attention()

                case pygame.K_v:
                    if event.mod & pygame.KMOD_CTRL:
                        self._validate_and_update_text(self.text.get() + pygame.scrap.get_text())

