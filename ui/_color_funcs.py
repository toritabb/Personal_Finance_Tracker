# 3rd party
from pygame import Color

# local
from .misc import clamp, lerp



__all__ = 'lighten', 'darken', 'saturate', 'desaturate', 'blend', 'invert_color'



def lighten(color: Color, percent: float) -> Color:
    hsva = color.hsva

    new_v = clamp(hsva[2] * (1 + percent), 0, 100)

    new_color = Color.from_hsva(hsva[0], hsva[1], new_v, hsva[3])

    return new_color



def darken(color: Color, percent: float) -> Color:
    hsva = color.hsva

    new_v = clamp(hsva[2] * (1 - percent), 0, 100)

    new_color = Color.from_hsva(hsva[0], hsva[1], new_v, hsva[3])

    return new_color



def saturate(color: Color, percent: float) -> Color:
    hsva = color.hsva

    new_s = clamp(hsva[1] * (1 + percent), 0, 255)

    new_color = Color.from_hsva(hsva[0], new_s, hsva[2], hsva[3])

    return new_color



def desaturate(color: Color, percent: float) -> Color:
    hsva = color.hsva

    new_s = clamp(hsva[1] * (1 - percent), 0, 255)

    new_color = Color.from_hsva(hsva[0], new_s, hsva[2], hsva[3])

    return new_color



def blend(color1: Color, color2: Color, percent: float) -> Color:
    return Color(
        int(lerp(color1.r, color2.r, percent)),
        int(lerp(color1.g, color2.g, percent)),
        int(lerp(color1.b, color2.b, percent)),
    )



def invert_color(color: Color) -> Color:
    return Color(
        255 - color.r,
        255 - color.g,
        255 - color.b,
    )

