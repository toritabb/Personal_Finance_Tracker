# 3rd party
from pygame import Color

# local
from ._color_funcs import *



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

TEXT = CHARCOAL

BUTTON = {
    'normal': CREAM,
    'hovered': OLD_PAPER,
    'pressed': DESERT_TAN,
    'border_normal': blend(OLD_PAPER, DESERT_TAN, 0.5),
    'border_hovered': DESERT_TAN,
    'border_pressed': DESERT_TAN,

    # accent used for things that should stand out
    'accent_normal': MOSS,
    'accent_hovered': FERN,
    'accent_pressed': BAMBOO,
    'accent_border_normal': blend(FERN, BAMBOO, 0.5),
    'accent_border_hovered': BAMBOO,
    'accent_border_pressed': BAMBOO,
}

TEXTBOX = {
    'normal': CREAM,
    'hovered': CREAM,
    'pressed': OLD_PAPER,
    'border_normal': blend(OLD_PAPER, DESERT_TAN, 0.5),
    'border_hovered': blend(OLD_PAPER, DESERT_TAN, 0.5),
    'border_pressed': DESERT_TAN,
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

