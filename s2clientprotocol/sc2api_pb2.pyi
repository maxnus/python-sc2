from __future__ import annotations

from collections.abc import Iterable
from enum import Enum

from google.protobuf.message import Message

from s2clientprotocol.spatial_pb2 import ActionSpatial, ObservationFeatureLayer, ObservationRender

from .common_pb2 import AvailableAbility, Point2D, Size2DI
from .data_pb2 import AbilityData, BuffData, EffectData, UnitTypeData, UpgradeData
from .debug_pb2 import DebugCommand
from .query_pb2 import RequestQuery, ResponseQuery
from .raw_pb2 import ActionRaw, ObservationRaw, StartRaw
from .score_pb2 import Score
from .ui_pb2 import ActionUI, ObservationUI

class Request(Message):
    create_game: RequestCreateGame
    join_game: RequestJoinGame
    restart_game: RequestRestartGame
    start_replay: RequestStartReplay
    leave_game: RequestLeaveGame
    quick_save: RequestQuickSave
    quick_load: RequestQuickLoad
    quit: RequestQuit
    game_info: RequestGameInfo
    observation: RequestObservation
    action: RequestAction
    obs_action: RequestObserverAction
    step: RequestStep
    data: RequestData
    query: RequestQuery
    save_replay: RequestSaveReplay
    map_command: RequestMapCommand
    replay_info: RequestReplayInfo
    available_maps: RequestAvailableMaps
    save_map: RequestSaveMap
    ping: RequestPing
    debug: RequestDebug
    id: int
    def __init__(
        self,
        create_game: RequestCreateGame = ...,
        join_game: RequestJoinGame = ...,
        restart_game: RequestRestartGame = ...,
        start_replay: RequestStartReplay = ...,
        leave_game: RequestLeaveGame = ...,
        quick_save: RequestQuickSave = ...,
        quick_load: RequestQuickLoad = ...,
        quit: RequestQuit = ...,
        game_info: RequestGameInfo = ...,
        observation: RequestObservation = ...,
        action: RequestAction = ...,
        obs_action: RequestObserverAction = ...,
        step: RequestStep = ...,
        data: RequestData = ...,
        query: RequestQuery = ...,
        save_replay: RequestSaveReplay = ...,
        map_command: RequestMapCommand = ...,
        replay_info: RequestReplayInfo = ...,
        available_maps: RequestAvailableMaps = ...,
        save_map: RequestSaveMap = ...,
        ping: RequestPing = ...,
        debug: RequestDebug = ...,
        id: int = ...,
    ) -> None: ...

class Response(Message):
    create_game: ResponseCreateGame
    join_game: ResponseJoinGame
    restart_game: ResponseRestartGame
    start_replay: ResponseStartReplay
    leave_game: ResponseLeaveGame
    quick_save: ResponseQuickSave
    quick_load: ResponseQuickLoad
    quit: ResponseQuit
    game_info: ResponseGameInfo
    observation: ResponseObservation
    action: ResponseAction
    obs_action: ResponseObserverAction
    step: ResponseStep
    data: ResponseData
    query: ResponseQuery
    save_replay: ResponseSaveReplay
    replay_info: ResponseReplayInfo
    available_maps: ResponseAvailableMaps
    save_map: ResponseSaveMap
    map_command: ResponseMapCommand
    ping: ResponsePing
    debug: ResponseDebug
    id: int
    error: Iterable[str]
    status: int
    def __init__(
        self,
        create_game: ResponseCreateGame = ...,
        join_game: ResponseJoinGame = ...,
        restart_game: ResponseRestartGame = ...,
        start_replay: ResponseStartReplay = ...,
        leave_game: ResponseLeaveGame = ...,
        quick_save: ResponseQuickSave = ...,
        quick_load: ResponseQuickLoad = ...,
        quit: ResponseQuit = ...,
        game_info: ResponseGameInfo = ...,
        observation: ResponseObservation = ...,
        action: ResponseAction = ...,
        obs_action: ResponseObserverAction = ...,
        step: ResponseStep = ...,
        data: ResponseData = ...,
        query: ResponseQuery = ...,
        save_replay: ResponseSaveReplay = ...,
        replay_info: ResponseReplayInfo = ...,
        available_maps: ResponseAvailableMaps = ...,
        save_map: ResponseSaveMap = ...,
        map_command: ResponseMapCommand = ...,
        ping: ResponsePing = ...,
        debug: ResponseDebug = ...,
        id: int = ...,
        error: Iterable[str] = ...,
        status: int = ...,
    ) -> None: ...

class Status(Enum):
    launched: int
    init_game: int
    in_game: int
    in_replay: int
    ended: int
    quit: int
    unknown: int

class RequestCreateGame(Message):
    local_map: LocalMap
    battlenet_map_name: str
    player_setup: Iterable[PlayerSetup]
    disable_fog: bool
    random_seed: int
    realtime: bool
    def __init__(
        self,
        local_map: LocalMap = ...,
        battlenet_map_name: str = ...,
        player_setup: Iterable[PlayerSetup] = ...,
        disable_fog: bool = ...,
        random_seed: int = ...,
        realtime: bool = ...,
    ) -> None: ...

class LocalMap(Message):
    map_path: str
    map_data: bytes
    def __init__(self, map_path: str = ..., map_data: bytes = ...) -> None: ...

class ResponseCreateGame(Message):
    class Error(Enum):
        MissingMap: int
        InvalidMapPath: int
        InvalidMapData: int
        InvalidMapName: int
        InvalidMapHandle: int
        MissingPlayerSetup: int
        InvalidPlayerSetup: int
        MultiplayerUnsupported: int

    error: int
    error_details: str
    def __init__(self, error: int = ..., error_details: str = ...) -> None: ...

class RequestJoinGame(Message):
    race: int
    observed_player_id: int
    options: InterfaceOptions
    server_ports: PortSet
    client_ports: Iterable[PortSet]
    shared_port: int
    player_name: str
    host_ip: str
    def __init__(
        self,
        race: int = ...,
        observed_player_id: int = ...,
        options: InterfaceOptions = ...,
        server_ports: PortSet = ...,
        client_ports: Iterable[PortSet] = ...,
        shared_port: int = ...,
        player_name: str = ...,
        host_ip: str = ...,
    ) -> None: ...

class PortSet(Message):
    game_port: int
    base_port: int
    def __init__(self, game_port: int = ..., base_port: int = ...) -> None: ...

class ResponseJoinGame(Message):
    class Error(Enum):
        MissingParticipation: int
        InvalidObservedPlayerId: int
        MissingOptions: int
        MissingPorts: int
        GameFull: int
        LaunchError: int
        FeatureUnsupported: int
        NoSpaceForUser: int
        MapDoesNotExist: int
        CannotOpenMap: int
        ChecksumError: int
        NetworkError: int
        OtherError: int

    player_id: int
    error: int
    error_details: str
    def __init__(self, player_id: int = ..., error: int = ..., error_details: str = ...) -> None: ...

class RequestRestartGame(Message):
    def __init__(self) -> None: ...

class ResponseRestartGame(Message):
    class Error(Enum):
        LaunchError: int

    error: int
    error_details: str
    need_hard_reset: bool
    def __init__(self, error: int = ..., error_details: str = ..., need_hard_reset: bool = ...) -> None: ...

class RequestStartReplay(Message):
    replay_path: str
    replay_data: bytes
    map_data: bytes
    observed_player_id: int
    options: InterfaceOptions
    disable_fog: bool
    realtime: bool
    record_replay: bool
    def __init__(
        self,
        replay_path: str = ...,
        replay_data: bytes = ...,
        map_data: bytes = ...,
        observed_player_id: int = ...,
        options: InterfaceOptions = ...,
        disable_fog: bool = ...,
        realtime: bool = ...,
        record_replay: bool = ...,
    ) -> None: ...

class ResponseStartReplay(Message):
    class Error(Enum):
        MissingReplay: int
        InvalidReplayPath: int
        InvalidReplayData: int
        InvalidMapData: int
        InvalidObservedPlayerId: int
        MissingOptions: int
        LaunchError: int

    error: int
    error_details: str
    def __init__(self, error: int = ..., error_details: str = ...) -> None: ...

class RequestMapCommand(Message):
    trigger_cmd: str
    def __init__(self, trigger_cmd: str = ...) -> None: ...

class ResponseMapCommand(Message):
    class Error(Enum):
        NoTriggerError: int

    error: int
    error_details: str
    def __init__(self, error: int = ..., error_details: str = ...) -> None: ...

class RequestLeaveGame(Message):
    def __init__(self) -> None: ...

class ResponseLeaveGame(Message):
    def __init__(self) -> None: ...

class RequestQuickSave(Message):
    def __init__(self) -> None: ...

class ResponseQuickSave(Message):
    def __init__(self) -> None: ...

class RequestQuickLoad(Message):
    def __init__(self) -> None: ...

class ResponseQuickLoad(Message):
    def __init__(self) -> None: ...

class RequestQuit(Message):
    def __init__(self) -> None: ...

class ResponseQuit(Message):
    def __init__(self) -> None: ...

class RequestGameInfo(Message):
    def __init__(self) -> None: ...

class ResponseGameInfo(Message):
    map_name: str
    mod_names: Iterable[str]
    local_map_path: str
    player_info: Iterable[PlayerInfo]
    start_raw: StartRaw
    options: InterfaceOptions
    def __init__(
        self,
        map_name: str = ...,
        mod_names: Iterable[str] = ...,
        local_map_path: str = ...,
        player_info: Iterable[PlayerInfo] = ...,
        start_raw: StartRaw = ...,
        options: InterfaceOptions = ...,
    ) -> None: ...

class RequestObservation(Message):
    disable_fog: bool
    game_loop: int
    def __init__(self, disable_fog: bool = ..., game_loop: int = ...) -> None: ...

class ResponseObservation(Message):
    actions: Iterable[Action]
    action_errors: Iterable[ActionError]
    observation: Observation
    player_result: Iterable[PlayerResult]
    chat: Iterable[ChatReceived]
    def __init__(
        self,
        actions: Iterable[Action] = ...,
        action_errors: Iterable[ActionError] = ...,
        observation: Observation = ...,
        player_result: Iterable[PlayerResult] = ...,
        chat: Iterable[ChatReceived] = ...,
    ) -> None: ...

class ChatReceived(Message):
    player_id: int
    message: str
    def __init__(self, player_id: int = ..., message: str = ...) -> None: ...

class RequestAction(Message):
    actions: Iterable[Action]
    def __init__(self, actions: Iterable[Action] = ...) -> None: ...

class ResponseAction(Message):
    result: Iterable[int]
    def __init__(self, result: Iterable[int] = ...) -> None: ...

class RequestObserverAction(Message):
    actions: Iterable[ObserverAction]
    def __init__(self, actions: Iterable[ObserverAction] = ...) -> None: ...

class ResponseObserverAction(Message):
    def __init__(self) -> None: ...

class RequestStep(Message):
    count: int
    def __init__(self, count: int = ...) -> None: ...

class ResponseStep(Message):
    simulation_loop: int
    def __init__(self, simulation_loop: int = ...) -> None: ...

class RequestData(Message):
    ability_id: bool
    unit_type_id: bool
    upgrade_id: bool
    buff_id: bool
    effect_id: bool
    def __init__(
        self,
        ability_id: bool = ...,
        unit_type_id: bool = ...,
        upgrade_id: bool = ...,
        buff_id: bool = ...,
        effect_id: bool = ...,
    ) -> None: ...

class ResponseData(Message):
    abilities: Iterable[AbilityData]
    units: Iterable[UnitTypeData]
    upgrades: Iterable[UpgradeData]
    buffs: Iterable[BuffData]
    effects: Iterable[EffectData]
    def __init__(
        self,
        abilities: Iterable[AbilityData] = ...,
        units: Iterable[UnitTypeData] = ...,
        upgrades: Iterable[UpgradeData] = ...,
        buffs: Iterable[BuffData] = ...,
        effects: Iterable[EffectData] = ...,
    ) -> None: ...

class RequestSaveReplay(Message):
    def __init__(self) -> None: ...

class ResponseSaveReplay(Message):
    data: bytes
    def __init__(self, data: bytes = ...) -> None: ...

class RequestReplayInfo(Message):
    replay_path: str
    replay_data: bytes
    download_data: bool
    def __init__(
        self,
        replay_path: str = ...,
        replay_data: bytes = ...,
        download_data: bool = ...,
    ) -> None: ...

class PlayerInfoExtra(Message):
    player_info: PlayerInfo
    player_result: PlayerResult
    player_mmr: int
    player_apm: int
    def __init__(
        self,
        player_info: PlayerInfo = ...,
        player_result: PlayerResult = ...,
        player_mmr: int = ...,
        player_apm: int = ...,
    ) -> None: ...

class ResponseReplayInfo(Message):
    class Error(Enum):
        MissingReplay: int
        InvalidReplayPath: int
        InvalidReplayData: int
        ParsingError: int
        DownloadError: int

    map_name: str
    local_map_path: str
    player_info: Iterable[PlayerInfoExtra]
    game_duration_loops: int
    game_duration_seconds: float
    game_version: str
    data_version: str
    data_build: int
    base_build: int
    error: int
    error_details: str
    def __init__(
        self,
        map_name: str = ...,
        local_map_path: str = ...,
        player_info: Iterable[PlayerInfoExtra] = ...,
        game_duration_loops: int = ...,
        game_duration_seconds: float = ...,
        game_version: str = ...,
        data_version: str = ...,
        data_build: int = ...,
        base_build: int = ...,
        error: int = ...,
        error_details: str = ...,
    ) -> None: ...

class RequestAvailableMaps(Message):
    def __init__(self) -> None: ...

class ResponseAvailableMaps(Message):
    local_map_paths: Iterable[str]
    battlenet_map_names: Iterable[str]
    def __init__(self, local_map_paths: Iterable[str] = ..., battlenet_map_names: Iterable[str] = ...) -> None: ...

class RequestSaveMap(Message):
    map_path: str
    map_data: bytes
    def __init__(self, map_path: str = ..., map_data: bytes = ...) -> None: ...

class ResponseSaveMap(Message):
    class Error(Enum):
        InvalidMapData: int

    error: int
    def __init__(self, error: int = ...) -> None: ...

class RequestPing(Message):
    def __init__(self) -> None: ...

class ResponsePing(Message):
    game_version: str
    data_version: str
    data_build: int
    base_build: int
    def __init__(
        self,
        game_version: str = ...,
        data_version: str = ...,
        data_build: int = ...,
        base_build: int = ...,
    ) -> None: ...

class RequestDebug(Message):
    debug: Iterable[DebugCommand]
    def __init__(self, debug: Iterable[DebugCommand] = ...) -> None: ...

class ResponseDebug(Message):
    def __init__(self) -> None: ...

class Difficulty(Enum):
    VeryEasy: int
    Easy: int
    Medium: int
    MediumHard: int
    Hard: int
    Harder: int
    VeryHard: int
    CheatVision: int
    CheatMoney: int
    CheatInsane: int

class PlayerType(Enum):
    Participant: int
    Computer: int
    Observer: int

class AIBuild(Enum):
    RandomBuild: int
    Rush: int
    Timing: int
    Power: int
    Macro: int
    Air: int

class PlayerSetup(Message):
    type: int
    race: int
    difficulty: int
    player_name: str
    ai_build: int
    def __init__(
        self,
        type: int = ...,
        race: int = ...,
        difficulty: int = ...,
        player_name: str = ...,
        ai_build: int = ...,
    ) -> None: ...

class SpatialCameraSetup(Message):
    resolution: Size2DI
    minimap_resolution: Size2DI
    width: float
    crop_to_playable_area: bool
    allow_cheating_layers: bool
    def __init__(
        self,
        resolution: Size2DI = ...,
        minimap_resolution: Size2DI = ...,
        width: float = ...,
        crop_to_playable_area: bool = ...,
        allow_cheating_layers: bool = ...,
    ) -> None: ...

class InterfaceOptions(Message):
    raw: bool
    score: bool
    feature_layer: SpatialCameraSetup
    render: SpatialCameraSetup
    show_cloaked: bool
    show_burrowed_shadows: bool
    show_placeholders: bool
    raw_affects_selection: bool
    raw_crop_to_playable_area: bool
    def __init__(
        self,
        raw: bool = ...,
        score: bool = ...,
        feature_layer: SpatialCameraSetup = ...,
        render: SpatialCameraSetup = ...,
        show_cloaked: bool = ...,
        show_burrowed_shadows: bool = ...,
        show_placeholders: bool = ...,
        raw_affects_selection: bool = ...,
        raw_crop_to_playable_area: bool = ...,
    ) -> None: ...

class PlayerInfo(Message):
    player_id: int
    type: int
    race_requested: int
    race_actual: int
    difficulty: int
    ai_build: int
    player_name: str
    def __init__(
        self,
        player_id: int = ...,
        type: int = ...,
        race_requested: int = ...,
        race_actual: int = ...,
        difficulty: int = ...,
        ai_build: int = ...,
        player_name: str = ...,
    ) -> None: ...

class PlayerCommon(Message):
    player_id: int
    minerals: int
    vespene: int
    food_cap: int
    food_used: int
    food_army: int
    food_workers: int
    idle_worker_count: int
    army_count: int
    warp_gate_count: int
    larva_count: int
    def __init__(
        self,
        player_id: int = ...,
        minerals: int = ...,
        vespene: int = ...,
        food_cap: int = ...,
        food_used: int = ...,
        food_army: int = ...,
        food_workers: int = ...,
        idle_worker_count: int = ...,
        army_count: int = ...,
        warp_gate_count: int = ...,
        larva_count: int = ...,
    ) -> None: ...

class Observation(Message):
    game_loop: int
    player_common: PlayerCommon
    alerts: Iterable[int]
    abilities: Iterable[AvailableAbility]
    score: Score
    raw_data: ObservationRaw
    feature_layer_data: ObservationFeatureLayer
    render_data: ObservationRender
    ui_data: ObservationUI
    def __init__(
        self,
        game_loop: int = ...,
        player_common: PlayerCommon = ...,
        alerts: Iterable[int] = ...,
        abilities: Iterable[AvailableAbility] = ...,
        score: Score = ...,
        raw_data: ObservationRaw = ...,
        feature_layer_data: ObservationFeatureLayer = ...,
        render_data: ObservationRender = ...,
        ui_data: ObservationUI = ...,
    ) -> None: ...

class Action(Message):
    action_raw: ActionRaw
    action_feature_layer: ActionSpatial
    action_render: ActionSpatial
    action_ui: ActionUI
    action_chat: ActionChat
    game_loop: int
    def __init__(
        self,
        action_raw: ActionRaw = ...,
        action_feature_layer: ActionSpatial = ...,
        action_render: ActionSpatial = ...,
        action_ui: ActionUI = ...,
        action_chat: ActionChat = ...,
        game_loop: int = ...,
    ) -> None: ...

class Channel(Enum):
    Broadcast: int
    Team: int

class ActionChat(Message):
    channel: int
    message: str
    def __init__(self, channel: int = ..., message: str = ...) -> None: ...

class ActionError(Message):
    unit_tag: int
    ability_id: int
    result: int
    def __init__(self, unit_tag: int = ..., ability_id: int = ..., result: int = ...) -> None: ...

class ObserverAction(Message):
    player_perspective: ActionObserverPlayerPerspective
    camera_move: ActionObserverCameraMove
    camera_follow_player: ActionObserverCameraFollowPlayer
    camera_follow_units: ActionObserverCameraFollowUnits
    def __init__(
        self,
        player_perspective: ActionObserverPlayerPerspective = ...,
        camera_move: ActionObserverCameraMove = ...,
        camera_follow_player: ActionObserverCameraFollowPlayer = ...,
        camera_follow_units: ActionObserverCameraFollowUnits = ...,
    ) -> None: ...

class ActionObserverPlayerPerspective(Message):
    player_id: int
    def __init__(self, player_id: int = ...) -> None: ...

class ActionObserverCameraMove(Message):
    world_pos: Point2D
    distance: float
    def __init__(self, world_pos: Point2D = ..., distance: float = ...) -> None: ...

class ActionObserverCameraFollowPlayer(Message):
    player_id: int
    def __init__(self, player_id: int = ...) -> None: ...

class ActionObserverCameraFollowUnits(Message):
    unit_tags: Iterable[int]
    def __init__(self, unit_tags: Iterable[int] = ...) -> None: ...

class Alert(Enum):
    AlertError: int
    AddOnComplete: int
    BuildingComplete: int
    BuildingUnderAttack: int
    LarvaHatched: int
    MergeComplete: int
    MineralsExhausted: int
    MorphComplete: int
    MothershipComplete: int
    MULEExpired: int
    NuclearLaunchDetected: int
    NukeComplete: int
    NydusWormDetected: int
    ResearchComplete: int
    TrainError: int
    TrainUnitComplete: int
    TrainWorkerComplete: int
    TransformationComplete: int
    UnitUnderAttack: int
    UpgradeComplete: int
    VespeneExhausted: int
    WarpInComplete: int

class Result(Enum):
    Victory: int
    Defeat: int
    Tie: int
    Undecided: int

class PlayerResult(Message):
    player_id: int
    result: int
    def __init__(self, player_id: int = ..., result: int = ...) -> None: ...
