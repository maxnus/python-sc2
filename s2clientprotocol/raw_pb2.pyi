from collections.abc import Iterable
from enum import Enum

from google.protobuf.message import Message

from .common_pb2 import ImageData, Point, Point2D, RectangleI, Size2DI

class StartRaw(Message):
    map_size: Size2DI
    pathing_grid: ImageData
    terrain_height: ImageData
    placement_grid: ImageData
    playable_area: RectangleI
    start_locations: Iterable[Point2D]
    def __init__(
        self,
        map_size: Size2DI = ...,
        pathing_grid: ImageData = ...,
        terrain_height: ImageData = ...,
        placement_grid: ImageData = ...,
        playable_area: RectangleI = ...,
        start_locations: Iterable[Point2D] = ...,
    ) -> None: ...

class ObservationRaw(Message):
    player: PlayerRaw
    units: Iterable[Unit]
    map_state: MapState
    event: Event
    effects: Iterable[Effect]
    radar: Iterable[RadarRing]
    def __init__(
        self,
        player: PlayerRaw = ...,
        units: Iterable[Unit] = ...,
        map_state: MapState = ...,
        event: Event = ...,
        effects: Iterable[Effect] = ...,
        radar: Iterable[RadarRing] = ...,
    ) -> None: ...

class RadarRing(Message):
    pos: Point
    radius: float
    def __init__(self, pos: Point = ..., radius: float = ...) -> None: ...

class PowerSource(Message):
    pos: Point
    radius: float
    tag: int
    def __init__(self, pos: Point = ..., radius: float = ..., tag: int = ...) -> None: ...

class PlayerRaw(Message):
    power_sources: Iterable[PowerSource]
    camera: Point
    upgrade_ids: Iterable[int]
    def __init__(
        self,
        power_sources: Iterable[PowerSource] = ...,
        camera: Point = ...,
        upgrade_ids: Iterable[int] = ...,
    ) -> None: ...

class UnitOrder(Message):
    ability_id: int
    target_world_space_pos: Point
    target_unit_tag: int
    progress: float
    def __init__(
        self,
        ability_id: int = ...,
        target_world_space_pos: Point = ...,
        target_unit_tag: int = ...,
        progress: float = ...,
    ) -> None: ...

class DisplayType(Enum):
    Visible: int
    Snapshot: int
    Hidden: int
    Placeholder: int

class Alliance(Enum):
    Self: int
    Ally: int
    Neutral: int
    Enemy: int

class CloakState(Enum):
    CloakedUnknown: int
    Cloaked: int
    CloakedDetected: int
    NotCloaked: int
    CloakedAllied: int

class PassengerUnit(Message):
    tag: int
    health: float
    health_max: float
    shield: float
    shield_max: float
    energy: float
    energy_max: float
    unit_type: int
    def __init__(
        self,
        tag: int = ...,
        health: float = ...,
        health_max: float = ...,
        shield: float = ...,
        shield_max: float = ...,
        energy: float = ...,
        energy_max: float = ...,
        unit_type: int = ...,
    ) -> None: ...

class RallyTarget(Message):
    point: Point
    tag: int
    def __init__(self, point: Point = ..., tag: int = ...) -> None: ...

class Unit(Message):
    display_type: int
    alliance: int
    tag: int
    unit_type: int
    owner: int
    pos: Point
    facing: float
    radius: float
    build_progress: float
    cloak: int
    buff_ids: Iterable[int]
    detect_range: float
    radar_range: float
    is_selected: bool
    is_on_screen: bool
    is_blip: bool
    is_powered: bool
    is_active: bool
    attack_upgrade_level: int
    armor_upgrade_level: int
    shield_upgrade_level: int
    health: float
    health_max: float
    shield: float
    shield_max: float
    energy: float
    energy_max: float
    mineral_contents: int
    vespene_contents: int
    is_flying: bool
    is_burrowed: bool
    is_hallucination: bool
    orders: Iterable[UnitOrder]
    add_on_tag: int
    passengers: Iterable[PassengerUnit]
    cargo_space_taken: int
    cargo_space_max: int
    assigned_harvesters: int
    ideal_harvesters: int
    weapon_cooldown: float
    engaged_target_tag: int
    buff_duration_remain: int
    buff_duration_max: int
    rally_targets: Iterable[RallyTarget]
    def __init__(
        self,
        display_type: int = ...,
        alliance: int = ...,
        tag: int = ...,
        unit_type: int = ...,
        owner: int = ...,
        pos: Point = ...,
        facing: float = ...,
        radius: float = ...,
        build_progress: float = ...,
        cloak: int = ...,
        buff_ids: Iterable[int] = ...,
        detect_range: float = ...,
        radar_range: float = ...,
        is_selected: bool = ...,
        is_on_screen: bool = ...,
        is_blip: bool = ...,
        is_powered: bool = ...,
        is_active: bool = ...,
        attack_upgrade_level: int = ...,
        armor_upgrade_level: int = ...,
        shield_upgrade_level: int = ...,
        health: float = ...,
        health_max: float = ...,
        shield: float = ...,
        shield_max: float = ...,
        energy: float = ...,
        energy_max: float = ...,
        mineral_contents: int = ...,
        vespene_contents: int = ...,
        is_flying: bool = ...,
        is_burrowed: bool = ...,
        is_hallucination: bool = ...,
        orders: Iterable[UnitOrder] = ...,
        add_on_tag: int = ...,
        passengers: Iterable[PassengerUnit] = ...,
        cargo_space_taken: int = ...,
        cargo_space_max: int = ...,
        assigned_harvesters: int = ...,
        ideal_harvesters: int = ...,
        weapon_cooldown: float = ...,
        engaged_target_tag: int = ...,
        buff_duration_remain: int = ...,
        buff_duration_max: int = ...,
        rally_targets: Iterable[RallyTarget] = ...,
    ) -> None: ...

class MapState(Message):
    visibility: ImageData
    creep: ImageData
    def __init__(self, visibility: ImageData = ..., creep: ImageData = ...) -> None: ...

class Event(Message):
    dead_units: Iterable[int]
    def __init__(self, dead_units: Iterable[int] = ...) -> None: ...

class Effect(Message):
    effect_id: int
    pos: Iterable[Point2D]
    alliance: int
    owner: int
    radius: float
    def __init__(
        self,
        effect_id: int = ...,
        pos: Iterable[Point2D] = ...,
        alliance: int = ...,
        owner: int = ...,
        radius: float = ...,
    ) -> None: ...

class ActionRaw(Message):
    unit_command: ActionRawUnitCommand
    camera_move: ActionRawCameraMove
    toggle_autocast: ActionRawToggleAutocast
    def __init__(
        self,
        unit_command: ActionRawUnitCommand = ...,
        camera_move: ActionRawCameraMove = ...,
        toggle_autocast: ActionRawToggleAutocast = ...,
    ) -> None: ...

class ActionRawUnitCommand(Message):
    ability_id: int
    target_world_space_pos: Point2D
    target_unit_tag: int
    unit_tags: Iterable[int]
    queue_command: bool
    def __init__(
        self,
        ability_id: int = ...,
        target_world_space_pos: Point2D = ...,
        target_unit_tag: int = ...,
        unit_tags: Iterable[int] = ...,
        queue_command: bool = ...,
    ) -> None: ...

class ActionRawCameraMove(Message):
    center_world_space: Point
    def __init__(self, center_world_space: Point = ...) -> None: ...

class ActionRawToggleAutocast(Message):
    ability_id: int
    unit_tags: Iterable[int]
    def __init__(self, ability_id: int = ..., unit_tags: Iterable[int] = ...) -> None: ...
