import streamlit as st
import duckdb
import pandas as pd

# Connect to DuckDB
con = duckdb.connect('data/edwards_stats.duckdb')

# Query recent data
df = con.execute("SELECT * FROM edwards_game_logs ORDER BY game_date DESC").fetchdf()

# Title
st.title("Anthony Edwards Game Log")

# Line chart for points, assists, rebounds
st.subheader("Performance Over Time")
st.line_chart(df.set_index('game_date')[['pts', 'reb', 'ast']])

# Table of full logs
st.subheader("Full Game Log")
st.dataframe(df)

con.close()
