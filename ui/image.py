# standard library
from typing import Optional

# 3rd party
import pygame
from pygame import Surface

# local
from file import get_global_path
from .base import Canvas, UIElement
from ._typing import Coordinate



__all__ = 'Image',



def load_image(image_name: str) -> Surface:
    abs_path = get_global_path(f'ui/images/{image_name}')

    image = pygame.image.load(abs_path).convert_alpha()

    return image



class Image(UIElement):
    __slots__ = 'image'

    def __init__(
            self,
            parent: Canvas,
            pos: Coordinate,
            image_name: str,
            *,
            size: Optional[Coordinate] = None
        ) -> None:

        image = load_image(image_name)

        if size is not None:
            image = pygame.transform.smoothscale(image, size)

        super().__init__(parent, (pos, image.size))

        self.image = image

    def render(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, self)

