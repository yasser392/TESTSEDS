"""
🏟️ Sports and Events Page - Paris 2024 Olympic Games Dashboard
Sports, events, schedules and venue analysis
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

from utils.data_loader import load_all_data
from utils.data_cleaning import clean_venues_data
from utils.ultimate_creative_theme import apply_ultimate_creative_theme, create_ultimate_navbar, create_ultimate_header

st.set_page_config(
    page_title="Sports & Events - Paris 2024",
    page_icon="🏟️",
    layout="wide"
)

# Apply Ultimate Creative Theme
apply_ultimate_creative_theme()

# Load data
@st.cache_data
def load_clean_data():
    data = load_all_data()
    from utils.data_cleaning import clean_athletes_data, clean_medals_total_data
    data['athletes'] = clean_athletes_data(data['athletes'])
    data['medals_total'] = clean_medals_total_data(data['medals_total'])
    data['venues'] = clean_venues_data(data['venues'])
    return data

data = load_clean_data()

# Navbar with filters
filters = create_ultimate_navbar(data['athletes'], data['medals_total'], data['events'])

# Page Header
create_ultimate_header("SPORTS & EVENTS", "Competition Schedules & Venue Locations", "🏟️")

# Event Schedule (Gantt Chart)
st.markdown("### 📅 Event Schedule Timeline")

# Filter for sport/venue selection
col1, col2 = st.columns(2)

# Get available columns from schedule
schedule_df = data['schedules'].copy()
available_columns = schedule_df.columns.tolist()

# Determine sport column name (could be 'sport', 'discipline', or similar)
sport_column = None
if 'sport' in available_columns:
    sport_column = 'sport'
elif 'discipline' in available_columns:
    sport_column = 'discipline'
elif 'event' in available_columns:
    sport_column = 'event'

venue_column = 'venue' if 'venue' in available_columns else None

with col1:
    if sport_column and sport_column in schedule_df.columns:
        sport_options = ['All'] + sorted(schedule_df[sport_column].dropna().unique().tolist())
        selected_sport_filter = st.selectbox(
            "Filter by Sport:",
            options=sport_options,
            index=0
        )
    else:
        selected_sport_filter = 'All'
        st.info(f"Sport filter not available. Available columns: {', '.join(available_columns)}")

with col2:
    if venue_column and venue_column in schedule_df.columns:
        venue_options = ['All'] + sorted(schedule_df[venue_column].dropna().unique().tolist())
        selected_venue_filter = st.selectbox(
            "Filter by Venue:",
            options=venue_options,
            index=0
        )
    else:
        selected_venue_filter = 'All'
        st.info("Venue filter not available")

# Apply filters only if columns exist
if selected_sport_filter != 'All' and sport_column:
    schedule_df = schedule_df[schedule_df[sport_column] == selected_sport_filter]

if selected_venue_filter != 'All' and venue_column:
    schedule_df = schedule_df[schedule_df[venue_column] == selected_venue_filter]

if len(schedule_df) > 0 and 'start_date' in schedule_df.columns and 'end_date' in schedule_df.columns:
    # Convert dates
    schedule_df['start_date'] = pd.to_datetime(schedule_df['start_date'], errors='coerce')
    schedule_df['end_date'] = pd.to_datetime(schedule_df['end_date'], errors='coerce')
    
    # Remove rows with invalid dates
    schedule_df = schedule_df.dropna(subset=['start_date', 'end_date'])
    
    if len(schedule_df) > 0:
        # Limit to first 50 events for readability
        schedule_df_limited = schedule_df.head(50)
        
        fig_schedule = px.timeline(
            schedule_df_limited,
            x_start='start_date',
            x_end='end_date',
            y='event' if 'event' in schedule_df_limited.columns else 'sport',
            color='sport' if 'sport' in schedule_df_limited.columns else None,
            title=f"Event Schedule{' - ' + selected_sport_filter if selected_sport_filter != 'All' else ''}"
        )
        
        fig_schedule.update_layout(
            height=600,
            showlegend=True,
            xaxis_title="Date",
            yaxis_title="Event"
        )
        
        st.plotly_chart(fig_schedule, width="stretch")
        
        if len(schedule_df) > 50:
            st.info(f"Showing first 50 of {len(schedule_df)} events. Use filters to narrow down the view.")
    else:
        st.info("No valid schedule data available for the selected filters")
else:
    st.info("Schedule data not available or missing date information")

st.markdown("---")

# Medal Count by Sport (Treemap)
st.markdown("### 🏅 Medal Count by Sport")

if len(data['medallists']) > 0:
    # Count medals by sport
    sport_medals = data['medallists'].groupby('discipline').size().reset_index(name='medal_count')
    sport_medals = sport_medals.sort_values('medal_count', ascending=False)
    
    # Apply sport filter if needed
    if filters['sports']:
        sport_medals = sport_medals[sport_medals['discipline'].isin(filters['sports'])]
    
    if len(sport_medals) > 0:
        fig_treemap = px.treemap(
            sport_medals,
            path=['discipline'],
            values='medal_count',
            title="Medal Distribution by Sport",
            color='medal_count',
            color_continuous_scale='Purpor'
        )
        
        fig_treemap.update_layout(height=500)
        st.plotly_chart(fig_treemap, width="stretch")
    else:
        st.info("No data available for selected sports")
else:
    st.info("Medal data not available")

st.markdown("---")

# Events by Sport
st.markdown("### 📋 Events by Sport")

if len(data['events']) > 0:
    # Get list of sports
    sports_list = sorted(data['events']['sport'].unique().tolist())
    
    # Sport selection
    selected_sport_events = st.selectbox("Select a Sport to view events:", sports_list)
    
    if selected_sport_events:
        # Filter events
        events_df = data['events'][data['events']['sport'] == selected_sport_events].copy()
        
        # Display events table
        st.dataframe(
            events_df[['event', 'sport_code', 'sport_url']],
            column_config={
                "event": "Event Name",
                "sport_code": "Sport Code",
                "sport_url": st.column_config.LinkColumn("Official Link")
            },
            use_container_width=True,
            hide_index=True
        )
        
        # Download button for selected sport
        csv_sport = events_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label=f"📥 Download {selected_sport_events} Events",
            data=csv_sport,
            file_name=f'paris_2024_events_{selected_sport_events.lower().replace(" ", "_")}.csv',
            mime='text/csv',
        )

    # Option to download all events
    with st.expander("📥 Download All Events Data"):
        csv_all = data['events'].to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Complete Events Dataset",
            data=csv_all,
            file_name='paris_2024_all_events.csv',
            mime='text/csv',
        )
else:
    st.info("No event data available")

st.markdown("---")

# Venue Map
st.markdown("### 🗺️ Olympic Venue Locations")

# Paris coordinates for map centering
PARIS_LAT = 48.8566
PARIS_LON = 2.3522

# Create venue data for map (using mock coordinates as venues.csv doesn't have lat/lon)
venue_data = data['venues'].copy()

# Filter venues based on global filters
valid_sports = None

# 1. Filter by selected sports
if filters['sports']:
    valid_sports = set(filters['sports'])

# 2. Filter by selected countries (find sports they participate in)
if filters['countries']:
    country_sports = set()
    # Filter athletes by selected countries
    country_athletes = data['athletes'][data['athletes']['country'].isin(filters['countries'])]
    
    # Collect all disciplines/sports these athletes participate in
    for disciplines in country_athletes['disciplines'].dropna():
        if isinstance(disciplines, list):
            country_sports.update(disciplines)
        elif isinstance(disciplines, str):
            country_sports.add(disciplines)
            
    if valid_sports is None:
        valid_sports = country_sports
    else:
        valid_sports = valid_sports.intersection(country_sports)

# Apply filter if we have restrictions
if valid_sports is not None:
    def venue_has_sport(venue_sports):
        if not isinstance(venue_sports, list):
            return False
        return any(sport in valid_sports for sport in venue_sports)
        
    venue_data = venue_data[venue_data['sports'].apply(venue_has_sport)]
    
    if len(venue_data) == 0:
        st.warning("No venues found for the selected combination of country and sport.")

# Add mock coordinates for Paris venues (simplified)
venue_coords = {
    'Aquatics Centre': (48.8928, 2.3902),
    'Bercy Arena': (48.8387, 2.3790),
    'Champ de Mars Arena': (48.8584, 2.2945),
    'Château de Versailles': (48.8049, 2.1204),
    'Eiffel Tower Stadium': (48.8584, 2.2945),
    'Grand Palais': (48.8660, 2.3124),
    'Invalides': (48.8567, 2.3126),
    'La Concorde': (48.8656, 2.3212),
    'Stade de France': (48.9244, 2.3601),
    'Stade Roland-Garros': (48.8450, 2.2527),
    'Trocadéro': (48.8634, 2.2877),
    'Paris La Defense Arena': (48.8956, 2.2275),
}

# Add coordinates to venue data
venue_map_data = []
for venue_name, coords in venue_coords.items():
    venue_info = venue_data[venue_data['venue'].str.contains(venue_name, case=False, na=False)]
    if len(venue_info) > 0:
        sports_list = venue_info.iloc[0].get('sports', [])
        if isinstance(sports_list, list):
            sports_str = ', '.join(sports_list)
        else:
            sports_str = str(sports_list)
        
        venue_map_data.append({
            'venue': venue_name,
            'lat': coords[0],
            'lon': coords[1],
            'sports': sports_str
        })

if venue_map_data:
    venue_map_df = pd.DataFrame(venue_map_data)
    
    fig_map = px.scatter_map(
        venue_map_df,
        lat='lat',
        lon='lon',
        hover_name='venue',
        hover_data={'lat': False, 'lon': False, 'sports': True},
        color_discrete_sequence=['#FF4B4B'],
        zoom=10,
        height=600,
        title="Olympic Venues in Paris"
    )
    
    fig_map.update_layout(
        map_style="open-street-map",
        margin={"r": 0, "t": 40, "l": 0, "b": 0}
    )
    
    
    st.plotly_chart(fig_map, width="stretch")
else:
    st.info("Venue location data not available")

st.markdown("---")

# Venue List
st.markdown("### 📍 Venue List")

if len(data['venues']) > 0:
    # Create a grid for venues
    for i, row in data['venues'].iterrows():
        with st.expander(f"🏟️ {row['venue']}"):
            v_col1, v_col2 = st.columns([3, 1])
            with v_col1:
                st.markdown(f"**Sports:** {row['sports']}")
                st.markdown(f"**Dates:** {row['date_start']} to {row['date_end']}")
            with v_col2:
                if 'url' in row and pd.notna(row['url']):
                    st.link_button("View Venue Info", row['url'])
else:
    st.info("No venue data available")

st.markdown("---")

# Additional Stats
st.markdown("### 📊 Event Statistics")

col1, col2, col3 = st.columns(3)

with col1:
    total_events = len(data['events'])
    st.metric("Total Events", f"{total_events}")

with col2:
    total_sports = data['events']['sport'].nunique()
    st.metric("Total Sports", f"{total_sports}")

with col3:
    total_venues = len(data['venues'])
    st.metric("Total Venues", f"{total_venues}")

st.markdown("---")

# Data Export Section
st.markdown("### 📥 Data Export")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Detailed Venue Data")
    if 'venues' in data and len(data['venues']) > 0:
        st.dataframe(data['venues'], height=300, use_container_width=True)
        
        csv_venues = data['venues'].to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Venue Data (CSV)",
            data=csv_venues,
            file_name='paris_2024_venues.csv',
            mime='text/csv',
        )
    else:
        st.info("Venue data not available")

with col2:
    st.markdown("#### Full Event Schedule")
    if 'schedules' in data and len(data['schedules']) > 0:
        st.dataframe(data['schedules'].head(100), height=300, use_container_width=True)
        st.caption("Showing first 100 rows")
        
        csv_schedules = data['schedules'].to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Full Schedule (CSV)",
            data=csv_schedules,
            file_name='paris_2024_schedule.csv',
            mime='text/csv',
        )
    else:
        st.info("Schedule data not available")
