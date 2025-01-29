# standard library
from typing import Optional, Sequence

# 3rd party
import pygame
from pygame import Rect

# local
from .collision import CollisionShape
from .event import Event, event_manager
from .misc import SequentialDict
from .theme import BACKGROUND
from .typing import Coordinate, RectValue
from .vector import vec2



__all__ = 'UIElement', 'Interactable', 'Canvas'

_REVOKE_MOUSE_ATTENTION = event_manager.get_custom_event_type()



class UIElement(Rect):
    __slots__ = 'parent', '_index'

    def __init__(
            self,
            parent: Optional['Canvas'],
            rect: RectValue
        ) -> None:

        super().__init__(rect)

        self.parent = parent
        self._index = parent.add_child(self) if parent is not None else -1

    def __str__(self) -> str:
        return f'UI Element {self.__class__}'

    def render(self, screen: pygame.Surface) -> None: ...

    def get_global_pos(self, position: Coordinate) -> vec2:
        if self.parent:
            return self.parent.transform + position

        else:
            return vec2(position)

    def close(self) -> None:
        if self.parent is not None and self._index >= 0:
            self.parent.remove_child(self._index)
            self._index = -1



class Canvas(UIElement):
    __slots__ = 'surface', '_children', 'transform'

    def __init__(
            self,
            parent: Optional['Canvas'],
            rect: RectValue
        ) -> None:

        super().__init__(parent, rect)

        self.surface = pygame.Surface(self.size)

        self._children: SequentialDict[UIElement] = SequentialDict()

        if parent is not None:
            self.transform = parent.transform - self.topright

        else:
            self.transform = vec2(0)

    def add_child(self, child: 'UIElement') -> int:
        return self._children.append(child)

    def remove_child(self, child_index: int) -> None:
        del self._children[child_index]

    def render(self) -> None:
        self.surface.fill(BACKGROUND)

        for child in self._children:
            child.render(self.surface)

    def close(self) -> None:
        super().close()

        children = [child for child in self._children]

        for child in children:
            child.close()



class Interactable(UIElement):
    __slots__ = 'collision_shapes', 'bounding_rect', 'hovered', 'pressed', '_listener_group_id'

    def __init__(
            self,
            parent: Canvas,
            collision_shapes: Sequence[CollisionShape],
            bounding_rect: Optional[Rect] = None
        ) -> None:

        if bounding_rect is not None:
            self.bounding_rect = bounding_rect
        else:
            self.bounding_rect = collision_shapes[0] if isinstance(collision_shapes[0], Rect) else collision_shapes[0].get_bounding_box()

            self.bounding_rect = self.bounding_rect.unionall([shape if isinstance(shape, Rect) else shape.get_bounding_box() for shape in collision_shapes])

        super().__init__(parent, self.bounding_rect)

        self.collision_shapes = tuple(collision_shapes)

        self.hovered = False
        self.pressed = False

        self._get_hovered(None)

        self._listener_group_id = event_manager.get_new_group()

        event_manager.add_listener(pygame.MOUSEMOTION, self._get_hovered, self._listener_group_id)
        event_manager.add_listener(pygame.MOUSEBUTTONDOWN, self._get_pressed, self._listener_group_id)
        event_manager.add_listener(pygame.MOUSEBUTTONUP, self._get_unpressed, self._listener_group_id)
        event_manager.add_listener(_REVOKE_MOUSE_ATTENTION, self._get_hovered, self._listener_group_id)

    def _get_hovered(self, _) -> bool:
        if (not event_manager.mouse_attention) or self.pressed:
            self.hovered = self.bounding_rect.collidepoint(event_manager.mouse_pos) and any(shape.collidepoint(event_manager.mouse_pos) for shape in self.collision_shapes)

            return True
        
        return False

    def _get_pressed(self, event: Event) -> bool:
        if not event_manager.mouse_attention and self.hovered and event.button == pygame.BUTTON_LEFT:
            self.pressed = True
            event_manager.mouse_attention = True

            return True
        
        return False

    def _get_unpressed(self, event: Event) -> bool:
        if self.pressed and event.button == pygame.BUTTON_LEFT:
            self.pressed = False
            event_manager.mouse_attention = False

            # update other objects in case they are hovered
            event_manager.post(Event(_REVOKE_MOUSE_ATTENTION))

            return True
        
        return False

    def close(self) -> None:
        super().close()

        if self._listener_group_id >= 0:
            event_manager.remove_listener_group(self._listener_group_id)

            self._listener_group_id = -1

