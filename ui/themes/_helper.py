from pygame import Color



__all__ = 'lighten', 'darken', 'saturate', 'desaturate'



def clamp(value: float, _min: float, _max: float) -> float:
    return max(_min, min(_max, value))



def lighten(color: Color, percent: float) -> Color:
    hsva = color.hsva

    new_v = clamp(hsva[2] * (1 + percent * 0.01), 0, 100)

    new_color = Color.from_hsva(hsva[0], hsva[1], new_v, hsva[3])

    return new_color



def darken(color: Color, percent: float) -> Color:
    hsva = color.hsva

    new_v = clamp(hsva[2] * (1 - percent * 0.01), 0, 100)

    new_color = Color.from_hsva(hsva[0], hsva[1], new_v, hsva[3])

    return new_color



def saturate(color: Color, percent: float) -> Color:
    hsva = color.hsva

    new_s = clamp(hsva[1] * (1 + percent * 0.01), 0, 255)

    new_color = Color.from_hsva(hsva[0], new_s, hsva[2], hsva[3])

    return new_color



def desaturate(color: Color, percent: float) -> Color:
    hsva = color.hsva

    new_s = clamp(hsva[1] * (1 - percent * 0.01), 0, 255)

    new_color = Color.from_hsva(hsva[0], new_s, hsva[2], hsva[3])

    return new_color

