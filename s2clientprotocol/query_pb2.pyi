from collections.abc import Iterable

from google.protobuf.message import Message

from .common_pb2 import AvailableAbility, Point2D

class RequestQuery(Message):
    pathing: Iterable[RequestQueryPathing]
    abilities: Iterable[RequestQueryAvailableAbilities]
    placements: Iterable[RequestQueryBuildingPlacement]
    ignore_resource_requirements: bool
    def __init__(
        self,
        pathing: Iterable[RequestQueryPathing] = ...,
        abilities: Iterable[RequestQueryAvailableAbilities] = ...,
        placements: Iterable[RequestQueryBuildingPlacement] = ...,
        ignore_resource_requirements: bool = ...,
    ) -> None: ...

class ResponseQuery(Message):
    pathing: Iterable[ResponseQueryPathing]
    abilities: Iterable[ResponseQueryAvailableAbilities]
    placements: Iterable[ResponseQueryBuildingPlacement]
    def __init__(
        self,
        pathing: Iterable[ResponseQueryPathing] = ...,
        abilities: Iterable[ResponseQueryAvailableAbilities] = ...,
        placements: Iterable[ResponseQueryBuildingPlacement] = ...,
    ) -> None: ...

class RequestQueryPathing(Message):
    start_pos: Point2D
    unit_tag: int
    end_pos: Point2D
    def __init__(
        self,
        start_pos: Point2D = ...,
        unit_tag: int = ...,
        end_pos: Point2D = ...,
    ) -> None: ...

class ResponseQueryPathing(Message):
    distance: float
    def __init__(self, distance: float = ...) -> None: ...

class RequestQueryAvailableAbilities(Message):
    unit_tag: int
    def __init__(self, unit_tag: int = ...) -> None: ...

class ResponseQueryAvailableAbilities(Message):
    abilities: Iterable[AvailableAbility]
    unit_tag: int
    unit_type_id: int
    def __init__(
        self,
        abilities: Iterable[AvailableAbility] = ...,
        unit_tag: int = ...,
        unit_type_id: int = ...,
    ) -> None: ...

class RequestQueryBuildingPlacement(Message):
    ability_id: int
    target_pos: Point2D
    placing_unit_tag: int
    def __init__(
        self,
        ability_id: int = ...,
        target_pos: Point2D = ...,
        placing_unit_tag: int = ...,
    ) -> None: ...

class ResponseQueryBuildingPlacement(Message):
    result: int
    def __init__(self, result: int = ...) -> None: ...
