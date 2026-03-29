from __future__ import annotations

from collections.abc import Iterable
from enum import Enum

from google.protobuf.message import Message

class ObservationUI(Message):
    groups: Iterable[ControlGroup]
    single: SinglePanel
    multi: MultiPanel
    cargo: CargoPanel
    production: ProductionPanel
    def __init__(
        self,
        groups: Iterable[ControlGroup] = ...,
        single: SinglePanel = ...,
        multi: MultiPanel = ...,
        cargo: CargoPanel = ...,
        production: ProductionPanel = ...,
    ) -> None: ...

class ControlGroup(Message):
    control_group_index: int
    leader_unit_type: int
    count: int
    def __init__(
        self,
        control_group_index: int = ...,
        leader_unit_type: int = ...,
        count: int = ...,
    ) -> None: ...

class UnitInfo(Message):
    unit_type: int
    player_relative: int
    health: int
    shields: int
    energy: int
    transport_slots_taken: int
    build_progress: float
    add_on: UnitInfo
    max_health: int
    max_shields: int
    max_energy: int
    def __init__(
        self,
        unit_type: int = ...,
        player_relative: int = ...,
        health: int = ...,
        shields: int = ...,
        energy: int = ...,
        transport_slots_taken: int = ...,
        build_progress: float = ...,
        add_on: UnitInfo = ...,
        max_health: int = ...,
        max_shields: int = ...,
        max_energy: int = ...,
    ) -> None: ...

class SinglePanel(Message):
    unit: UnitInfo
    attack_upgrade_level: int
    armor_upgrade_level: int
    shield_upgrade_level: int
    buffs: Iterable[int]
    def __init__(
        self,
        unit: UnitInfo = ...,
        attack_upgrade_level: int = ...,
        armor_upgrade_level: int = ...,
        shield_upgrade_level: int = ...,
        buffs: Iterable[int] = ...,
    ) -> None: ...

class MultiPanel(Message):
    units: Iterable[UnitInfo]
    def __init__(self, units: Iterable[UnitInfo] = ...) -> None: ...

class CargoPanel(Message):
    unit: UnitInfo
    passengers: Iterable[UnitInfo]
    slots_available: int
    def __init__(
        self,
        unit: UnitInfo = ...,
        passengers: Iterable[UnitInfo] = ...,
        slots_available: int = ...,
    ) -> None: ...

class BuildItem(Message):
    ability_id: int
    build_progress: float
    def __init__(self, ability_id: int = ..., build_progress: float = ...) -> None: ...

class ProductionPanel(Message):
    unit: UnitInfo
    build_queue: Iterable[UnitInfo]
    production_queue: Iterable[BuildItem]
    def __init__(
        self,
        unit: UnitInfo = ...,
        build_queue: Iterable[UnitInfo] = ...,
        production_queue: Iterable[BuildItem] = ...,
    ) -> None: ...

class ActionUI(Message):
    control_group: ActionControlGroup
    select_army: ActionSelectArmy
    select_warp_gates: ActionSelectWarpGates
    select_larva: ActionSelectLarva
    select_idle_worker: ActionSelectIdleWorker
    multi_panel: ActionMultiPanel
    cargo_panel: ActionCargoPanelUnload
    production_panel: ActionProductionPanelRemoveFromQueue
    toggle_autocast: ActionToggleAutocast
    def __init__(
        self,
        control_group: ActionControlGroup = ...,
        select_army: ActionSelectArmy = ...,
        select_warp_gates: ActionSelectWarpGates = ...,
        select_larva: ActionSelectLarva = ...,
        select_idle_worker: ActionSelectIdleWorker = ...,
        multi_panel: ActionMultiPanel = ...,
        cargo_panel: ActionCargoPanelUnload = ...,
        production_panel: ActionProductionPanelRemoveFromQueue = ...,
        toggle_autocast: ActionToggleAutocast = ...,
    ) -> None: ...

class ControlGroupAction(Enum):
    Recall: int
    Set: int
    Append: int
    SetAndSteal: int
    AppendAndSteal: int

class ActionControlGroup(Message):
    action: int
    control_group_index: int
    def __init__(self, action: int = ..., control_group_index: int = ...) -> None: ...

class ActionSelectArmy(Message):
    selection_add: bool
    def __init__(self, selection_add: bool = ...) -> None: ...

class ActionSelectWarpGates(Message):
    selection_add: bool
    def __init__(self, selection_add: bool = ...) -> None: ...

class ActionSelectLarva(Message):
    def __init__(self) -> None: ...

class ActionSelectIdleWorker(Message):
    class Type(Enum):
        Set: int
        Add: int
        All: int
        AddAll: int

    type: int
    def __init__(self, type: int = ...) -> None: ...

class ActionMultiPanel(Message):
    class Type(Enum):
        SingleSelect: int
        DeselectUnit: int
        SelectAllOfType: int
        DeselectAllOfType: int

    type: int
    unit_index: int
    def __init__(self, type: int = ..., unit_index: int = ...) -> None: ...

class ActionCargoPanelUnload(Message):
    unit_index: int
    def __init__(self, unit_index: int = ...) -> None: ...

class ActionProductionPanelRemoveFromQueue(Message):
    unit_index: int
    def __init__(self, unit_index: int = ...) -> None: ...

class ActionToggleAutocast(Message):
    ability_id: int
    def __init__(self, ability_id: int = ...) -> None: ...
