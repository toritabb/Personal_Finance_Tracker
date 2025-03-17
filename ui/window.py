# 3rd party
import pygame

# local
from constants import FPS, SCREEN_SIZE, SCREEN_W, SCREEN_H
from data import data_manager
from .base import Canvas
from .event import event_manager
from .pages import PageManager



__all__ = 'Window',



class Window(Canvas):
    __slots__ = 'surface', 'clock', 'page_manager'

    def __init__(self) -> None:
        super().__init__(self, ((0, 0), SCREEN_SIZE))

        self.surface = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.Clock()
        self.page_manager = PageManager(self)

        pygame.display.set_caption('Finance Manager', 'Finance Manager')

        monitor_resolution = pygame.display.get_desktop_sizes()[0]
        pygame.display.set_window_position(((monitor_resolution[0] - SCREEN_W) // 2, (monitor_resolution[1] - SCREEN_H) // 2))

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

    def close(self) -> None:
        super().close()

        data_manager.logout_user()


