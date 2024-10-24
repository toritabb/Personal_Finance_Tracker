import importlib.util as importlib

from .typing import ColorValue
from path import get_global_path



class Theme:
    background: ColorValue

    button_base_normal: ColorValue
    button_base_hovered: ColorValue
    button_base_pressed: ColorValue

    button_border_normal: ColorValue
    button_border_hovered: ColorValue
    button_border_pressed: ColorValue

    text: ColorValue

    @classmethod
    def from_file(cls, filename: str) -> 'Theme':
        spec = importlib.spec_from_file_location('theme', get_global_path(f'ui/themes/{filename}.py'))

        if spec is None or spec.loader is None:
            raise FileNotFoundError(f'Error reading theme file {filename}. File not found.')
        
        module = importlib.module_from_spec(spec)

        spec.loader.exec_module(module)

        theme = cls.__new__(cls)

        theme.background = module.BACKGROUND

        theme.button_base_normal = module.BUTTON['normal']
        theme.button_base_hovered = module.BUTTON['hovered']
        theme.button_base_pressed = module.BUTTON['pressed']

        theme.button_border_normal = module.BUTTON_BORDER['normal']
        theme.button_border_hovered = module.BUTTON_BORDER['hovered']
        theme.button_border_pressed = module.BUTTON_BORDER['pressed']

        theme.text = module.TEXT

        return theme



theme = Theme.from_file('ocean')


def set_theme(theme: str) -> None:
    pass

