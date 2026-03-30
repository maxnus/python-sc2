from examples.zerg.zerg_rush import ZergRushBot
from sc2 import maps
from sc2.data import Race
from sc2.main import _host_game_iter
from sc2.player import Bot
from sc2.portconfig import Portconfig


def main():
    portconfig: Portconfig = Portconfig()
    print(portconfig.as_json)

    # pyrefly: ignore
    player_config = [Bot(Race.Zerg, ZergRushBot()), Bot(Race.Zerg, None)]

    for g in _host_game_iter(maps.get("Abyssal Reef LE"), player_config, realtime=False, portconfig=portconfig):
        print(g)


if __name__ == "__main__":
    main()
