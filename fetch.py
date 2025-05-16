from nba_api.stats.endpoints import playergamelog
import pandas as pd

def fetch_anthony_edwards_stats():
    player_id = 1630162  # Anthony Edwards
    gamelog = playergamelog.PlayerGameLog(player_id=player_id, season='2024')
    df = gamelog.get_data_frames()[0]
    df.to_csv('data/raw_stats.csv', index=False)
    return df
