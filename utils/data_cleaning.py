"""
Data cleaning and preprocessing utilities for Paris 2024 Olympic Dashboard
"""
import pandas as pd
import numpy as np
from datetime import datetime


# Comprehensive continent mapping for all NOC codes
CONTINENT_MAPPING = {
    'Africa': ['ALG', 'ANG', 'BDI', 'BEN', 'BOT', 'BUR', 'CAF', 'CGO', 'CHA', 'CIV', 
               'CMR', 'COD', 'COM', 'CPV', 'DJI', 'EGY', 'ERI', 'ETH', 'GAB', 'GAM', 
               'GBS', 'GEQ', 'GHA', 'GUI', 'KEN', 'LBA', 'LBR', 'LES', 'MAD', 'MAR', 
               'MAW', 'MLI', 'MOZ', 'MRI', 'MTN', 'NAM', 'NGR', 'NIG', 'RSA', 'RWA', 
               'SEN', 'SEY', 'SLE', 'SOM', 'SSD', 'STP', 'SUD', 'SWZ', 'TAN', 'TOG', 
               'TUN', 'UGA', 'ZAM', 'ZIM'],
    
    'Asia': ['AFG', 'BAN', 'BHU', 'BRN', 'BRU', 'CAM', 'CHN', 'HKG', 'INA', 'IND', 
             'IRI', 'IRQ', 'JOR', 'JPN', 'KAZ', 'KGZ', 'KOR', 'KSA', 'KUW', 'LAO', 
             'LBN', 'MAS', 'MDV', 'MGL', 'MYA', 'NEP', 'OMA', 'PAK', 'PHI', 'PLE', 
             'PRK', 'QAT', 'SGP', 'SRI', 'SYR', 'THA', 'TJK', 'TKM', 'TPE', 'UAE', 
             'UZB', 'VIE', 'YEM'],
    
    'Europe': ['ALB', 'AND', 'ARM', 'AUT', 'AZE', 'BEL', 'BIH', 'BUL', 'BLR', 'CRO', 
               'CYP', 'CZE', 'DEN', 'ESP', 'EST', 'FIN', 'FRA', 'GBR', 'GEO', 'GER', 
               'GRE', 'HUN', 'IRL', 'ISL', 'ISR', 'ITA', 'KOS', 'LAT', 'LIE', 'LTU', 
               'LUX', 'MDA', 'MKD', 'MLT', 'MON', 'MNE', 'NED', 'NOR', 'POL', 'POR', 
               'ROU', 'SRB', 'SMR', 'SLO', 'SVK', 'SUI', 'SWE', 'TUR', 'UKR', 'RUS', 
               'AIN'],
    
    'North America': ['ANT', 'BAH', 'BAR', 'BER', 'BIZ', 'CAN', 'CAY', 'CRC', 'CUB', 
                      'DMA', 'DOM', 'ESA', 'GRN', 'GUA', 'GUM', 'HAI', 'HON', 'ISV', 
                      'JAM', 'MEX', 'NCA', 'PAN', 'PUR', 'SKN', 'LCA', 'VIN', 'TTO', 
                      'USA', 'ASA'],
    
    'South America': ['ARG', 'ARU', 'BOL', 'BRA', 'CHI', 'COL', 'ECU', 'GUY', 'PAR', 
                      'PER', 'SUR', 'URU', 'VEN'],
    
    'Oceania': ['AUS', 'COK', 'FIJ', 'FSM', 'KIR', 'MHL', 'NRU', 'NZL', 'PLW', 'PNG', 
                'SAM', 'SOL', 'TGA', 'TLS', 'TUV', 'VAN'],
    
    'Other': ['EOR', 'ROC', 'OAR', 'AIN']  # Refugee team and special designations
}


def get_continent_mapping_dict():
    """
    Create a dictionary mapping NOC codes to continents
    
    Returns:
        dict: NOC code -> continent mapping
    """
    noc_to_continent = {}
    for continent, noc_codes in CONTINENT_MAPPING.items():
        for noc in noc_codes:
            noc_to_continent[noc] = continent
    return noc_to_continent


def add_continent_to_dataframe(df, noc_column='country_code'):
    """
    Add continent column to a DataFrame based on NOC codes
    
    Args:
        df: DataFrame with NOC codes
        noc_column: Name of the column containing NOC codes
        
    Returns:
        DataFrame with added 'continent' column
    """
    noc_to_continent = get_continent_mapping_dict()
    df = df.copy()
    df['continent'] = df[noc_column].map(noc_to_continent)
    # Fill any missing continents with 'Other'
    df['continent'] = df['continent'].fillna('Other')
    return df


def calculate_age(birth_date_str, reference_date='2024-07-26'):
    """
    Calculate age from birth date string
    
    Args:
        birth_date_str: Birth date as string (YYYY-MM-DD)
        reference_date: Reference date for age calculation (Olympics start date)
        
    Returns:
        int: Age in years, or None if birth date is invalid
    """
    if pd.isna(birth_date_str) or birth_date_str == '':
        return None
    
    try:
        birth_date = pd.to_datetime(birth_date_str)
        ref_date = pd.to_datetime(reference_date)
        age = ref_date.year - birth_date.year
        # Adjust if birthday hasn't occurred yet this year
        if (ref_date.month, ref_date.day) < (birth_date.month, birth_date.day):
            age -= 1
        return age
    except:
        return None


def clean_athletes_data(df):
    """
    Clean athletes data: handle missing values, calculate ages, add continents
    
    Args:
        df: Raw athletes DataFrame
        
    Returns:
        Cleaned DataFrame
    """
    df = df.copy()
    
    # Convert height and weight to numeric, replacing 0.0 with NaN
    df['height'] = pd.to_numeric(df['height'], errors='coerce')
    df['weight'] = pd.to_numeric(df['weight'], errors='coerce')
    df.loc[df['height'] == 0.0, 'height'] = np.nan
    df.loc[df['weight'] == 0.0, 'weight'] = np.nan
    
    # Calculate ages
    df['age'] = df['birth_date'].apply(calculate_age)
    
    # Add continent
    df = add_continent_to_dataframe(df, 'country_code')
    
    # Parse disciplines from string representation of list
    # Parse disciplines from string representation of list
    def safe_parse_list(x):
        try:
            if pd.isna(x):
                return []
            return eval(x)
        except:
            return []
            
    df['disciplines'] = df['disciplines'].apply(safe_parse_list)
    
    return df


def clean_medals_data(df):
    """
    Clean medals data: standardize medal types, add continents
    
    Args:
        df: Raw medals DataFrame
        
    Returns:
        Cleaned DataFrame
    """
    df = df.copy()
    
    # Standardize medal type names if needed
    if 'medal_type' in df.columns:
        df['medal_type'] = df['medal_type'].str.title()
        
    # Convert medal_date to datetime
    if 'medal_date' in df.columns:
        df['medal_date'] = pd.to_datetime(df['medal_date'], errors='coerce')
    
    # Add continent
    if 'country_code' in df.columns:
        df = add_continent_to_dataframe(df, 'country_code')
    
    return df


def clean_medals_total_data(df):
    """
    Clean medals total data: add continents, ensure numeric types
    
    Args:
        df: Raw medals total DataFrame
        
    Returns:
        Cleaned DataFrame
    """
    df = df.copy()
    
    # Ensure medal counts are numeric
    for col in ['Gold Medal', 'Silver Medal', 'Bronze Medal', 'Total']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)
    
    # Add continent
    df = add_continent_to_dataframe(df, 'country_code')
    
    return df


def clean_venues_data(df):
    """
    Clean venues data: validate dates and coordinates
    
    Args:
        df: Raw venues DataFrame
        
    Returns:
        Cleaned DataFrame
    """
    df = df.copy()
    
    # Convert dates to datetime
    if 'date_start' in df.columns:
        df['date_start'] = pd.to_datetime(df['date_start'], errors='coerce')
    if 'date_end' in df.columns:
        df['date_end'] = pd.to_datetime(df['date_end'], errors='coerce')
    
    # Parse sports list from string
    if 'sports' in df.columns:
        try:
            df['sports'] = df['sports'].apply(eval)
        except:
            pass
    
    return df


def preprocess_coaches_data(df):
    """
    Preprocess coaches data for joining with athletes
    
    Args:
        df: Raw coaches DataFrame
        
    Returns:
        Cleaned DataFrame
    """
    df = df.copy()
    
    # Add continent
    if 'country_code' in df.columns:
        df = add_continent_to_dataframe(df, 'country_code')
    
    return df


def merge_athlete_with_coach(athletes_df, coaches_df=None, teams_df=None):
    """
    Merge athletes with their coaches
    
    Args:
        athletes_df: Athletes DataFrame
        coaches_df: Coaches DataFrame (optional)
        teams_df: Teams DataFrame (optional)
        
    Returns:
        DataFrame with coach information added
    """
    # This is a simplified version - actual implementation would need
    # more complex logic to match athletes with coaches
    return athletes_df
