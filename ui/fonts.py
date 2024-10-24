# standard library
from functools import lru_cache

# 3rd party
from pygame import freetype

# local
from path import get_global_path


freetype.init()



# (name, size) or (name, size, bold, italic)
FontDescriptor = tuple[str, int] | tuple[str, int, bool, bool]

_SYSFONTS = set(freetype.get_fonts())
_FONT_PATHS = {
    'inter': get_global_path('ui/fonts/Inter.ttf'),
    'lexend': get_global_path('ui/fonts/Lexend.ttf'),
    'eater': get_global_path('ui/fonts/Eater.ttf')
}



@lru_cache()
def get_font(font: FontDescriptor) -> freetype.Font:
    name = font[0].lower()

    if name in _SYSFONTS:
        return freetype.SysFont(*font) # type: ignore

    elif name in _FONT_PATHS:
        f = freetype.Font(_FONT_PATHS[name], font[1])

        f.kerning = True

        if len(font) > 2:
            f.strong = font[2]
            f.oblique = font[3]

        return f
    
    else:
        raise Exception(f'Invalid font "{font[0]}"')

