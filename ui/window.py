# 3rd party
import pygame

# local
from .base import Canvas



__all__ = 'Window',



class Window(Canvas):
    __slots__ = 'clock'

    def __init__(
            self,
            size: tuple[int, int],
            center: bool = True
        ) -> None:

        super().__init__(None, (0, 0, 0, 0))

        self.surface = pygame.display.set_mode(size)
        self.clock = pygame.Clock()

        pygame.display.set_caption('Finance Manager', 'Finance Manager aaaaaaa')
        
        if center:
            screen_size = pygame.display.get_desktop_sizes()[0]

            pygame.display.set_window_position(((screen_size[0] - size[0]) // 2, (screen_size[1] - size[1]) // 2))

    def render(self) -> None:
        super().render()

        pygame.display.flip()

        self.clock.tick(30)


