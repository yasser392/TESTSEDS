"""
🎨 3D Insights Page - Paris 2024 Olympic Games Dashboard
Creative 3D visualizations and advanced analytics
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

from utils.data_loader import load_all_data
from utils.data_cleaning import clean_athletes_data, clean_medals_total_data
from utils.filter_helpers import apply_filters_to_medals_total
from utils.ultimate_creative_theme import apply_ultimate_creative_theme, create_ultimate_navbar, create_ultimate_header

st.set_page_config(
    page_title="3D Insights - Paris 2024",
    page_icon="🎨",
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
    return data

data = load_clean_data()

# Navbar with filters
filters = create_ultimate_navbar(data['athletes'], data['medals_total'], data['events'])

# Page Header
create_ultimate_header("3D INSIGHTS", "Explore Olympic Data in Stunning 3D Visualizations", "🎨")

# Apply filters
filtered_medals = apply_filters_to_medals_total(data['medals_total'], filters)
filtered_athletes = data['athletes'].copy()
if filters['countries']:
    filtered_athletes = filtered_athletes[filtered_athletes['country'].isin(filters['countries'])]
if filters['continents']:
    filtered_athletes = filtered_athletes[filtered_athletes['continent'].isin(filters['continents'])]

# 3D Medal Distribution by Country
st.markdown("### 🌐 3D Medal Distribution Globe")

if len(filtered_medals) > 0:
    # Prepare data for 3D scatter
    medals_3d = filtered_medals.copy()
    
    # Create 3D scatter plot
    fig_3d_medals = px.scatter_3d(
        medals_3d.head(30),  # Top 30 for clarity
        x='Gold Medal',
        y='Silver Medal',
        z='Bronze Medal',
        size='Total',
        color='Total',
        hover_name='country',
        color_continuous_scale='Plasma',
        size_max=50,
        title="3D Medal Space: Gold vs Silver vs Bronze (Top 30 Countries)",
        labels={'Gold Medal': 'Gold', 'Silver Medal': 'Silver', 'Bronze Medal': 'Bronze'}
    )
    
    fig_3d_medals.update_layout(
        scene=dict(
            xaxis_title='Gold Medals',
            yaxis_title='Silver Medals',
            zaxis_title='Bronze Medals',
            bgcolor='rgba(240, 240, 255, 0.9)',
            xaxis=dict(backgroundcolor="rgb(230, 230,250)", gridcolor="white", showbackground=True),
            yaxis=dict(backgroundcolor="rgb(230, 230,250)", gridcolor="white", showbackground=True),
            zaxis=dict(backgroundcolor="rgb(230, 230,250)", gridcolor="white", showbackground=True),
        ),
        height=700,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
    st.plotly_chart(fig_3d_medals, width='stretch')
else:
    st.info("No data available for current filters")

st.markdown("---")

# 3D Athlete Performance Space
st.markdown("### 🏃 3D Athlete Performance Space")

col1, col2 = st.columns(2)

with col1:
    athletes_with_data = filtered_athletes[
        filtered_athletes['age'].notna() & 
        filtered_athletes['height'].notna() & 
        filtered_athletes['weight'].notna()
    ]
    
    if len(athletes_with_data) > 10:  # Only show if we have enough data
        # Sample intelligently based on available data
        sample_size = min(500, len(athletes_with_data))
        athlete_sample = athletes_with_data.sample(n=sample_size)
        
        fig_athletes_3d = px.scatter_3d(
            athlete_sample,
            x='height',
            y='weight',
            z='age',
            color='gender',
            hover_name='name',
            hover_data=['country', 'disciplines'],
            color_discrete_map={'Male': '#4169E1', 'Female': '#FF69B4'},
            title=f"Athletes: Height vs Weight vs Age (Showing {sample_size} athletes)",
            opacity=0.7
        )
        
        fig_athletes_3d.update_layout(
            scene=dict(
                xaxis_title='Height (cm)',
                yaxis_title='Weight (kg)',
                zaxis_title='Age (years)',
                bgcolor='rgba(255, 240, 240, 0.9)'
            ),
            height=600
        )
        
        st.plotly_chart(fig_athletes_3d, width='stretch')
    else:
        st.info("Insufficient athlete data for 3D visualization (need physical stats)")

with col2:
    st.markdown("### 📊 Interactive 3D Surface")
    
    if len(filtered_medals) > 0:
        # Create a 3D surface plot showing medal trends
        continents = filtered_medals.groupby('continent').agg({
            'Gold Medal': 'sum',
            'Silver Medal': 'sum', 
            'Bronze Medal': 'sum'
        }).reset_index()
        
        if len(continents) > 0:
            # Create mesh for surface
            medal_types = ['Gold Medal', 'Silver Medal', 'Bronze Medal']
            z_data = continents[medal_types].values.T
            
            fig_surface = go.Figure(data=[go.Surface(
                z=z_data,
                x=continents['continent'].tolist(),
                y=medal_types,
                colorscale='Electric',
                showscale=True
            )])
            
            fig_surface.update_layout(
                title='3D Medal Surface by Continent',
                scene=dict(
                    xaxis_title='Continent',
                    yaxis_title='Medal Type',
                    zaxis_title='Medal Count',
                    camera=dict(
                        eye=dict(x=1.5, y=1.5, z=1.3)
                    )
                ),
                height=600
            )
            
            st.plotly_chart(fig_surface, width="stretch")

st.markdown("---")

# 3D Mesh Network
st.markdown("### 🕸️ 3D Medal Network Visualization")

if len(filtered_medals) >= 10:
    top_countries = filtered_medals.nlargest(10, 'Total')
    
    # Create 3D network-like visualization
    theta = np.linspace(0, 2*np.pi, len(top_countries))
    r = top_countries['Total'].values
    
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    z = top_countries['Gold Medal'].values
    
    fig_network = go.Figure()
    
    # Add points
    fig_network.add_trace(go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers+text',
        marker=dict(
            size=top_countries['Total'].values / 5,
            color=top_countries['Gold Medal'].values,
            colorscale='Purples',
            showscale=True,
            colorbar=dict(title="Gold Medals")
        ),
        text=top_countries['country'].tolist(),
        textposition="top center",
        hovertemplate='<b>%{text}</b><br>Gold: ' + top_countries['Gold Medal'].astype(str) + 
                     '<br>Total: ' + top_countries['Total'].astype(str) + '<extra></extra>'
    ))
    
    # Add connecting lines
    for i in range(len(x)):
        fig_network.add_trace(go.Scatter3d(
            x=[0, x[i]], y=[0, y[i]], z=[0, z[i]],
            mode='lines',
            line=dict(color='rgba(100, 100, 100, 0.3)', width=2),
            showlegend=False,
            hoverinfo='skip'
        ))
    
    fig_network.update_layout(
        title='3D Network: Countries Connected by Performance',
        scene=dict(
            bgcolor='rgba(240, 248, 255, 0.9)',
            xaxis=dict(showgrid=False, showticklabels=False, title=''),
            yaxis=dict(showgrid=False, showticklabels=False, title=''),
            zaxis_title='Gold Medals',
            camera=dict(eye=dict(x=1.8, y=1.8, z=1.3))
        ),
        height=700,
        showlegend=False
    )
    
    st.plotly_chart(fig_network, width="stretch")

st.markdown("---")

# Animated 3D Bubble
st.markdown("### 💫 3D Animated Medal Evolution")

if len(filtered_medals) > 0:
    # Create animated bubble chart
    top_15 = filtered_medals.nlargest(15, 'Total')
    
    fig_bubble = px.scatter_3d(
        top_15,
        x='Gold Medal',
        y='Silver Medal',
        z='Bronze Medal',
        size='Total',
        color='continent',
        hover_name='country',
        size_max=60,
        title="3D Medal Bubble Chart (Top 15 Countries)",
        color_discrete_sequence=px.colors.qualitative.Vivid
    )
    
    fig_bubble.update_layout(
        scene=dict(
            xaxis_title='🥇 Gold',
            yaxis_title='🥈 Silver',
            zaxis_title='🥉 Bronze',
            bgcolor='rgba(255, 250, 240, 0.95)',
            camera=dict(
                eye=dict(x=1.5, y=1.5, z=1.5)
            )
        ),
        height=700
    )
    
    # Add rotation animation
    fig_bubble.update_layout(
        updatemenus=[dict(
            type="buttons",
            showactive=False,
            buttons=[dict(
                label="▶ Rotate",
                method="animate",
                args=[None, {"frame": {"duration": 50}, "fromcurrent": True}]
            )]
        )]
    )
    
    st.plotly_chart(fig_bubble, width="stretch")

# Footer with stats
st.markdown("---")
st.markdown("### 📈 Quick Stats")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Countries Analyzed", len(filtered_medals))
with col2:
    st.metric("Total 3D Data Points", len(filtered_athletes))
with col3:
    st.metric("Visualizations", "6 3D Charts")
with col4:
    st.metric("Dimensions", "3D + Time")
