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
_CUSTOM_FONTS = {
    'nunito': get_global_path('ui/fonts/Nunito.ttf'),
    'nunito-bold': get_global_path('ui/fonts/Nunito_bold.ttf'),
    'nunito-italic': get_global_path('ui/fonts/Nunito_italic.ttf'),
    'nunito-bold-italic': get_global_path('ui/fonts/Nunito_bold_italic.ttf')
}



@lru_cache()
def get_font(font: FontDescriptor) -> freetype.Font:
    name = font[0].lower()

    if name in _SYSFONTS:
        return freetype.SysFont(*font) # type: ignore

    elif name in _CUSTOM_FONTS:
        if len(font) > 2:
            name += '-bold' * font[2] + '-italic' * font[3]

        f = freetype.Font(_CUSTOM_FONTS[name], font[1])

        f.kerning = True

        return f
    
    else:
        raise Exception(f'Invalid font "{font[0]}"')

