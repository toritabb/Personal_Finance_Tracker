# 3rd party
import pygame

# local
from constants import FPS, SCREEN_SIZE, SCREEN_W, SCREEN_H
from .base import Canvas
from .event import event_manager
from .pages import PageManager



__all__ = 'Window',



class Window(Canvas):
    __slots__ = 'surface', 'clock', 'page_manager'

    def __init__(
            self,
            center: bool = True
        ) -> None:

        super().__init__(None, ((0, 0), SCREEN_SIZE))

        self.surface = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.Clock()

        pygame.display.set_caption('Finance Manager', 'Finance Manager aaaaaaa')
        
        if center:
            screen_size = pygame.display.get_desktop_sizes()[0]

            pygame.display.set_window_position(((screen_size[0] - SCREEN_W) // 2, (screen_size[1] - SCREEN_H) // 2))

        self.page_manager = PageManager(self)

    def render(self) -> None:
        super().render(None)

        pygame.display.flip()

        self.clock.tick(FPS)

    def mainloop(self) -> None:
        while event_manager.running:
            event_manager.update()

            self.render()

            pygame.display.set_caption(f'FPS: {self.clock.get_fps():.0f}')

        self.close()


