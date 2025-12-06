"""
🗺️ Global Analysis Page - Paris 2024 Olympic Games Dashboard
Geographic and hierarchical medal analysis with continent-level views
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from utils.data_loader import load_all_data
from utils.data_cleaning import clean_athletes_data, clean_medals_total_data, clean_medals_data
from utils.filter_helpers import apply_filters_to_medals_total
from utils.navbar_filter import create_navbar_filters
from utils.ultimate_creative_theme import apply_ultimate_creative_theme, create_ultimate_navbar, create_ultimate_header
from utils.analytics import calculate_cumulative_medals

st.set_page_config(
    page_title="Global Analysis - Paris 2024",
    page_icon="🗺️",
    layout="wide"
)

# Apply Ultimate Creative Theme
apply_ultimate_creative_theme()

# Load data
@st.cache_data
def load_clean_data():
    data = load_all_data()
    data['athletes'] = clean_athletes_data(data['athletes'])
    data['medals_total'] = clean_medals_total_data(data['medals_total'])
    data['medals'] = clean_medals_data(data['medals'])
    return data

data = load_clean_data()

# Navbar with filters
filters = create_ultimate_navbar(data['athletes'], data['medals_total'], data['events'])

# Page Header
create_ultimate_header("GLOBAL ANALYSIS", "Geographic Medal Distribution Across The World", "🗺️")


# Apply filters
filtered_medals = apply_filters_to_medals_total(data['medals_total'], filters)

# World Medal Map (Choropleth)
st.markdown("### 🌍 World Medal Map")

if len(filtered_medals) > 0:
    fig_map = px.choropleth(
        filtered_medals,
        locations='country_code',
        color='Total',
        hover_name='country',
        hover_data={
            'country_code': False,
            'Gold Medal': True,
            'Silver Medal': True,
            'Bronze Medal': True,
            'Total': True
        },
        color_continuous_scale='Purpor',
        labels={'Total': 'Total Medals'}
    )
    
    fig_map.update_layout(
        title_text="Medal Count by Country",
        geo=dict(showframe=False, showcoastlines=True),
        height=500
    )
    
    st.plotly_chart(fig_map, width="stretch")
else:
    st.info("No data available for current filters")

st.markdown("---")

# Medal Hierarchy by Continent
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🎯 Medal Hierarchy (Sunburst)")
    
    # Use detailed medals data for deeper hierarchy (including Sport)
    hierarchy_source = data['medals'].copy()
    
    # Apply filters to detailed data
    if filters['countries']:
        hierarchy_source = hierarchy_source[hierarchy_source['country'].isin(filters['countries'])]
    if filters['continents']:
        hierarchy_source = hierarchy_source[hierarchy_source['continent'].isin(filters['continents'])]
    
    if len(hierarchy_source) > 0:
        # Group by hierarchy levels: Continent -> Country -> Sport
        hierarchy_grouped = hierarchy_source.groupby(['continent', 'country', 'discipline']).size().reset_index(name='count')
        
        fig_sunburst = px.sunburst(
            hierarchy_grouped,
            path=['continent', 'country', 'discipline'],
            values='count',
            color='continent',
            title="Continent → Country → Sport",
            color_discrete_sequence=px.colors.qualitative.Bold
        )
        
        fig_sunburst.update_layout(height=500)
        st.plotly_chart(fig_sunburst, width="stretch")
    else:
        st.info("No data available")

with col2:
    st.markdown("### 🎯 Medal Hierarchy (Treemap)")
    
    if len(hierarchy_source) > 0:
        fig_treemap = px.treemap(
            hierarchy_grouped,
            path=['continent', 'country', 'discipline'],
            values='count',
            color='continent',
            title="Continent → Country → Sport",
            color_discrete_sequence=px.colors.qualitative.Bold
        )
        
        fig_treemap.update_layout(height=500)
        st.plotly_chart(fig_treemap, width="stretch")
    else:
        st.info("No data available")

st.markdown("---")

# Continent vs Medals
st.markdown("### 🌐 Continent vs. Medals")

if len(filtered_medals) > 0:
    continent_medals = filtered_medals.groupby('continent').agg({
        'Gold Medal': 'sum',
        'Silver Medal': 'sum',
        'Bronze Medal': 'sum'
    }).reset_index()
    
    fig_continent = go.Figure()
    fig_continent.add_trace(go.Bar(name='Gold', x=continent_medals['continent'], y=continent_medals['Gold Medal'], marker_color='#FFD700'))
    fig_continent.add_trace(go.Bar(name='Silver', x=continent_medals['continent'], y=continent_medals['Silver Medal'], marker_color='#C0C0C0'))
    fig_continent.add_trace(go.Bar(name='Bronze', x=continent_medals['continent'], y=continent_medals['Bronze Medal'], marker_color='#CD7F32'))
    
    fig_continent.update_layout(
        title="Medal Distribution by Continent",
        xaxis_title="Continent",
        yaxis_title="Number of Medals",
        barmode='group',
        height=400
    )
    
    st.plotly_chart(fig_continent, width="stretch")
else:
    st.info("No data available")

st.markdown("---")

# Top 20 Countries vs Medals
st.markdown("### 🏆 Top 20 Countries vs. Medals")

if len(filtered_medals) > 0:
    top_20 = filtered_medals.nlargest(20, 'Total')
    
    fig_countries = go.Figure()
    fig_countries.add_trace(go.Bar(name='Gold', x=top_20['country'], y=top_20['Gold Medal'], marker_color='#FFD700'))
    fig_countries.add_trace(go.Bar(name='Silver', x=top_20['country'], y=top_20['Silver Medal'], marker_color='#C0C0C0'))
    fig_countries.add_trace(go.Bar(name='Bronze', x=top_20['country'], y=top_20['Bronze Medal'], marker_color='#CD7F32'))
    
    fig_countries.update_layout(
        title="Medal Distribution for Top 20 Countries",
        xaxis_title="Country",
        yaxis_title="Number of Medals",
        barmode='group',
        height=500,
        xaxis={'tickangle': -45}
    )
    
    st.plotly_chart(fig_countries, width="stretch")
else:
    st.info("No data available")

st.markdown("---")

# Medal Race: Cumulative Medals Over Time
st.markdown("### 📈 Medal Race: Cumulative Medals Over Time")

# Load full medals data for time series analysis
# We need the raw medals data which has dates, not the aggregated totals
if 'medals' in data and len(data['medals']) > 0:
    # Calculate cumulative medals
    cumulative_data = calculate_cumulative_medals(data['medals'])
    
    if not cumulative_data.empty:
        # Filter for top N countries based on current total medals
        # We can use the already calculated top_20 from the previous section or recalculate
        top_n = st.slider("Select Number of Top Countries to Display", min_value=5, max_value=20, value=10)
        
        # Get top countries by max cumulative medals
        top_countries_list = cumulative_data.groupby('country')['cumulative_medals'].max().nlargest(top_n).index.tolist()
        
        # Filter data for these countries
        filtered_cumulative = cumulative_data[cumulative_data['country'].isin(top_countries_list)]
        
        # Create line chart
        fig_race = px.line(
            filtered_cumulative,
            x='medal_date',
            y='cumulative_medals',
            color='country',
            title=f'Cumulative Medals Over Time (Top {top_n} Countries)',
            labels={'cumulative_medals': 'Total Medals', 'medal_date': 'Date', 'country': 'Country'},
            markers=True
        )
        
        fig_race.update_layout(
            xaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)'),
            yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)'),
            hovermode='x unified',
            height=600,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=-0.2,
                xanchor="center",
                x=0.5
            )
        )
        
        st.plotly_chart(fig_race, width="stretch")
    else:
        st.info("No timeline data available")
else:
    st.info("Medal data with dates not available")

st.markdown("---")

# Head-to-Head Comparison
st.markdown("### ⚔️ Head-to-Head Country Comparison")

if len(data['medals_total']) > 0:
    # Get list of countries
    countries_list = sorted(data['medals_total']['country'].unique().tolist())
    
    # Selection columns
    sel_col1, sel_col2 = st.columns(2)
    
    with sel_col1:
        country1 = st.selectbox("Select Country 1", countries_list, index=0)
        
    with sel_col2:
        # Default to second country if available
        default_idx = 1 if len(countries_list) > 1 else 0
        country2 = st.selectbox("Select Country 2", countries_list, index=default_idx)
        
    if country1 and country2:
        # Get data for both countries
        c1_data = data['medals_total'][data['medals_total']['country'] == country1].iloc[0] if not data['medals_total'][data['medals_total']['country'] == country1].empty else None
        c2_data = data['medals_total'][data['medals_total']['country'] == country2].iloc[0] if not data['medals_total'][data['medals_total']['country'] == country2].empty else None
        
        # Get athlete counts
        c1_athletes = len(data['athletes'][data['athletes']['country'] == country1])
        c2_athletes = len(data['athletes'][data['athletes']['country'] == country2])
        
        # Display comparison metrics
        comp_col1, comp_col2 = st.columns(2)
        
        with comp_col1:
            st.markdown(f"#### {country1}")
            if c1_data is not None:
                st.metric("🥇 Gold", c1_data['Gold Medal'], delta=int(c1_data['Gold Medal'] - (c2_data['Gold Medal'] if c2_data is not None else 0)))
                st.metric("🥈 Silver", c1_data['Silver Medal'], delta=int(c1_data['Silver Medal'] - (c2_data['Silver Medal'] if c2_data is not None else 0)))
                st.metric("🥉 Bronze", c1_data['Bronze Medal'], delta=int(c1_data['Bronze Medal'] - (c2_data['Bronze Medal'] if c2_data is not None else 0)))
                st.metric("🏅 Total", c1_data['Total'], delta=int(c1_data['Total'] - (c2_data['Total'] if c2_data is not None else 0)))
                st.metric("👥 Athletes", c1_athletes, delta=c1_athletes - c2_athletes)
            else:
                st.warning("No medal data available")
                
        with comp_col2:
            st.markdown(f"#### {country2}")
            if c2_data is not None:
                st.metric("🥇 Gold", c2_data['Gold Medal'], delta=int(c2_data['Gold Medal'] - (c1_data['Gold Medal'] if c1_data is not None else 0)))
                st.metric("🥈 Silver", c2_data['Silver Medal'], delta=int(c2_data['Silver Medal'] - (c1_data['Silver Medal'] if c1_data is not None else 0)))
                st.metric("🥉 Bronze", c2_data['Bronze Medal'], delta=int(c2_data['Bronze Medal'] - (c1_data['Bronze Medal'] if c1_data is not None else 0)))
                st.metric("🏅 Total", c2_data['Total'], delta=int(c2_data['Total'] - (c1_data['Total'] if c1_data is not None else 0)))
                st.metric("👥 Athletes", c2_athletes, delta=c2_athletes - c1_athletes)
            else:
                st.warning("No medal data available")
        
        # Radar Chart Comparison
        if c1_data is not None and c2_data is not None:
            st.markdown("#### 🕸️ Performance Radar")
            
            categories = ['Gold', 'Silver', 'Bronze', 'Total Medals', 'Athletes (Scaled)']
            
            # Scale athletes to be comparable with medals for visualization
            max_medals = max(c1_data['Total'], c2_data['Total'])
            max_athletes = max(c1_athletes, c2_athletes)
            scale_factor = max_medals / max_athletes if max_athletes > 0 else 1
            
            fig_radar = go.Figure()
            
            fig_radar.add_trace(go.Scatterpolar(
                r=[c1_data['Gold Medal'], c1_data['Silver Medal'], c1_data['Bronze Medal'], c1_data['Total'], c1_athletes * scale_factor],
                theta=categories,
                fill='toself',
                name=country1
            ))
            
            fig_radar.add_trace(go.Scatterpolar(
                r=[c2_data['Gold Medal'], c2_data['Silver Medal'], c2_data['Bronze Medal'], c2_data['Total'], c2_athletes * scale_factor],
                theta=categories,
                fill='toself',
                name=country2
            ))
            
            fig_radar.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, max(c1_data['Total'], c2_data['Total']) * 1.1]
                    )
                ),
                showlegend=True,
                height=500
            )
            
            st.plotly_chart(fig_radar, width="stretch")
            
            st.caption("* 'Athletes' metric is scaled to fit the chart range")

else:
    st.info("No data available for comparison")

st.markdown("---")

# 3D Medal Analysis
st.markdown("### 🧊 3D Medal Distribution")

if len(filtered_medals) > 0:
    # Filter out countries with 0 medals to reduce clutter
    plot_data = filtered_medals[filtered_medals['Total'] > 0].copy()
    
    if len(plot_data) > 0:
        fig_3d_medals = px.scatter_3d(
            plot_data,
            x='Gold Medal',
            y='Silver Medal',
            z='Bronze Medal',
            color='continent',
            size='Total',
            hover_name='country',
            title="Medal Composition Cluster (Gold vs Silver vs Bronze)",
            labels={'Gold Medal': 'Gold', 'Silver Medal': 'Silver', 'Bronze Medal': 'Bronze'},
            color_discrete_sequence=px.colors.qualitative.Bold,
            opacity=0.8,
            size_max=40
        )
        
        fig_3d_medals.update_layout(
            height=600,
            scene=dict(
                xaxis=dict(backgroundcolor="rgba(0,0,0,0)", gridcolor="rgba(255,255,255,0.1)"),
                yaxis=dict(backgroundcolor="rgba(0,0,0,0)", gridcolor="rgba(255,255,255,0.1)"),
                zaxis=dict(backgroundcolor="rgba(0,0,0,0)", gridcolor="rgba(255,255,255,0.1)"),
            ),
            margin=dict(l=0, r=0, b=0, t=40)
        )
        
        st.plotly_chart(fig_3d_medals, use_container_width=True)
        st.caption("Bubble size represents Total Medals. Rotate to explore country clusters.")
    else:
        st.info("No countries with medals in current selection")
else:
    st.info("No data available")

st.markdown("---")

# Data Export Section
st.markdown("### 📥 Data Export")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Detailed Medal Data")
    if 'medals' in data and len(data['medals']) > 0:
        st.dataframe(data['medals'].head(100), height=300, use_container_width=True)
        st.caption("Showing first 100 rows")
        
        csv_medals = data['medals'].to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Full Medal Data (CSV)",
            data=csv_medals,
            file_name='paris_2024_detailed_medals.csv',
            mime='text/csv',
        )
    else:
        st.info("Medal data not available")

with col2:
    st.markdown("#### Teams Data")
    if 'teams' in data and len(data['teams']) > 0:
        st.dataframe(data['teams'].head(100), height=300, use_container_width=True)
        st.caption("Showing first 100 rows")
        
        csv_teams = data['teams'].to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Teams Data (CSV)",
            data=csv_teams,
            file_name='paris_2024_teams.csv',
            mime='text/csv',
        )
    else:
        st.info("Teams data not available")
