# standard library
from math import cos, sin, tau
from typing import Optional

# 3rd party
import pygame
from pygame import Surface

# local
from .base import Canvas
from .color import random as random_color
from .event import Event, event_manager
from .theme import Color, COLOR_MAP, DESERT_TAN
from .vector import vec2
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
            gap: int = 0,
            border_color: Optional[Color] = None
        ) -> None:

        super().__init__(parent, (pos, (size - 1, size - 1)))

        gap *= 2

        padded_size = size - gap * (border_color is not None)
        thickness = int(padded_size * thickness_percent)

        self.options = options

        # render a bigger version of the pie chart to scale down for antialiasing
        if border_color is not None:
            big_surface = pygame.Surface(((padded_size + gap) * 2, (padded_size + gap) * 2), flags=pygame.SRCALPHA)
            
            rect = pygame.Rect(gap, gap, padded_size * 2, padded_size * 2)

        else:
            big_surface = pygame.Surface((padded_size * 2, padded_size * 2), flags=pygame.SRCALPHA)

            rect = big_surface.get_rect()

        center = vec2(rect.center)

        big_surface.fill(self.fill_color)

        total_scalar = tau / sum(option.value for option in self.options)
        angles = [0.0]

        if border_color is not None:
            pygame.draw.circle(big_surface, border_color, center, padded_size + gap)

        for option in self.options:
            angles.append(angles[-1] + option.value * total_scalar)

            pygame.draw.arc(big_surface, option.color, rect, angles[-2] - 0.005, angles[-1], thickness)

        for angle in angles[:-1]:
            pygame.draw.line(big_surface, self.fill_color if border_color is None else border_color, center, center + vec2(cos(angle), -sin(angle)) * (padded_size + gap - 2), gap + 1)

        pygame.draw.circle(big_surface, self.fill_color, center, (gap * 0.5 - 1) if border_color is None else padded_size - thickness - gap)

        # scale the surface down and put it on the displayed one
        pygame.transform.smoothscale(big_surface, self.surface.size, self.surface)

    def render(self, surface: Surface) -> None:
        surface.blit(self.surface, self)

