# 3rd party
from pygame import Color

# local
from ._color_funcs import *



__all__ = 'Color', 'BACKGROUND', 'HEADER', 'TEXT'



# base colors
# MOSS = Color(96, 108, 56)
# FERN = Color(68, 81, 40)
# BAMBOO = Color(40, 54, 24)
MOSS = Color(131, 148, 76)
FERN = Color(117, 136, 68)
BAMBOO = Color(103, 123, 61)
DARK_MOSS = Color(54, 68, 32)

CREAM = Color(244, 228, 192)
OLD_PAPER = Color(240, 212, 168)
DESERT_TAN = Color(234, 195, 143)

CHARCOAL = Color(14, 18, 23)



# element colors
BACKGROUND = CREAM
HEADER = OLD_PAPER

TEXT = CHARCOAL

BUTTON = {
    'normal': CREAM,
    'hovered': OLD_PAPER,
    'pressed': DESERT_TAN,
    'border_normal': blend(OLD_PAPER, DESERT_TAN, 0.5),
    'border_hovered': DESERT_TAN,
    'border_pressed': DESERT_TAN,
}

BUTTON_ACCENT = {
    'normal': MOSS,
    'hovered': FERN,
    'pressed': BAMBOO,
    'border_normal': blend(FERN, BAMBOO, 0.5),
    'border_hovered': BAMBOO,
    'border_pressed': BAMBOO,
}

TOGGLE = {
    'normal': CREAM,
    'hovered': OLD_PAPER,
    'pressed': DESERT_TAN,
    'border_normal': blend(OLD_PAPER, DESERT_TAN, 0.5),
    'border_hovered': DESERT_TAN,
    'border_pressed': DESERT_TAN,
    'fill_normal':  blend(FERN, BAMBOO, 0.5),
    'fill_hovered': blend(FERN, BAMBOO, 0.5),
    'fill_pressed': BAMBOO,
}

TOGGLE_ACCENT = {
    'normal': CREAM,
    'hovered': OLD_PAPER,
    'pressed': DESERT_TAN,
    'border_normal': blend(OLD_PAPER, DESERT_TAN, 0.5),
    'border_hovered': DESERT_TAN,
    'border_pressed': DESERT_TAN,
    'fill_normal':  blend(FERN, BAMBOO, 0.5),
    'fill_hovered': blend(FERN, BAMBOO, 0.5),
    'fill_pressed': BAMBOO,
}

COLOR_MAP = {
    'button': BUTTON,
    'button_accent': BUTTON_ACCENT,
    'toggle': TOGGLE,
    'toggle_accent': TOGGLE_ACCENT,
    # 'textbox': TEXTBOX,
}

