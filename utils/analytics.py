"""
Analytics utility functions for Paris 2024 Olympic Dashboard
"""
import pandas as pd

def calculate_cumulative_medals(medals_df):
    """
    Calculate cumulative medal counts for each country over time.
    
    Args:
        medals_df: Cleaned medals DataFrame with 'medal_date' and 'country' columns
        
    Returns:
        DataFrame with columns: date, country, daily_medals, cumulative_medals
    """
    # Ensure we have the necessary columns
    if 'medal_date' not in medals_df.columns or 'country' not in medals_df.columns:
        return pd.DataFrame()
    
    # Filter out rows with missing dates or countries
    df = medals_df.dropna(subset=['medal_date', 'country']).copy()
    
    # Group by date and country to get daily counts
    daily_counts = df.groupby(['medal_date', 'country']).size().reset_index(name='daily_medals')
    
    # Create a complete date range from min to max date
    min_date = df['medal_date'].min()
    max_date = df['medal_date'].max()
    all_dates = pd.date_range(start=min_date, end=max_date, freq='D')
    
    # Get all unique countries
    countries = df['country'].unique()
    
    # Create a MultiIndex of all combinations of dates and countries
    idx = pd.MultiIndex.from_product([all_dates, countries], names=['medal_date', 'country'])
    
    # Reindex the daily counts to include all dates for all countries, filling missing with 0
    full_df = daily_counts.set_index(['medal_date', 'country']).reindex(idx, fill_value=0).reset_index()
    
    # Calculate cumulative sum for each country
    full_df['cumulative_medals'] = full_df.groupby('country')['daily_medals'].cumsum()
    
    return full_df
