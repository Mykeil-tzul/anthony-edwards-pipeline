import pandas as pd

def clean_stats(filepath='data/raw_stats.csv'):
    df = pd.read_csv(filepath)

    # Standardize column names
    df.columns = [col.lower() for col in df.columns]

    # Select relevant columns
    df = df[['game_date', 'matchup', 'pts', 'reb', 'ast', 'fg3m', 'plus_minus']]
    
    # Parse game date
    df['game_date'] = pd.to_datetime(df['game_date'])

    # Sort by date (earliest to latest)
    df = df.sort_values(by='game_date', ascending=True)

    # Add 5-game rolling averages
    df['pts_rolling'] = df['pts'].rolling(window=5).mean()
    df['ast_rolling'] = df['ast'].rolling(window=5).mean()
    df['reb_rolling'] = df['reb'].rolling(window=5).mean()

    # Save cleaned and enriched data
    df.to_csv('data/clean_stats.csv', index=False)
    
    return df

