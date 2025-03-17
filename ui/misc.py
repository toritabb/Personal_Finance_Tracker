from collections.abc import Iterator
from typing import Callable, Generic, TypeVar, Any



__all__ = 'Pointer',


SequentialDictType = TypeVar('SequentialDictType')
PointerType = TypeVar('PointerType')



class SequentialDict(dict[int, tuple[SequentialDictType, int]]):
    __slots__ = '_i'

    def __init__(self) -> None:
        super().__init__()

        self._i = 0

    def __getitem__(self, key: int) -> SequentialDictType:
        return super().__getitem__(key)[0]

    def __setitem__(self, key: tuple[int, int], value: SequentialDictType) -> None:
        return super().__setitem__(key[0], (value, key[1]))

    def append(self, value: SequentialDictType, priority: int = 1) -> int:
        self[self._i, priority] = value

        self._i += 1

        return self._i - 1

    def get_values(self) -> list[SequentialDictType]:
        values = [v[0] for v in sorted(self.values(), key=lambda x: x[1])]

        return values



class Pointer(Generic[PointerType]):
    __slots__ = '_value', '_listeners'

    def __init__(self, value: PointerType) -> None:
        self._value = value
        self._listeners: SequentialDict[Callable[[Pointer[PointerType]], Any]] = SequentialDict()

    def __bool__(self) -> bool:
        return bool(self._value)

    def get(self) -> PointerType:
        return self._value

    def set_no_listen(self, value: PointerType) -> None:
        self._value = value

    def set(self, value: PointerType) -> None:
        self._value = value

        for listener in self._listeners.get_values():
            listener(self)

    def listen(self, func: Callable[['Pointer[PointerType]'], Any], priority: int = 1) -> int:
        return self._listeners.append(func, priority)

    def stop_listening(self, listener_id: int) -> None:
        del self._listeners[listener_id]



def clamp(value: float, _min: float, _max: float) -> float:
    return min(_max, max(_min, value))



def lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t

