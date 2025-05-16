import duckdb

con = duckdb.connect('data/edwards_stats.duckdb')

# Run a simple query to check if data exists
results = con.execute("SELECT * FROM edwards_game_logs LIMIT 5").fetchdf()

print(results)

con.close()
