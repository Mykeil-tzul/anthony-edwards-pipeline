import duckdb
import pandas as pd

def load_to_duckdb(filepath='data/clean_stats.csv'):
    con = duckdb.connect('data/edwards_stats.duckdb')
    df = pd.read_csv(filepath)

    con.execute("""
        CREATE TABLE IF NOT EXISTS edwards_game_logs (
            game_date DATE,
            matchup TEXT,
            pts INTEGER,
            reb INTEGER,
            ast INTEGER,
            fg3m INTEGER,
            plus_minus INTEGER
        );
    """)

    con.execute("DELETE FROM edwards_game_logs;")  # reset for dev testing
    con.register('df', df)
    con.execute("INSERT INTO edwards_game_logs SELECT * FROM df;")
    con.close()
