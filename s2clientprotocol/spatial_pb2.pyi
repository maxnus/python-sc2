from __future__ import annotations

from collections.abc import Iterable
from enum import Enum

from google.protobuf.message import Message

from .common_pb2 import ImageData, PointI, RectangleI

class ObservationFeatureLayer(Message):
    renders: FeatureLayers
    minimap_renders: FeatureLayersMinimap
    def __init__(
        self,
        renders: FeatureLayers = ...,
        minimap_renders: FeatureLayersMinimap = ...,
    ) -> None: ...

class FeatureLayers(Message):
    height_map: ImageData
    visibility_map: ImageData
    creep: ImageData
    power: ImageData
    player_id: ImageData
    unit_type: ImageData
    selected: ImageData
    unit_hit_points: ImageData
    unit_hit_points_ratio: ImageData
    unit_energy: ImageData
    unit_energy_ratio: ImageData
    unit_shields: ImageData
    unit_shields_ratio: ImageData
    player_relative: ImageData
    unit_density_aa: ImageData
    unit_density: ImageData
    effects: ImageData
    hallucinations: ImageData
    cloaked: ImageData
    blip: ImageData
    buffs: ImageData
    buff_duration: ImageData
    active: ImageData
    build_progress: ImageData
    buildable: ImageData
    pathable: ImageData
    placeholder: ImageData
    def __init__(
        self,
        height_map: ImageData = ...,
        visibility_map: ImageData = ...,
        creep: ImageData = ...,
        power: ImageData = ...,
        player_id: ImageData = ...,
        unit_type: ImageData = ...,
        selected: ImageData = ...,
        unit_hit_points: ImageData = ...,
        unit_hit_points_ratio: ImageData = ...,
        unit_energy: ImageData = ...,
        unit_energy_ratio: ImageData = ...,
        unit_shields: ImageData = ...,
        unit_shields_ratio: ImageData = ...,
        player_relative: ImageData = ...,
        unit_density_aa: ImageData = ...,
        unit_density: ImageData = ...,
        effects: ImageData = ...,
        hallucinations: ImageData = ...,
        cloaked: ImageData = ...,
        blip: ImageData = ...,
        buffs: ImageData = ...,
        buff_duration: ImageData = ...,
        active: ImageData = ...,
        build_progress: ImageData = ...,
        buildable: ImageData = ...,
        pathable: ImageData = ...,
        placeholder: ImageData = ...,
    ) -> None: ...

class FeatureLayersMinimap(Message):
    height_map: ImageData
    visibility_map: ImageData
    creep: ImageData
    camera: ImageData
    player_id: ImageData
    player_relative: ImageData
    selected: ImageData
    alerts: ImageData
    buildable: ImageData
    pathable: ImageData
    unit_type: ImageData
    def __init__(
        self,
        height_map: ImageData = ...,
        visibility_map: ImageData = ...,
        creep: ImageData = ...,
        camera: ImageData = ...,
        player_id: ImageData = ...,
        player_relative: ImageData = ...,
        selected: ImageData = ...,
        alerts: ImageData = ...,
        buildable: ImageData = ...,
        pathable: ImageData = ...,
        unit_type: ImageData = ...,
    ) -> None: ...

class ObservationRender(Message):
    map: ImageData
    minimap: ImageData
    def __init__(self, map: ImageData = ..., minimap: ImageData = ...) -> None: ...

class ActionSpatial(Message):
    unit_command: ActionSpatialUnitCommand
    camera_move: ActionSpatialCameraMove
    unit_selection_point: ActionSpatialUnitSelectionPoint
    unit_selection_rect: ActionSpatialUnitSelectionRect
    def __init__(
        self,
        unit_command: ActionSpatialUnitCommand = ...,
        camera_move: ActionSpatialCameraMove = ...,
        unit_selection_point: ActionSpatialUnitSelectionPoint = ...,
        unit_selection_rect: ActionSpatialUnitSelectionRect = ...,
    ) -> None: ...

class ActionSpatialUnitCommand(Message):
    ability_id: int
    target_screen_coord: PointI
    target_minimap_coord: PointI
    queue_command: bool
    def __init__(
        self,
        ability_id: int = ...,
        target_screen_coord: PointI = ...,
        target_minimap_coord: PointI = ...,
        queue_command: bool = ...,
    ) -> None: ...

class ActionSpatialCameraMove(Message):
    center_minimap: PointI
    def __init__(self, center_minimap: PointI = ...) -> None: ...

class Type(Enum):
    Select: int
    Toggle: int
    AllType: int
    AddAllType: int

class ActionSpatialUnitSelectionPoint(Message):
    selection_screen_coord: PointI
    type: int
    def __init__(self, selection_screen_coord: PointI = ..., type: int = ...) -> None: ...

class ActionSpatialUnitSelectionRect(Message):
    selection_screen_coord: Iterable[RectangleI]
    selection_add: bool
    def __init__(self, selection_screen_coord: Iterable[RectangleI] = ..., selection_add: bool = ...) -> None: ...
