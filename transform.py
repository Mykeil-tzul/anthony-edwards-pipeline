import pandas as pd

def clean_stats(filepath='data/anthony_edwards_gamelog.csv'):
    # Load the raw game log CSV
    df = pd.read_csv(filepath)

    # Keep only relevant columns and rename them
    df = df[['GAME_DATE', 'MATCHUP', 'PTS', 'REB', 'AST', 'FG3M', 'PLUS_MINUS']]
    df.columns = ['game_date', 'matchup', 'pts', 'reb', 'ast', 'fg3m', 'plus_minus']

    # Convert game_date to datetime format
    df['game_date'] = pd.to_datetime(df['game_date'])

    # Sort by date so rolling averages are correct
    df = df.sort_values(by='game_date', ascending=True)

    # Add 5-game rolling averages for key stats
    df['pts_rolling'] = df['pts'].rolling(window=5).mean()
    df['ast_rolling'] = df['ast'].rolling(window=5).mean()
    df['reb_rolling'] = df['reb'].rolling(window=5).mean()

    # Save the cleaned dataset
    df.to_csv('data/clean_stats.csv', index=False)

    return df

