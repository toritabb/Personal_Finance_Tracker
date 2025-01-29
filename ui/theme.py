# 3rd party
from pygame import Color

# local
from ._color_funcs import *



# base colors
LIGHT_GREEN = Color(96, 108, 56)
MEDIUM_GREEN = Color(68, 81, 40)
DARK_GREEN = Color(40, 54, 24)
CREAM = Color(254, 250, 224)
TAN = Color(221, 161, 94)
BROWN = Color(188, 108, 37)
CHARCOAL = Color(14, 18, 23)


# element colors
BACKGROUND = CREAM

TEXT = CHARCOAL
TEXT_COLORKEY = invert(TEXT)

BUTTON = {
    'normal': LIGHT_GREEN,
    'hovered': lighten(LIGHT_GREEN, 0.2),
    'pressed': darken(LIGHT_GREEN, 0.2),
    'border_normal': MEDIUM_GREEN,
    'border_hovered': lighten(MEDIUM_GREEN, 0.2),
    'border_pressed': darken(MEDIUM_GREEN, 0.2),
}

TEXTBOX = {
    'normal': LIGHT_GREEN,
    'hovered': LIGHT_GREEN,
    'pressed': LIGHT_GREEN,
    'border_normal': darken(LIGHT_GREEN, 0.2),
    'border_hovered': darken(LIGHT_GREEN, 0.2),
    'border_pressed': darken(LIGHT_GREEN, 0.4),
}

TOGGLE = {
    'normal': LIGHT_GREEN,
    'hovered': lighten(LIGHT_GREEN, 0.2),
    'pressed': darken(LIGHT_GREEN, 0.2),
    'fill_normal': DARK_GREEN,
    'fill_hovered': lighten(DARK_GREEN, 0.15),
    'fill_pressed': darken(DARK_GREEN, 0.15),
}

