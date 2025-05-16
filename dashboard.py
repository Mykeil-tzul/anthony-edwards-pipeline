import streamlit as st
import duckdb
import pandas as pd

# Connect to DuckDB and read the cleaned data
con = duckdb.connect('data/edwards_stats.duckdb')
df = con.execute("SELECT * FROM edwards_game_logs ORDER BY game_date DESC").fetchdf()
con.close()

# Title
st.title("🏀 Anthony Edwards Real-Time Game Log")

st.markdown("""
Track Anthony Edwards' performance game-by-game with rolling averages, opponent breakdowns, and high-scoring filters.
Data is updated using a real-time NBA data pipeline built with Python, DuckDB, and Streamlit.
""")

# Show full game log
st.subheader("📋 Full Game Log")
st.dataframe(df)

# Rolling averages line chart
st.subheader("📈 5-Game Rolling Averages (PTS, AST, REB)")
st.line_chart(df.set_index('game_date')[['pts_rolling', 'ast_rolling', 'reb_rolling']])

# Performance by opponent
st.subheader("📊 Average Performance by Opponent")
opponent_summary = df.groupby('matchup')[['pts', 'reb', 'ast']].mean().sort_values(by='pts', ascending=False)
st.dataframe(opponent_summary.style.format("{:.1f}"))

# Filter by minimum points scored
st.subheader("🔍 Filter Games by Points Scored")
min_points = st.slider("Show games with at least this many points:", 10, 50, 25)
filtered_df = df[df['pts'] >= min_points]
st.dataframe(filtered_df)

# Footer
st.caption("Built by Mykeil Tzul | Streamlit + DuckDB + nba_api")

