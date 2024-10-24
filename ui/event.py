# standard library
from threading import Thread
from typing import Callable, Optional, Any

# 3rd party
import pygame
from pygame import Event, Vector2 as vec2

# local
from .misc import SequentialDict



ListenerFunc = Callable[[Event], Any]



class Listener:
    __slots__ = '_func', '_group'

    def __init__(self, func: ListenerFunc, group: int) -> None:
        self._func = func
        self._group = group

    def __call__(self, event: Event) -> Any:
        return self._func(event)



class EventManager:
    __slots__ = 'listeners', 'groups', 'mouse_pos', 'mouse_rel', 'mouse_attention', '_key_pressed', '_mouse_button_pressed', 'running', '_group_id'

    def __init__(self) -> None:
        # listeners
        self.listeners: dict[int, SequentialDict[Listener]] = {}
        self.groups: dict[int, list[tuple[int, int]]] = {}

        # mouse
        self.mouse_pos = vec2(0)
        self.mouse_rel = vec2(0)
        self.mouse_attention = False

        # mouse buttons and keys
        self._key_pressed: dict[int, bool] = dict()
        self._mouse_button_pressed: dict[int, bool] = dict()

        # running
        self.running = True

        # group id
        self._group_id = 0

    def update(self) -> None:
        # reset relative mouse movement
        self.mouse_rel = vec2(0)

        # loop through events
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.running = False

                case pygame.KEYDOWN:
                    self._key_pressed[event.key] = True

                case pygame.KEYUP:
                    self._key_pressed[event.key] = False

                case pygame.MOUSEBUTTONDOWN:
                    self._mouse_button_pressed[event.button] = True

                case pygame.MOUSEBUTTONUP:
                    self._mouse_button_pressed[event.button] = False

                case pygame.MOUSEMOTION:
                    self.mouse_rel = vec2(event.pos) - self.mouse_pos
                    self.mouse_pos = vec2(event.pos)

            if event.type in self.listeners:
                listeners = [l for l in self.listeners[event.type].values()]

                for listener in listeners:
                    listener(event)

    def set_timer(
            self,
            seconds: float,
            event: Event,
            repeat: int = 1
        ) -> None:

        '''
        Post an event after `seconds` seconds `repeat` times.
        '''

        wait_thread = Thread(target=self.timer_worker, args=(seconds, event, repeat))

        wait_thread.start()

    @staticmethod
    def timer_worker(seconds: float, event: Event, repeat: int):
        for _ in range(repeat):
            pygame.time.wait(round(seconds * 1000))

            pygame.event.post(event)

    def post(
            self,
            event: Event
        ) -> None:

        '''
        Post an event.
        '''

        pygame.event.post(event)

    def add_listener(
            self,
            event_type: int,
            function: ListenerFunc,
            group_id: Optional[int] = None
        ) -> int:

        '''
        Listen for an event of type `event_type` and call `function` whenever one is posted.

        `group_id` is for removing listeners. If specified, the listener will be in that group, otherwise, it will be in a newly generated group.
         
        The listener's group id is returned.
        '''

        group_id = group_id if group_id is not None else self.get_new_group()

        listener = Listener(function, group_id)

        if event_type not in self.listeners:
            self.listeners[event_type] = SequentialDict()

        # append the listener and get the index
        index = self.listeners[event_type].append(listener)

        # add that index to the group
        self.groups[group_id].append((event_type, index))

        return group_id

    def remove_listener_group(self, group_id: int) -> None:
        '''
        Deleted the group and all of its listeners.

        `group_id` shouldn't be used again for any other listeners.
        '''

        for event_type, i in self.groups[group_id]:
            del self.listeners[event_type][i]

        del self.groups[group_id]

    def key_pressed(
            self,
            key: int
        ) -> bool:

        '''
        Returns True if `key` is currently pressed.
        '''

        return key in self._key_pressed and self._key_pressed[key]

    def button_pressed(
            self,
            button: int
        ) -> bool:

        '''
        Returns True if `button` is currently pressed.
        '''

        return button in self._mouse_button_pressed and self._mouse_button_pressed[button]

    def get_custom_event_type(self) -> int:
        '''
        Returns a new custom event type.
        '''
    
        return pygame.event.custom_type()

    def get_new_group(self) -> int:
        '''
        Returns a new listener group id.
        '''

        self.groups[self._group_id] = []

        self._group_id += 1

        return self._group_id - 1



event_manager = EventManager()

