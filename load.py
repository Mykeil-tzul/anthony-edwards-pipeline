import duckdb
import pandas as pd

def load_to_duckdb(filepath='data/clean_stats.csv'):
    con = duckdb.connect('data/edwards_stats.duckdb')

    # Read the cleaned CSV
    df = pd.read_csv(filepath)

    # Drop and recreate the table with all expected columns
    con.execute("DROP TABLE IF EXISTS edwards_game_logs;")

    con.execute("""
        CREATE TABLE edwards_game_logs (
            game_date DATE,
            matchup TEXT,
            pts INTEGER,
            reb INTEGER,
            ast INTEGER,
            fg3m INTEGER,
            plus_minus INTEGER,
            pts_rolling DOUBLE,
            ast_rolling DOUBLE,
            reb_rolling DOUBLE
        );
    """)

    con.register('df', df)
    con.execute("INSERT INTO edwards_game_logs SELECT * FROM df;")
    con.close()


