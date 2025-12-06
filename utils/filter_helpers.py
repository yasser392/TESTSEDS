"""
Filter helper utilities for Paris 2024 Olympic Dashboard
Creates consistent sidebar filters across all pages
"""
import streamlit as st
import pandas as pd


def create_sidebar_filters(athletes_df, medals_total_df, events_df):
    """
    Create consistent sidebar filters for all pages
    
    Args:
        athletes_df: Athletes DataFrame (with continent column)
        medals_total_df: Medals total DataFrame (with continent column)
        events_df: Events DataFrame
        
    Returns:
        dict: Dictionary of selected filter values
    """
    st.sidebar.header("🎯 Global Filters")
    
    # Get unique values for filters
    all_countries = sorted(athletes_df['country'].dropna().unique())
    all_sports = sorted(events_df['sport'].dropna().unique())
    all_continents = sorted(athletes_df['continent'].dropna().unique())
    
    # Country filter
    selected_countries = st.sidebar.multiselect(
        "🌍 Select Countries",
        options=all_countries,
        default=[],
        help="Filter by specific countries (leave empty for all)"
    )
    
    # Sport filter
    selected_sports = st.sidebar.multiselect(
        "⚽ Select Sports",
        options=all_sports,
        default=[],
        help="Filter by specific sports (leave empty for all)"
    )
    
    # Continent filter (CREATIVITY CHALLENGE)
    selected_continents = st.sidebar.multiselect(
        "🗺️ Select Continents",
        options=all_continents,
        default=[],
        help="Filter by continents (Creativity Filter!)"
    )
    
    # Medal type filter with checkboxes
    st.sidebar.subheader("🏅 Medal Types")
    col1, col2, col3 = st.sidebar.columns(3)
    
    with col1:
        gold_checked = st.checkbox("🥇 Gold", value=True)
    with col2:
        silver_checked = st.checkbox("🥈 Silver", value=True)
    with col3:
        bronze_checked = st.checkbox("🥉 Bronze", value=True)
    
    selected_medal_types = []
    if gold_checked:
        selected_medal_types.append('Gold Medal')
    if silver_checked:
        selected_medal_types.append('Silver Medal')
    if bronze_checked:
        selected_medal_types.append('Bronze Medal')
    
    return {
        'countries': selected_countries,
        'sports': selected_sports,
        'continents': selected_continents,
        'medal_types': selected_medal_types
    }


def apply_filters_to_athletes(df, filters):
    """
    Apply filters to athletes DataFrame
    
    Args:
        df: Athletes DataFrame
        filters: Dictionary of filter values
        
    Returns:
        Filtered DataFrame
    """
    filtered_df = df.copy()
    
    # Apply country filter
    if filters['countries']:
        filtered_df = filtered_df[filtered_df['country'].isin(filters['countries'])]
    
    # Apply continent filter
    if filters['continents']:
        filtered_df = filtered_df[filtered_df['continent'].isin(filters['continents'])]
    
    # Apply sport filter (need to expand disciplines list)
    if filters['sports']:
        # This handles the case where disciplines is a list
        filtered_df = filtered_df[
            filtered_df['disciplines'].apply(
                lambda x: any(sport in str(x) for sport in filters['sports']) if pd.notna(x) else False
            )
        ]
    
    return filtered_df


def apply_filters_to_medals_total(df, filters):
    """
    Apply filters to medals total DataFrame
    
    Args:
        df: Medals total DataFrame
        filters: Dictionary of filter values
        
    Returns:
        Filtered DataFrame
    """
    filtered_df = df.copy()
    
    # Apply country filter
    if filters['countries']:
        filtered_df = filtered_df[filtered_df['country'].isin(filters['countries'])]
    
    # Apply continent filter
    if filters['continents']:
        filtered_df = filtered_df[filtered_df['continent'].isin(filters['continents'])]
    
    # Apply medal type filter
    # Keep only selected medal types in the display
    if filters['medal_types']:
        # Create a copy to avoid modifying original
        result_df = filtered_df.copy()
        
        # Zero out non-selected medal types
        if 'Gold Medal' not in filters['medal_types']:
            result_df['Gold Medal'] = 0
        if 'Silver Medal' not in filters['medal_types']:
            result_df['Silver Medal'] = 0
        if 'Bronze Medal' not in filters['medal_types']:
            result_df['Bronze Medal'] = 0
        
        # Recalculate total
        result_df['Total'] = (
            result_df['Gold Medal'] + 
            result_df['Silver Medal'] + 
            result_df['Bronze Medal']
        )
        
        # Filter out countries with zero medals after filtering
        result_df = result_df[result_df['Total'] > 0]
        
        return result_df
    
    return filtered_df


def apply_filters_to_events(df, filters):
    """
    Apply filters to events DataFrame
    
    Args:
        df: Events DataFrame
        filters: Dictionary of filter values
        
    Returns:
        Filtered DataFrame
    """
    filtered_df = df.copy()
    
    # Apply sport filter
    if filters['sports']:
        filtered_df = filtered_df[filtered_df['sport'].isin(filters['sports'])]
    
    return filtered_df


def get_filtered_datasets(data, filters):
    """
    Apply filters to all datasets
    
    Args:
        data: Dictionary of all DataFrames
        filters: Dictionary of filter values
        
    Returns:
        dict: Dictionary of filtered DataFrames
    """
    return {
        'athletes': apply_filters_to_athletes(data['athletes'], filters),
        'medals_total': apply_filters_to_medals_total(data['medals_total'], filters),
        'events': apply_filters_to_events(data['events'], filters)
    }
