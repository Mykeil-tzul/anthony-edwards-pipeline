from nba_api.stats.endpoints import playergamelog
from nba_api.stats.static import players
import pandas as pd
import time
import random
from requests.exceptions import ReadTimeout

def fetch_anthony_edwards_stats(output_path='data/raw_stats.csv'):
    anthony = [p for p in players.get_players() if p['full_name'] == 'Anthony Edwards'][0]
    player_id = anthony['id']

    success = False
    retries = 3
    for attempt in range(retries):
        try:
            print(f"Fetching stats for Anthony Edwards (attempt {attempt+1})...")
            gamelog = playergamelog.PlayerGameLog(player_id=player_id, season='2024-25', timeout=60)
            df = gamelog.get_data_frames()[0]
            df.to_csv(output_path, index=False)
            print(f"✅ Saved {len(df)} games to {output_path}")
            success = True
            break
        except ReadTimeout:
            print("⚠️ ReadTimeout hit — retrying in a few seconds...")
            time.sleep(3 + random.random() * 2)

    if not success:
        raise Exception("❌ Failed to fetch data after multiple retries.")
