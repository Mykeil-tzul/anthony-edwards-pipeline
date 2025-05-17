import requests
import pandas as pd
import time

def fetch_anthony_edwards_stats():
    url = "https://stats.nba.com/stats/playergamelog"
    params = {
        "PlayerID": "1630162",  # Anthony Edwards
        "Season": "2024-25",
        "SeasonType": "Regular Season",
        "MeasureType": "Base",
        "PerMode": "PerGame"
    }
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://www.nba.com/"
    }

    retries = 5
    delay = 5
    for attempt in range(retries):
        try:
            response = requests.get(url, headers=headers, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            df = pd.DataFrame(data["resultSets"][0]["rowSet"], columns=data["resultSets"][0]["headers"])
            df.to_csv("data/raw_stats.csv", index=False)
            print("✅ Data fetched and saved")
            return
        except requests.exceptions.RequestException as e:
            print(f"⚠️ Attempt {attempt + 1} failed: {e}")
            time.sleep(delay)
    
    raise Exception("❌ Failed to fetch data after retries")
