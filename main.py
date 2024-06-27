from utils import *

if __name__ == "__main__":
    proxy = proxy("proxy.json")
    info, hash_map = nba_players_info(proxy)
    playerids_json("player_ids.json", hash_map)
