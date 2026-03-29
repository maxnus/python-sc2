from collections.abc import Iterable
from enum import Enum

from google.protobuf.message import Message

from .common_pb2 import Point, Point2D

class DebugCommand(Message):
    draw: DebugDraw
    game_state: int
    create_unit: DebugCreateUnit
    kill_unit: DebugKillUnit
    test_process: DebugTestProcess
    score: DebugSetScore
    end_game: DebugEndGame
    unit_value: DebugSetUnitValue
    def __init__(
        self,
        draw: DebugDraw = ...,
        game_state: int = ...,
        create_unit: DebugCreateUnit = ...,
        kill_unit: DebugKillUnit = ...,
        test_process: DebugTestProcess = ...,
        score: DebugSetScore = ...,
        end_game: DebugEndGame = ...,
        unit_value: DebugSetUnitValue = ...,
    ) -> None: ...

class DebugDraw(Message):
    text: Iterable[DebugText]
    lines: Iterable[DebugLine]
    boxes: Iterable[DebugBox]
    spheres: Iterable[DebugSphere]
    def __init__(
        self,
        text: Iterable[DebugText] = ...,
        lines: Iterable[DebugLine] = ...,
        boxes: Iterable[DebugBox] = ...,
        spheres: Iterable[DebugSphere] = ...,
    ) -> None: ...

class Line(Message):
    p0: Point
    p1: Point
    def __init__(self, p0: Point = ..., p1: Point = ...) -> None: ...

class Color(Message):
    r: int
    g: int
    b: int
    def __init__(self, r: int = ..., g: int = ..., b: int = ...) -> None: ...

class DebugText(Message):
    color: Color
    text: str
    virtual_pos: Point
    world_pos: Point
    size: int
    def __init__(
        self,
        color: Color = ...,
        text: str = ...,
        virtual_pos: Point = ...,
        world_pos: Point = ...,
        size: int = ...,
    ) -> None: ...

class DebugLine(Message):
    color: Color
    line: Line
    def __init__(self, color: Color = ..., line: Line = ...) -> None: ...

class DebugBox(Message):
    color: Color
    min: Point
    max: Point
    def __init__(self, color: Color = ..., min: Point = ..., max: Point = ...) -> None: ...

class DebugSphere(Message):
    color: Color
    p: Point
    r: float
    def __init__(self, color: Color = ..., p: Point = ..., r: float = ...) -> None: ...

class DebugGameState(Enum):
    show_map: int
    control_enemy: int
    food: int
    free: int
    all_resources: int
    god: int
    minerals: int
    gas: int
    cooldown: int
    tech_tree: int
    upgrade: int
    fast_build: int

class DebugCreateUnit(Message):
    unit_type: int
    owner: int
    pos: Point2D
    quantity: int
    def __init__(
        self,
        unit_type: int = ...,
        owner: int = ...,
        pos: Point2D = ...,
        quantity: int = ...,
    ) -> None: ...

class DebugKillUnit(Message):
    tag: Iterable[int]
    def __init__(self, tag: Iterable[int] = ...) -> None: ...

class Test(Enum):
    hang: int
    crash: int
    exit: int

class DebugTestProcess(Message):
    test: int
    delay_ms: int
    def __init__(self, test: int = ..., delay_ms: int = ...) -> None: ...

class DebugSetScore(Message):
    score: float
    def __init__(self, score: float = ...) -> None: ...

class EndResult(Enum):
    Surrender: int
    DeclareVictory: int

class DebugEndGame(Message):
    end_result: int
    def __init__(self, end_result: int = ...) -> None: ...

class UnitValue(Enum):
    Energy: int
    Life: int
    Shields: int

class DebugSetUnitValue(Message):
    unit_value: int
    value: float
    unit_tag: int
    def __init__(
        self,
        unit_value: int = ...,
        value: float = ...,
        unit_tag: int = ...,
    ) -> None: ...
