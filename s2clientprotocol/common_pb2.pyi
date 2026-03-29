# https://github.com/Blizzard/s2client-proto/blob/bff45dae1fc685e6acbaae084670afb7d1c0832c/s2clientprotocol/common.proto
from enum import Enum

from google.protobuf.message import Message

class AvailableAbility(Message):
    ability_id: int
    requires_point: bool
    def __init__(self, ability_id: int = ..., requires_point: bool = ...) -> None: ...

class ImageData(Message):
    bits_per_pixel: int
    size: Size2DI
    data: bytes
    def __init__(self, bits_per_pixel: int = ..., size: Size2DI = ..., data: bytes = ...) -> None: ...

class PointI(Message):
    x: int
    y: int
    def __init__(self, x: int = ..., y: int = ...) -> None: ...

class RectangleI(Message):
    p0: PointI
    p1: PointI
    def __init__(self, p0: PointI = ..., p1: PointI = ...) -> None: ...

class Point2D(Message):
    x: float
    y: float
    def __init__(self, x: float = ..., y: float = ...) -> None: ...

class Point(Message):
    x: float
    y: float
    z: float
    def __init__(self, x: float = ..., y: float = ..., z: float = ...) -> None: ...

class Size2DI(Message):
    x: int
    y: int
    def __init__(self, x: int = ..., y: int = ...) -> None: ...

class Race(Enum):
    NoRace: int
    Terran: int
    Zerg: int
    Protoss: int
    Random: int
