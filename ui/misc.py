from collections.abc import Iterator
from typing import Generic, TypeVar



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
    __slots__ = '_value'

    def __init__(self, value: PointerType) -> None:
        self._value = value

    def __bool__(self) -> bool:
        return bool(self._value)

    def get(self) -> PointerType:
        return self._value

    def set(self, value: PointerType) -> None:
        self._value = value



def clamp(value: float, _min: float, _max: float) -> float:
    return min(_max, max(_min, value))

