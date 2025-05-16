import pandas as pd

def clean_stats(filepath='data/raw_stats.csv'):
    df = pd.read_csv(filepath)
    df.columns = [col.lower() for col in df.columns]
    df = df[['game_date', 'matchup', 'pts', 'reb', 'ast', 'fg3m', 'plus_minus']]
    df['game_date'] = pd.to_datetime(df['game_date'])
    df = df.sort_values(by='game_date', ascending=True)
    df.to_csv('data/clean_stats.csv', index=False)
    return df
