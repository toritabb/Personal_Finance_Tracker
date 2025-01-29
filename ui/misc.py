from collections.abc import Iterator
from typing import Callable, Generic, TypeVar, Any



SequentialDictType = TypeVar('SequentialDictType')
PointerType = TypeVar('PointerType')



class SequentialDict(dict[int, SequentialDictType]):
    __slots__ = '_i'

    def __init__(self) -> None:
        super().__init__()

        self._i = 0

    def __iter__(self) -> Iterator[SequentialDictType]:
        return super().values().__iter__()

    def append(self, value: SequentialDictType) -> int:
        self[self._i] = value

        self._i += 1

        return self._i - 1



class Pointer(Generic[PointerType]):
    __slots__ = '_value', '_listeners'

    def __init__(self, value: PointerType) -> None:
        self._value = value
        self._listeners: SequentialDict[Callable[[Pointer[PointerType]], Any]] = SequentialDict()

    def __bool__(self) -> bool:
        return bool(self._value)

    def get(self) -> PointerType:
        return self._value

    def set(self, value: PointerType) -> None:
        self._value = value

        for listener in self._listeners.values():
            listener(self)

    def listen(self, func: Callable[['Pointer[PointerType]'], Any]) -> int:
        return self._listeners.append(func)

    def stop_listening(self, listener_id: int) -> None:
        del self._listeners[listener_id]



def clamp(value: float, _min: float, _max: float) -> float:
    return min(_max, max(_min, value))



def lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t

