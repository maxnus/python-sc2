from __future__ import annotations

from enum import Enum

from google.protobuf.message import Message

class ScoreType(Enum):
    Curriculum: int
    Melee: int

class Score(Message):
    score_type: int
    score: int
    score_details: ScoreDetails
    def __init__(
        self,
        score_type: int = ...,
        score: int = ...,
        score_details: ScoreDetails = ...,
    ) -> None: ...

class CategoryScoreDetails(Message):
    none: float
    army: float
    economy: float
    technology: float
    upgrade: float
    def __init__(
        self,
        none: float = ...,
        army: float = ...,
        economy: float = ...,
        technology: float = ...,
        upgrade: float = ...,
    ) -> None: ...

class VitalScoreDetails(Message):
    life: float
    shields: float
    energy: float
    def __init__(
        self,
        life: float = ...,
        shields: float = ...,
        energy: float = ...,
    ) -> None: ...

class ScoreDetails(Message):
    idle_production_time: float
    idle_worker_time: float
    total_value_units: float
    total_value_structures: float
    killed_value_units: float
    killed_value_structures: float
    collected_minerals: float
    collected_vespene: float
    collection_rate_minerals: float
    collection_rate_vespene: float
    spent_minerals: float
    spent_vespene: float
    food_used: CategoryScoreDetails
    killed_minerals: CategoryScoreDetails
    killed_vespene: CategoryScoreDetails
    lost_minerals: CategoryScoreDetails
    lost_vespene: CategoryScoreDetails
    friendly_fire_minerals: CategoryScoreDetails
    friendly_fire_vespene: CategoryScoreDetails
    used_minerals: CategoryScoreDetails
    used_vespene: CategoryScoreDetails
    total_used_minerals: CategoryScoreDetails
    total_used_vespene: CategoryScoreDetails
    total_damage_dealt: VitalScoreDetails
    total_damage_taken: VitalScoreDetails
    total_healed: VitalScoreDetails
    current_apm: float
    current_effective_apm: float
    def __init__(
        self,
        idle_production_time: float = ...,
        idle_worker_time: float = ...,
        total_value_units: float = ...,
        total_value_structures: float = ...,
        killed_value_units: float = ...,
        killed_value_structures: float = ...,
        collected_minerals: float = ...,
        collected_vespene: float = ...,
        collection_rate_minerals: float = ...,
        collection_rate_vespene: float = ...,
        spent_minerals: float = ...,
        spent_vespene: float = ...,
        food_used: CategoryScoreDetails = ...,
        killed_minerals: CategoryScoreDetails = ...,
        killed_vespene: CategoryScoreDetails = ...,
        lost_minerals: CategoryScoreDetails = ...,
        lost_vespene: CategoryScoreDetails = ...,
        friendly_fire_minerals: CategoryScoreDetails = ...,
        friendly_fire_vespene: CategoryScoreDetails = ...,
        used_minerals: CategoryScoreDetails = ...,
        used_vespene: CategoryScoreDetails = ...,
        total_used_minerals: CategoryScoreDetails = ...,
        total_used_vespene: CategoryScoreDetails = ...,
        total_damage_dealt: VitalScoreDetails = ...,
        total_damage_taken: VitalScoreDetails = ...,
        total_healed: VitalScoreDetails = ...,
        current_apm: float = ...,
        current_effective_apm: float = ...,
    ) -> None: ...
