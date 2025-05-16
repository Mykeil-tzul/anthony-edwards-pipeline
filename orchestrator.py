from fetch import fetch_anthony_edwards_stats
from transform import clean_stats
from load import load_to_duckdb

def run_pipeline():
    print("Running Anthony Edwards pipeline...")
    fetch_anthony_edwards_stats()
    clean_stats()
    load_to_duckdb()
    print("Pipeline complete.")

if __name__ == "__main__":
    run_pipeline()
