import importlib.util as importlib

from pygame import Color
from path import get_global_path



class Theme:
    background: Color

    text: Color

    button: Color
    button_hovered: Color
    button_pressed: Color
    button_border: Color
    button_border_hovered: Color
    button_border_pressed: Color

    toggle: Color
    toggle_hovered: Color
    toggle_pressed: Color
    toggle_fill: Color
    toggle_fill_hovered: Color
    toggle_fill_pressed: Color

    textbox: Color
    textbox_hovered: Color
    textbox_pressed: Color
    textbox_fill: Color
    textbox_fill_hovered: Color
    textbox_fill_pressed: Color

    @classmethod
    def from_file(cls, filename: str) -> 'Theme':
        spec = importlib.spec_from_file_location('theme', get_global_path(f'ui/themes/{filename}.py'))

        if spec is None or spec.loader is None:
            raise FileNotFoundError(f'Error reading theme file {filename}. File not found.')
        
        module = importlib.module_from_spec(spec)

        spec.loader.exec_module(module)

        theme = cls.__new__(cls)

        theme.background = module.BACKGROUND

        theme.text = module.TEXT

        theme.button = module.BUTTON
        theme.button_hovered = module.BUTTON_HOVERED
        theme.button_pressed = module.BUTTON_PRESSED
        theme.button_border = module.BUTTON_BORDER
        theme.button_border_hovered = module.BUTTON_BORDER_HOVERED
        theme.button_border_pressed = module.BUTTON_BORDER_PRESSED

        theme.toggle = module.TOGGLE
        theme.toggle_hovered = module.TOGGLE_HOVERED
        theme.toggle_pressed = module.TOGGLE_PRESSED
        theme.toggle_fill = module.TOGGLE_FILL
        theme.toggle_fill_hovered = module.TOGGLE_FILL_HOVERED
        theme.toggle_fill_pressed = module.TOGGLE_FILL_PRESSED

        theme.textbox = module.TEXTBOX
        theme.textbox_hovered = module.TEXTBOX_HOVERED
        theme.textbox_pressed = module.TEXTBOX_PRESSED
        theme.textbox_fill = module.TEXTBOX_FILL
        theme.textbox_fill_hovered = module.TEXTBOX_FILL_HOVERED
        theme.textbox_fill_pressed = module.TEXTBOX_FILL_PRESSED

        return theme



theme = Theme.from_file('forest')

