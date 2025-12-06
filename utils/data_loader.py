"""
Data loading utilities with caching for Paris 2024 Olympic Dashboard
"""
import streamlit as st
import pandas as pd
from pathlib import Path


@st.cache_data
def load_athletes_data():
    """Load and cache athletes data"""
    return pd.read_csv('athletes.csv')


@st.cache_data
def load_medals_total_data():
    """Load and cache medals total data"""
    return pd.read_csv('medals_total.csv')


@st.cache_data
def load_medals_data():
    """Load and cache medals data"""
    return pd.read_csv('medals.csv')


@st.cache_data
def load_medallists_data():
    """Load and cache medallists data"""
    return pd.read_csv('medallists.csv')


@st.cache_data
def load_nocs_data():
    """Load and cache NOCs data"""
    return pd.read_csv('nocs.csv')


@st.cache_data
def load_events_data():
    """Load and cache events data"""
    return pd.read_csv('events.csv')


@st.cache_data
def load_schedules_data():
    """Load and cache schedules data"""
    return pd.read_csv('schedules.csv')


@st.cache_data
def load_coaches_data():
    """Load and cache coaches data"""
    return pd.read_csv('coaches.csv')


@st.cache_data
def load_venues_data():
    """Load and cache venues data"""
    return pd.read_csv('venues.csv')


@st.cache_data
def load_teams_data():
    """Load and cache teams data"""
    return pd.read_csv('teams.csv')


def load_all_data():
    """
    Load all datasets and return as a dictionary
    
    Returns:
        dict: Dictionary containing all loaded DataFrames
    """
    return {
        'athletes': load_athletes_data(),
        'medals_total': load_medals_total_data(),
        'medals': load_medals_data(),
        'medallists': load_medallists_data(),
        'nocs': load_nocs_data(),
        'events': load_events_data(),
        'schedules': load_schedules_data(),
        'coaches': load_coaches_data(),
        'venues': load_venues_data(),
        'teams': load_teams_data()
    }
