# standard library
from math import cos, sin, tau
from typing import Optional

# 3rd party
import pygame
from pygame import Surface
import pygame.gfxdraw

# local
from .base import Canvas
from .color import random as random_color
from .event import Event, event_manager
from .theme import Color, COLOR_MAP
from ._typing import Coordinate



__all__ = 'PieChart', 'PieChartSlice'



class PieChartSlice:
    __slots__ = 'name', 'value', 'color'

    def __init__(
            self,
            name: str,
            value: float,
            color: Optional[Color] = None
        ) -> None:

        self.name = name
        self.value = value
        self.color = random_color() if color is None else color



class PieChart(Canvas):
    __slots__ = 'options'

    def __init__(
            self,
            parent: Canvas,
            pos: Coordinate,
            size: int,
            options: list[PieChartSlice],
            *,
            thickness_percent: float = 0.4,
            gap: int = 0
        ) -> None:

        super().__init__(parent, (pos, (size - 1, size - 1)))

        padded_size = size
        thickness = int(padded_size * thickness_percent)

        self.options = options

        # render a bigger version of the pie chart to scale down for antialiasing
        big_surface = pygame.Surface((size * 2, size * 2), pygame.SRCALPHA)
        big_surface.fill(self.fill_color)

        total_scalar = tau / sum(option.value for option in self.options)
        angles = [0.0]

        for option in self.options:
            angles.append(angles[-1] + option.value * total_scalar)

            pygame.draw.arc(big_surface, option.color, (0, 0, size * 2, size * 2), angles[-2], angles[-1], thickness)

        for angle in angles[:-1]:
            pygame.draw.line(big_surface, self.fill_color, (size, size), (size + cos(angle) * (size + gap), size + sin(angle) * -(size + gap)), gap * 2)

        pygame.draw.circle(big_surface, self.fill_color, (size, size), gap - 1)

        # scale the surface down and put it on the displayed one
        pygame.transform.smoothscale(big_surface, self.surface.size, self.surface)

    def render(self, surface: Surface) -> None:
        surface.blit(self.surface, self)

    # def _old_render(self, surface: Surface) -> None:
    #     self.surface.fill(self.fill_color)

    #     total_scalar = tau / sum(option.value for option in self.options)
    #     angles = [0.0]

    #     for option in self.options:
    #         angles.append(angles[-1] + option.value * total_scalar)

    #         pygame.draw.arc(self.surface, option.color, self._rect, angles[-2], angles[-1], self._thickness)

    #     for angle in angles[:-1]:
    #         pygame.draw.aaline(self.surface, self.fill_color, self._rect.center, self._rect.center + vec2(cos(angle) * self._rect.width, sin(angle) * -self._rect.width), self._gap)

    #     surface.blit(self.surface, self)

