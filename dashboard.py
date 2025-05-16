import streamlit as st
import duckdb
import pandas as pd

# Connect to DuckDB and fetch data
con = duckdb.connect('data/edwards_stats.duckdb')
df = con.execute("SELECT * FROM edwards_game_logs ORDER BY game_date DESC").fetchdf()
con.close()

# Format title and intro
st.title("🏀 Anthony Edwards Game Performance Tracker")
st.markdown("""
This dashboard highlights Anthony Edwards' NBA season with a focus on **Playoff performance**.
Built using Python, DuckDB, and Streamlit.
""")

# 📋 Full Season Log
st.subheader("📋 All Games (Full Season)")
st.dataframe(df)

# 🏆 Playoff Tracker Section
st.subheader("🏆 Playoff Game Tracker")

# Ensure game_date is datetime
df['game_date'] = pd.to_datetime(df['game_date'])

# Filter playoff games based on month (May = 5, June = 6)
df_playoffs = df[df['game_date'].dt.month.isin([5, 6])]

if not df_playoffs.empty:
    st.markdown("### 🔢 Playoff Averages")
    st.dataframe(df_playoffs[['pts', 'reb', 'ast']].mean().to_frame(name='Average').style.format("{:.1f}"))

    st.markdown("### 🔥 Top Playoff Games")
    st.dataframe(df_playoffs.sort_values(by='pts', ascending=False).head(5))
else:
    st.info("No playoff games found in the dataset yet.")

# 📊 Full Game Log with Scoring Filter
st.subheader("📈 Filter by Points Scored")
min_points = st.slider("Show games with at least this many points:", 10, 50, 25)
filtered_df = df[df['pts'] >= min_points]
st.dataframe(filtered_df)

# Footer
st.caption("Built by Mykeil Tzul • Data Pipeline + Dashboard Project")
