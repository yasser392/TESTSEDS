"""
👤 Athlete Performance Page - Paris 2024 Olympic Games Dashboard
Athlete-centric analysis with profile cards and performance metrics
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from utils.data_loader import load_all_data
from utils.data_cleaning import clean_athletes_data, clean_medals_data
from utils.filter_helpers import apply_filters_to_athletes
from utils.ultimate_creative_theme import apply_ultimate_creative_theme, create_ultimate_navbar, create_ultimate_header

st.set_page_config(
    page_title="Athlete Performance - Paris 2024",
    page_icon="👤",
    layout="wide"
)

# Apply Ultimate Creative Theme
apply_ultimate_creative_theme()

# Load data
# Load data
@st.cache_data
def load_clean_data_v2():
    data = load_all_data()
    data['athletes'] = clean_athletes_data(data['athletes'])
    data['medals'] = clean_medals_data(data['medals'])
    data['medallists'] = data['medallists']
    return data

data = load_clean_data_v2()

# Double check disciplines are lists (handling potential cache/parsing issues)
if 'disciplines' in data['athletes'].columns:
    def ensure_list_type(x):
        if isinstance(x, list):
            return x
        if isinstance(x, str):
            try:
                return eval(x)
            except:
                return []
        return []
    
    # Apply only if we detect strings
    if data['athletes']['disciplines'].apply(lambda x: isinstance(x, str)).any():
        data['athletes']['disciplines'] = data['athletes']['disciplines'].apply(ensure_list_type)

# Navbar with filters
filters = create_ultimate_navbar(data['athletes'], data['medals_total'], data['events'])

# Page Header  
create_ultimate_header("ATHLETE PERFORMANCE", "Detailed Athlete Analysis & Metrics", "👤")

# Apply filters to athletes
filtered_athletes = data['athletes'].copy()
if filters['countries']:
    filtered_athletes = filtered_athletes[filtered_athletes['country'].isin(filters['countries'])]
if filters['continents']:
    filtered_athletes = filtered_athletes[filtered_athletes['continent'].isin(filters['continents'])]

# Athlete Profile Card
st.markdown("### 🎯 Athlete Profile Card")

# Create searchable athlete selectbox
athlete_names = sorted(filtered_athletes['name'].dropna().unique())

if len(athlete_names) > 0:
    selected_athlete = st.selectbox(
        "Search and select an athlete:",
        options=athlete_names,
        help="Type to search for an athlete"
    )
    
    if selected_athlete:
        athlete_data = filtered_athletes[filtered_athletes['name'] == selected_athlete].iloc[0]
        
        # Display athlete profile in columns
        col1, col2, col3 = st.columns([1, 2, 2])
        
        with col1:
            # Placeholder for profile image
            st.markdown(f"""
                <div style='text-align: center; padding: 1rem; background-color: #f0f2f6; border-radius: 10px;'>
                    <div style='font-size: 80px;'>🏃</div>
                    <p style='margin: 0; font-size: 0.9rem; color: #666;'>Profile Photo</p>
                </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"**Full Name:** {athlete_data['name']}")
            st.markdown(f"**Country/NOC:** {athlete_data['country']} ({athlete_data['country_code']})")
            
            height_str = f"{athlete_data['height']:.1f} cm" if pd.notna(athlete_data['height']) else "N/A"
            weight_str = f"{athlete_data['weight']:.1f} kg" if pd.notna(athlete_data['weight']) else "N/A"
            st.markdown(f"**Height:** {height_str}")
            st.markdown(f"**Weight:** {weight_str}")
            
            age_str = f"{int(athlete_data['age'])} years" if pd.notna(athlete_data['age']) else "N/A"
            st.markdown(f"**Age:** {age_str}")
        
        with col3:
            # Get coach information
            coach_names = []
            if 'coaches' in data and len(data['coaches']) > 0:
                coaches_df = data['coaches']
                athlete_country = athlete_data['country_code']
                athlete_disciplines = athlete_data['disciplines'] # This is a list
                
                # Filter coaches by country
                country_coaches = coaches_df[coaches_df['country_code'] == athlete_country]
                
                # Filter by discipline
                # Coach discipline is a string, athlete disciplines is a list of strings
                if not country_coaches.empty and isinstance(athlete_disciplines, list):
                    relevant_coaches = country_coaches[country_coaches['disciplines'].isin(athlete_disciplines)]
                    if not relevant_coaches.empty:
                        coach_names = relevant_coaches['name'].tolist()
            
            if coach_names:
                coach_info = ", ".join(coach_names)
            else:
                coach_info = "N/A"
            
            st.markdown(f"**Coach(es):** {coach_info}")
            
            # Sports and disciplines
            disciplines = athlete_data.get('disciplines', 'N/A')
            if isinstance(disciplines, list):
                disciplines = ', '.join(disciplines)
            st.markdown(f"**Disciplines:** {disciplines}")
            
            st.markdown(f"**Function:** {athlete_data.get('function', 'N/A')}")
            st.markdown(f"**Birth Place:** {athlete_data.get('birth_place', 'N/A')}")

else:
    st.info("No athletes found for current filters")

st.markdown("---")

# Athlete Age Distribution
st.markdown("### 📊 Athlete Age Distribution")

if len(filtered_athletes[filtered_athletes['age'].notna()]) > 0:
    age_df = filtered_athletes[filtered_athletes['age'].notna()]
    
    # Row 1: Gender and Continent
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### By Gender")
        fig_gender = px.box(
            age_df,
            x='gender',
            y='age',
            color='gender',
            title="Age Distribution by Gender",
            color_discrete_map={'Male': '#00D4FF', 'Female': '#FF00CC'} # Cyberpunk colors
        )
        fig_gender.update_layout(height=400)
        st.plotly_chart(fig_gender, use_container_width=True)
        
    with col2:
        st.markdown("#### By Continent")
        fig_continent = px.violin(
            age_df,
            x='continent',
            y='age',
            color='continent',
            box=True,
            title="Age Distribution by Continent",
            color_discrete_sequence=px.colors.qualitative.Bold
        )
        fig_continent.update_layout(height=400)
        st.plotly_chart(fig_continent, use_container_width=True)
        
    # Row 2: Discipline
    st.markdown("#### By Discipline")
    
    # Get all available sports and top sports for default selection
    all_sports = sorted(filtered_athletes['disciplines'].explode().dropna().unique().tolist())
    top_sports_data = filtered_athletes['disciplines'].explode().value_counts().head(15).index.tolist() if len(filtered_athletes) > 0 else []
    
    # Interactive sport selection
    selected_sports = st.multiselect(
        "Select Sports to Compare:",
        options=all_sports,
        default=[sport for sport in top_sports_data if sport in all_sports],
        help="Choose specific sports to analyze age distribution"
    )
    
    if selected_sports:
        # Prepare data for discipline chart
        discipline_age_data = []
        for _, row in age_df.iterrows():
            if isinstance(row['disciplines'], list):
                for sport in row['disciplines']:
                    if sport in selected_sports:
                        discipline_age_data.append({'Sport': sport, 'Age': row['age'], 'Gender': row['gender']})
        
        if discipline_age_data:
            disc_age_df = pd.DataFrame(discipline_age_data)
            
            fig_disc = px.box(
                disc_age_df,
                x='Sport',
                y='Age',
                color='Gender',
                title=f"Age Distribution by Sport ({len(selected_sports)} Selected)",
                color_discrete_map={'Male': '#00D4FF', 'Female': '#FF00CC'}
            )
            
            fig_disc.update_layout(
                height=500,
                xaxis={'tickangle': -45}
            )
            
            st.plotly_chart(fig_disc, use_container_width=True)
        else:
            st.info("No age data available for the selected sports")
    else:
        st.info("Please select at least one sport to view the chart")

else:
    st.info("No age data available for current filters")

st.markdown("---")

# Gender Distribution
st.markdown("### ⚧️ Gender Distribution by Continent")

col1, col2 = st.columns(2)

with col1:
    if len(filtered_athletes) > 0:
        gender_overall = filtered_athletes['gender'].value_counts()
        
        fig_gender_pie = px.pie(
            values=gender_overall.values,
            names=gender_overall.index,
            title="Overall Gender Distribution",
            color_discrete_map={'Male': '#4169E1', 'Female': '#FF69B4'}
        )
        
        st.plotly_chart(fig_gender_pie, width="stretch")

with col2:
    if len(filtered_athletes) > 0:
        gender_continent = filtered_athletes.groupby(['continent', 'gender']).size().reset_index(name='count')
        
        fig_gender_bar = px.bar(
            gender_continent,
            x='continent',
            y='count',
            color='gender',
            title="Gender Distribution by Continent",
            barmode='group',
            color_discrete_map={'Male': '#4169E1', 'Female': '#FF69B4'}
        )
        
        fig_gender_bar.update_layout(height=400)
        st.plotly_chart(fig_gender_bar, width="stretch")

st.markdown("---")

# Top Athletes by Medals
st.markdown("### 🏅 Top 10 Athletes by Medal Count")

if len(data['medallists']) > 0:
    # Count medals by athlete
    athlete_medals = data['medallists'].groupby('name').size().reset_index(name='medal_count')
    athlete_medals = athlete_medals.sort_values('medal_count', ascending=False).head(10)
    
    # Merge with athlete data to get country
    athlete_medals = athlete_medals.merge(
        data['athletes'][['name', 'country']].drop_duplicates(),
        on='name',
        how='left'
    )
    
    fig_top_athletes = px.bar(
        athlete_medals.sort_values('medal_count'),
        x='medal_count',
        y='name',
        orientation='h',
        title="Athletes with Most Medals",
        labels={'medal_count': 'Number of Medals', 'name': 'Athlete'},
        color='medal_count',
        color_continuous_scale='Purpor',
        hover_data=['country']
    )
    
    fig_top_athletes.update_layout(
        height=500,
        showlegend=False
    )
    
    st.plotly_chart(fig_top_athletes, width="stretch")
else:
    st.info("No medallist data available")

st.markdown("---")

st.markdown("---")

# 3D Physical Analysis
st.markdown("### 🧊 3D Physical Analysis")

if len(filtered_athletes) > 0:
    # Filter for valid physical data
    physical_df = filtered_athletes.dropna(subset=['height', 'weight', 'age']).copy()
    
    if len(physical_df) > 0:
        # Limit points for performance if dataset is large
        if len(physical_df) > 2000:
            physical_df = physical_df.sample(2000)
            st.caption("Displaying a random sample of 2000 athletes for performance")
            
        fig_3d = px.scatter_3d(
            physical_df,
            x='weight',
            y='height',
            z='age',
            color='gender',
            hover_name='name',
            hover_data=['country', 'disciplines'],
            title="Athlete Physical Attributes (Weight vs Height vs Age)",
            labels={'weight': 'Weight (kg)', 'height': 'Height (cm)', 'age': 'Age (years)'},
            color_discrete_map={'Male': '#00D4FF', 'Female': '#FF00CC'},
            opacity=0.7
        )
        
        fig_3d.update_layout(
            height=600,
            scene=dict(
                xaxis=dict(backgroundcolor="rgba(0,0,0,0)", gridcolor="rgba(255,255,255,0.1)"),
                yaxis=dict(backgroundcolor="rgba(0,0,0,0)", gridcolor="rgba(255,255,255,0.1)"),
                zaxis=dict(backgroundcolor="rgba(0,0,0,0)", gridcolor="rgba(255,255,255,0.1)"),
            ),
            margin=dict(l=0, r=0, b=0, t=40)
        )
        
        st.plotly_chart(fig_3d, use_container_width=True)
        
        # Prepare data for performance charts (merge with medal counts)
        if len(data['medallists']) > 0:
            medal_counts = data['medallists']['name'].value_counts().reset_index()
            medal_counts.columns = ['name', 'medal_count']
            
            # Merge with physical data
            perf_df = physical_df.merge(medal_counts, on='name', how='inner') # Only athletes with medals
            
            if len(perf_df) > 0:
                st.markdown("#### 🥇 Performance Landscapes")
                col1, col2 = st.columns(2)
                
                with col1:
                    # Chart 2: Age vs Height vs Medals
                    fig_3d_perf1 = px.scatter_3d(
                        perf_df,
                        x='age',
                        y='height',
                        z='medal_count',
                        color='gender',
                        hover_name='name',
                        hover_data=['country', 'disciplines'],
                        title="Performance: Age vs Height vs Medals",
                        labels={'age': 'Age', 'height': 'Height', 'medal_count': 'Medals'},
                        color_discrete_map={'Male': '#00D4FF', 'Female': '#FF00CC'},
                        opacity=0.8
                    )
                    fig_3d_perf1.update_layout(
                        height=500,
                        scene=dict(
                            xaxis=dict(backgroundcolor="rgba(0,0,0,0)", gridcolor="rgba(255,255,255,0.1)"),
                            yaxis=dict(backgroundcolor="rgba(0,0,0,0)", gridcolor="rgba(255,255,255,0.1)"),
                            zaxis=dict(backgroundcolor="rgba(0,0,0,0)", gridcolor="rgba(255,255,255,0.1)"),
                        ),
                        margin=dict(l=0, r=0, b=0, t=0)
                    )
                    st.plotly_chart(fig_3d_perf1, use_container_width=True)
                    
                with col2:
                    # Chart 3: Weight vs Age vs Medals
                    fig_3d_perf2 = px.scatter_3d(
                        perf_df,
                        x='weight',
                        y='age',
                        z='medal_count',
                        color='gender',
                        hover_name='name',
                        hover_data=['country', 'disciplines'],
                        title="Success: Weight vs Age vs Medals",
                        labels={'weight': 'Weight', 'age': 'Age', 'medal_count': 'Medals'},
                        color_discrete_map={'Male': '#00D4FF', 'Female': '#FF00CC'},
                        opacity=0.8
                    )
                    fig_3d_perf2.update_layout(
                        height=500,
                        scene=dict(
                            xaxis=dict(backgroundcolor="rgba(0,0,0,0)", gridcolor="rgba(255,255,255,0.1)"),
                            yaxis=dict(backgroundcolor="rgba(0,0,0,0)", gridcolor="rgba(255,255,255,0.1)"),
                            zaxis=dict(backgroundcolor="rgba(0,0,0,0)", gridcolor="rgba(255,255,255,0.1)"),
                        ),
                        margin=dict(l=0, r=0, b=0, t=0)
                    )
                    st.plotly_chart(fig_3d_perf2, use_container_width=True)
            else:
                st.info("No athletes with both physical data and medals found in current selection")
                
    else:
        st.info("Insufficient physical data (height/weight) for 3D visualization")
else:
    st.info("No data available")

st.markdown("---")

# Detailed Athlete Data Table
st.markdown("### 📋 Detailed Athlete Data")

if len(filtered_athletes) > 0:
    # Select columns to display
    display_cols = ['name', 'country', 'country_code', 'disciplines', 'gender', 'age', 'height', 'weight']
    
    # Filter columns that exist in the dataframe
    valid_cols = [col for col in display_cols if col in filtered_athletes.columns]
    
    display_df = filtered_athletes[valid_cols].copy()
    
    # Format disciplines list as string for better display
    if 'disciplines' in display_df.columns:
        display_df['disciplines'] = display_df['disciplines'].apply(
            lambda x: ', '.join(x) if isinstance(x, list) else str(x)
        )
    
    # Display dataframe with download option
    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "name": "Athlete Name",
            "country": "Country",
            "country_code": "NOC",
            "disciplines": "Sport(s)",
            "gender": "Gender",
            "age": "Age",
            "height": "Height (cm)",
            "weight": "Weight (kg)"
        }
    )
    
    # Download button
    csv = display_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Athlete Data as CSV",
        data=csv,
        file_name='paris_2024_athletes.csv',
        mime='text/csv',
    )
else:
    st.info("No athlete data available to display")
