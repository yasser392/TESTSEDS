"""
🏅 Paris 2024 Olympic Games Dashboard - Overview Page
LA28 Volunteer Selection Challenge

Main landing page with KPIs and high-level summaries
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Import custom utilities
from utils.data_loader import load_all_data
from utils.data_cleaning import (
    clean_athletes_data, 
    clean_medals_total_data, 
    clean_medals_data
)
from utils.filter_helpers import apply_filters_to_medals_total
from utils.ultimate_creative_theme import apply_ultimate_creative_theme, create_ultimate_navbar, create_ultimate_header

#  Page configuration
st.set_page_config(
    page_title="Paris 2024 Olympics Dashboard",
    page_icon="🏅",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply Ultimate Creative Theme
apply_ultimate_creative_theme()

# Load and clean data
@st.cache_data
def load_and_clean_data():
    """Load and clean all necessary data"""
    data = load_all_data()
    data['athletes'] = clean_athletes_data(data['athletes'])
    data['medals_total'] = clean_medals_total_data(data['medals_total'])
    data['medals'] = clean_medals_data(data['medals'])
    return data

# Load data
with st.spinner('Loading Olympic data...'):
    data = load_and_clean_data()

# Create navbar with filters and get filter values
filters = create_ultimate_navbar(
    data['athletes'], 
    data['medals_total'], 
    data['events']
)

# Page Header
create_ultimate_header(
    "PARIS 2024 OLYMPICS",
    "Experience the Ultimate Interactive Dashboard",
    "🏅"
)

# Apply filters
filtered_medals = apply_filters_to_medals_total(data['medals_total'], filters)
filtered_athletes = data['athletes'].copy()
if filters['countries']:
    filtered_athletes = filtered_athletes[filtered_athletes['country'].isin(filters['countries'])]
if filters['continents']:
    filtered_athletes = filtered_athletes[filtered_athletes['continent'].isin(filters['continents'])]

filtered_events = data['events'].copy()
if filters['sports']:
    filtered_events = filtered_events[filtered_events['sport'].isin(filters['sports'])]

# KPI Metrics Section
st.markdown("## 📊 Key Performance Indicators")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    total_athletes = len(filtered_athletes)
    st.metric(
        label="👥 Total Athletes",
        value=f"{total_athletes:,}",
        help="Number of athletes participating"
    )

with col2:
    total_countries = filtered_medals['country'].nunique() if len(filtered_medals) > 0 else 0
    st.metric(
        label="🌍 Total Countries",
        value=f"{total_countries}",
        help="Number of countries with medals"
    )

with col3:
    total_sports = filtered_events['sport'].nunique() if len(filtered_events) > 0 else 0
    st.metric(
        label="⚽ Total Sports",
        value=f"{total_sports}",
        help="Number of different sports"
    )

with col4:
    total_medals = filtered_medals['Total'].sum() if len(filtered_medals) > 0 else 0
    st.metric(
        label="🏅 Total Medals",
        value=f"{int(total_medals):,}",
        help="Total medals awarded"
    )

with col5:
    total_events = len(filtered_events)
    st.metric(
        label="🎯 Number of Events",
        value=f"{total_events}",
        help="Total number of events"
    )

st.markdown("---")

# Visualizations
col_left, col_right = st.columns(2)

with col_left:
    st.markdown("### 🥇 Global Medal Distribution")
    
    if len(filtered_medals) > 0:
        # Calculate medal totals
        total_gold = filtered_medals['Gold Medal'].sum()
        total_silver = filtered_medals['Silver Medal'].sum()
        total_bronze = filtered_medals['Bronze Medal'].sum()
        
        # Create pie chart with premium colors
        medal_distribution = pd.DataFrame({
            'Medal Type': ['🥇 Gold', '🥈 Silver', '🥉 Bronze'],
            'Count': [total_gold, total_silver, total_bronze]
        })
        
        fig_pie = px.pie(
            medal_distribution,
            values='Count',
            names='Medal Type',
            title='Medal Distribution by Type',
            color_discrete_sequence=['#FFD700', '#C0C0C0', '#CD7F32'],  # Gold, Silver, Bronze colors
            hole=0.4
        )
        
        fig_pie.update_traces(
            textposition='inside',
            textinfo='percent+label',
            marker=dict(line=dict(color='white', width=3))
        )
        
        fig_pie.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white', size=14),
            showlegend=True,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=-0.2,
                xanchor="center",
                x=0.5,
                font=dict(color='white')
            )
        )
        
        st.plotly_chart(fig_pie, width='stretch')
    else:
        st.info("No medal data available for current filters")

with col_right:
    st.markdown("### 🏆 Top 10 Medal Standings")
    
    if len(filtered_medals) > 0:
        # Get top 10 countries
        top_10 = filtered_medals.nlargest(10, 'Total')
        
        fig_bar = px.bar(
            top_10,
            x='Total',
            y='country',
            orientation='h',
            title='Top 10 Countries by Total Medals',
            color='Total',
            color_continuous_scale='Purpor',  # Purple-Orange gradient
            labels={'Total': 'Total Medals', 'country': 'Country'}
        )
        
        fig_bar.update_traces(
            marker=dict(
                line=dict(color='white', width=1.5)
            )
        )
        
        fig_bar.update_layout(
            yaxis={'categoryorder': 'total ascending', 'showgrid': False, 'color': 'white'},
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white', size=12),
            xaxis=dict(
                showgrid=True,
                gridcolor='rgba(255,255,255,0.1)',
                color='white'
            ),
            coloraxis_colorbar=dict(
                title=dict(text="Medals", font=dict(color='white')),
                tickfont=dict(color='white')
            )
        )
        
        st.plotly_chart(fig_bar, width='stretch')
    else:
        st.info("No medal data available for current filters")

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #666; padding: 1rem;'>
        <p>🏅 Paris 2024 Olympic Games Dashboard | Created for LA28 Volunteer Selection</p>
        <p>Data Source: <a href='https://www.kaggle.com/datasets/piterfm/paris-2024-olympic-summer-games' target='_blank'>Kaggle Paris 2024 Olympic Summer Games Dataset</a></p>
    </div>
""", unsafe_allow_html=True)
