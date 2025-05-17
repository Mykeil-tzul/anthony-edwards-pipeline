import requests
import pandas as pd
import time
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.static import players
from nba_api.stats.library.http import NBAStatsHTTP

# Set proper headers to bypass nba.com bot protection
NBAStatsHTTP.headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.3",
    "Accept-Language": "en-US,en;q=0.9",
    "Origin": "https://www.nba.com",
    "Referer": "https://www.nba.com/"
}

def fetch_anthony_edwards_stats(retries=5, delay=3):
    print("⏳ Fetching Anthony Edwards game logs...")

    # Get Anthony Edwards' player ID
    anthony = players.find_players_by_full_name("Anthony Edwards")[0]
    player_id = anthony["id"]

    attempt = 0
    while attempt < retries:
        try:
            # Fetch regular season and playoff logs
            gamelog = playergamelog.PlayerGameLog(
                player_id=player_id,
                season="2024-25",
                season_type_all_star="Regular Season"
            )
            df = gamelog.get_data_frames()[0]
            print(f"✅ Retrieved {len(df)} regular season games.")

            playoffs = playergamelog.PlayerGameLog(
                player_id=player_id,
                season="2024-25",
                season_type_all_star="Playoffs"
            )
            df_playoffs = playoffs.get_data_frames()[0]
            print(f"✅ Retrieved {len(df_playoffs)} playoff games.")

            # Combine both
            full_df = pd.concat([df, df_playoffs], ignore_index=True)
            full_df.to_csv("data/anthony_edwards_gamelog.csv", index=False)
            print("✅ Game logs saved to data/anthony_edwards_gamelog.csv")
            return full_df

        except requests.exceptions.RequestException as e:
            print(f"⚠️ Attempt {attempt + 1} failed: {e}")
            attempt += 1
            time.sleep(delay)

    raise Exception("❌ Failed to fetch data after retries")

# Local test
if __name__ == "__main__":
    fetch_anthony_edwards_stats()
