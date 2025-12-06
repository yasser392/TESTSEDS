
import pandas as pd
import numpy as np
from utils.data_loader import load_athletes_data
from utils.data_cleaning import clean_athletes_data

def debug_disciplines():
    print("Loading athletes data...")
    df = load_athletes_data()
    print(f"Original shape: {df.shape}")
    print(f"Original disciplines sample: {df['disciplines'].head().tolist()}")
    
    print("\nCleaning athletes data...")
    cleaned_df = clean_athletes_data(df)
    
    print(f"\nCleaned disciplines sample: {cleaned_df['disciplines'].head().tolist()}")
    print(f"Type of first element: {type(cleaned_df['disciplines'].iloc[0])}")
    
    # Check if any are lists
    is_list = cleaned_df['disciplines'].apply(lambda x: isinstance(x, list))
    print(f"\nNumber of rows where disciplines is a list: {is_list.sum()}")
    print(f"Total rows: {len(cleaned_df)}")
    
    if is_list.sum() == 0:
        print("\nISSUE CONFIRMED: 'disciplines' column was not converted to lists.")
        
        # Try to debug why
        print("\nAttempting row-by-row conversion to find errors:")
        for i, val in enumerate(df['disciplines'].head(20)):
            try:
                eval(val)
                print(f"Row {i}: Success")
            except Exception as e:
                print(f"Row {i}: Failed - Value: {val} - Error: {e}")

if __name__ == "__main__":
    debug_disciplines()
