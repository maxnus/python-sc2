from collections.abc import Iterable
from enum import Enum

from google.protobuf.message import Message

class Target(Enum):
    # NONE: int
    Point: int
    Unit: int
    PointOrUnit: int
    PointOrNone: int

class AbilityData(Message):
    ability_id: int
    link_name: str
    link_index: int
    button_name: str
    friendly_name: str
    hotkey: str
    remaps_to_ability_id: int
    available: bool
    target: int
    allow_minimap: bool
    allow_autocast: bool
    is_building: bool
    footprint_radius: float
    is_instant_placement: bool
    cast_range: float
    def __init__(
        self,
        ability_id: int = ...,
        link_name: str = ...,
        link_index: int = ...,
        button_name: str = ...,
        friendly_name: str = ...,
        hotkey: str = ...,
        remaps_to_ability_id: int = ...,
        available: bool = ...,
        target: int = ...,
        allow_minimap: bool = ...,
        allow_autocast: bool = ...,
        is_building: bool = ...,
        footprint_radius: float = ...,
        is_instant_placement: bool = ...,
        cast_range: float = ...,
    ) -> None: ...

class Attribute(Enum):
    Light: int
    Armored: int
    Biological: int
    Mechanical: int
    Robotic: int
    Psionic: int
    Massive: int
    Structure: int
    Hover: int
    Heroic: int
    Summoned: int

class DamageBonus(Message):
    attribute: int
    bonus: float
    def __init__(self, attribute: int = ..., bonus: float = ...) -> None: ...

class TargetType(Enum):
    Ground: int
    Air: int
    Any: int

class Weapon(Message):
    type: int
    damage: float
    damage_bonus: Iterable[DamageBonus]
    attacks: int
    range: float
    speed: float
    def __init__(
        self,
        type: int = ...,
        damage: float = ...,
        damage_bonus: Iterable[DamageBonus] = ...,
        attacks: int = ...,
        range: float = ...,
        speed: float = ...,
    ) -> None: ...

class UnitTypeData(Message):
    unit_id: int
    name: str
    available: bool
    cargo_size: int
    mineral_cost: int
    vespene_cost: int
    food_required: float
    food_provided: float
    ability_id: int
    race: int
    build_time: float
    has_vespene: bool
    has_minerals: bool
    sight_range: float
    tech_alias: Iterable[int]
    unit_alias: int
    tech_requirement: int
    require_attached: bool
    attributes: Iterable[int]
    movement_speed: float
    armor: float
    weapons: Iterable[Weapon]
    def __init__(
        self,
        unit_id: int = ...,
        name: str = ...,
        available: bool = ...,
        cargo_size: int = ...,
        mineral_cost: int = ...,
        vespene_cost: int = ...,
        food_required: float = ...,
        food_provided: float = ...,
        ability_id: int = ...,
        race: int = ...,
        build_time: float = ...,
        has_vespene: bool = ...,
        has_minerals: bool = ...,
        sight_range: float = ...,
        tech_alias: Iterable[int] = ...,
        unit_alias: int = ...,
        tech_requirement: int = ...,
        require_attached: bool = ...,
        attributes: Iterable[int] = ...,
        movement_speed: float = ...,
        armor: float = ...,
        weapons: Iterable[Weapon] = ...,
    ) -> None: ...

class UpgradeData(Message):
    upgrade_id: int
    name: str
    mineral_cost: int
    vespene_cost: int
    research_time: float
    ability_id: int
    def __init__(
        self,
        upgrade_id: int = ...,
        name: str = ...,
        mineral_cost: int = ...,
        vespene_cost: int = ...,
        research_time: float = ...,
        ability_id: int = ...,
    ) -> None: ...

class BuffData(Message):
    buff_id: int
    name: str
    def __init__(self, buff_id: int = ..., name: str = ...) -> None: ...

class EffectData(Message):
    effect_id: int
    name: str
    friendly_name: str
    radius: float
    def __init__(
        self,
        effect_id: int = ...,
        name: str = ...,
        friendly_name: str = ...,
        radius: float = ...,
    ) -> None: ...
