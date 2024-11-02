import pandas as pd
import os

def load_data():
    file_path = "data/processed/bikes_completed.csv"
    print("Current working directory:", os.getcwd())
    print("File exists:", os.path.exists(file_path))
    
    try:
        df = pd.read_csv(file_path)
        if df.empty:
            print("Warning: The DataFrame is empty.")
        else:
            print("File loaded successfully.")
        return df
    except FileNotFoundError:
        print("Error: The file 'data/processed/bikes_completed.csv' was not found.")
        return None
    except Exception as e:
        print(f"Error loading the file: {e}")
        return None
