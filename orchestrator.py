from fetch import fetch_anthony_edwards_stats
from transform import clean_stats
from load import load_to_duckdb
import traceback

def run_pipeline():
    try:
        print("Running Anthony Edwards pipeline...")
        fetch_anthony_edwards_stats()
        clean_stats()
        load_to_duckdb()
        print("✅ Pipeline complete.")
    except Exception as e:
        print("❌ Pipeline failed with error:")
        traceback.print_exc()
        exit(1)

if __name__ == "__main__":
    run_pipeline()

