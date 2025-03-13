# standard library
from typing import Literal, Optional, Sequence

# 3rd party
import pygame
from pygame import Rect, Surface

# local
from .collision import CollisionShape
from .event import Event, event_manager
from .misc import SequentialDict
from .theme import Color, BACKGROUND
from .vector import vec2
from ._typing import Coordinate, RectValue



__all__ = 'center', 'UIElement', 'Interactable', 'Canvas'

_REVOKE_MOUSE_ATTENTION = event_manager.get_custom_event_type()



def center(*elements: 'UIElement', axis: Literal['x', 'y', 'xy'] = 'x') -> None:
    '''
    Centers elements inside their parent (the screen for most things).

    Elements will stay in the same place relative to each other
    '''

    parent = elements[0].parent
    bounding_box = pygame.Rect.unionall(elements[0], [e for e in elements])

    match axis:
        case 'x':
            dx = parent.centerx - parent.x - bounding_box.centerx

            for element in elements:
                element.move_offset(dx, 0)

        case 'y':
            dy = parent.centery - parent.y - bounding_box.centery

            for element in elements:
                element.move_offset(0, dy)

        case 'xy':
            dx = parent.centerx - parent.x - bounding_box.centerx
            dy = parent.centery - parent.y - bounding_box.centery

            for element in elements:
                element.move_offset(dx, dy)



class UIElement(Rect):
    __slots__ = 'parent', '_index'

    def __init__(
            self,
            parent: 'Canvas',
            rect: RectValue
        ) -> None:

        super().__init__(rect)

        self.parent = parent

        if parent is not self:
            self._index = parent.add_child(self) if parent is not None else -1

    def __repr__(self) -> str:
        return f'UI Element {self.__class__}'

    def __str__(self) -> str:
        return f'UI Element {self.__class__}'
    
    def move_offset(self, dx: int, dy: int) -> None:
        self.move_ip(dx, dy)

    def render(self, surface: Surface) -> None: ...

    def get_local_pos(self, position: Coordinate) -> vec2:
        if self.parent:
            return position + self.parent.transform

        else:
            return vec2(position)

    def close(self) -> None:
        if self.parent is not self and self._index >= 0:
            self.parent.remove_child(self._index)
            self._index = -1



class Canvas(UIElement):
    __slots__ = 'surface', 'fill_color', '_children', 'transform'

    def __init__(
            self,
            parent: 'Canvas',
            rect: RectValue,
            fill_color: Color = BACKGROUND
        ) -> None:

        super().__init__(parent, rect)

        self.surface = Surface(self.size)
        self.fill_color = fill_color

        self.surface.fill(fill_color)

        self._children: SequentialDict[UIElement] = SequentialDict()

        if parent is not self:
            self.transform = parent.transform - self.topleft

        else:
            self.transform = vec2(0, 0)

    def move_offset(self, dx: int, dy: int) -> None:
        super().move_offset(dx, dy)

        self.transform -= vec2(dx, dy)

    def add_child(self, child: 'UIElement') -> int:
        return self._children.append(child)

    def remove_child(self, child_index: int) -> None:
        del self._children[child_index]

    def render(self, surface: Optional[Surface] = None) -> None:
        self.surface.fill(self.fill_color)

        for child in self._children:
            child.render(self.surface)

        if surface is not None:
            surface.blit(self.surface, self)

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
        event_manager.add_listener(_REVOKE_MOUSE_ATTENTION, self._get_pressed, self._listener_group_id)

    def _get_hovered(self, _) -> bool:
        if (not event_manager.mouse_attention) or self.pressed:
            mouse_pos = self.get_local_pos(event_manager.mouse_pos)

            self.hovered = self.bounding_rect.collidepoint(mouse_pos) and any(shape.collidepoint(mouse_pos) for shape in self.collision_shapes)

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
            event_manager.post(Event(_REVOKE_MOUSE_ATTENTION, button = pygame.BUTTON_LEFT))

            return True
        
        return False

    def move_offset(self, dx: int, dy: int) -> None:
        super().move_offset(dx, dy)

        for collision_shape in self.collision_shapes:
            collision_shape.move_ip(dx, dy)

        self.bounding_rect.move_ip(dx, dy)

    def close(self) -> None:
        super().close()

        if self._listener_group_id >= 0:
            event_manager.remove_listener_group(self._listener_group_id)

            self._listener_group_id = -1

            if self.pressed and event_manager.mouse_attention:
                event_manager.mouse_attention = False

