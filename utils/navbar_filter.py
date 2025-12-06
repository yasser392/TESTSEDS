"""
Creative Navbar Filter Utility for Paris 2024 Olympic Dashboard
Renders global filters in a stunning navbar with glassmorphism and gradients
"""
import streamlit as st
import pandas as pd


def apply_navbar_styles():
    """Apply creative navbar styling with glassmorphism and deep purple-blue theme"""
    st.markdown("""
        <style>
       /* Import Premium Creative Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Righteous&display=swap');
        @import url('https://api.fontshare.com/v2/css?f[]=clash-display@700&display=swap');
        
        /* Hide Streamlit header */
        header[data-testid="stHeader"] {
            display: none;
        }
        
        /* Adjust main content padding */
        .main .block-container {
            padding-top: 0rem !important;
            max-width: 100% !important;
        }
        
        /* Creative Navbar - Fixed at top with Olympic theme */
        .navbar-container {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 999999;
            background: linear-gradient(135deg, 
                rgba(0, 10, 30, 0.95) 0%,
                rgba(20, 20, 60, 0.95) 25%, 
                rgba(40, 0, 80, 0.95) 50%,
                rgba(20, 20, 60, 0.95) 75%,
                rgba(0, 10, 30, 0.95) 100%);
            backdrop-filter: blur(40px) saturate(180%);
            -webkit-backdrop-filter: blur(40px) saturate(180%);
            padding: 1rem 2rem 1.5rem 2rem;
            border-bottom: 3px solid transparent;
            border-image: linear-gradient(90deg, 
                #0066FF 0%, #00D9FF 25%, #00FF87 50%, #FFD700 75%, #FF6B35 100%) 1;
            box-shadow: 
                0 10px 50px rgba(0, 0, 0, 0.7),
                0 0 100px rgba(0, 102, 255, 0.4),
                0 0 150px rgba(157, 0, 255, 0.3),
                inset 0 0 60px rgba(0, 217, 255, 0.05);
            animation: navbarGlow 4s ease-in-out infinite;
            position: relative;
            overflow: hidden;
        }
        
        /* Animated background effect */
        .navbar-container::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: linear-gradient(45deg, 
                transparent 30%,
                rgba(0, 217, 255, 0.1) 50%,
                transparent 70%);
            animation: holographicSweep 8s linear infinite;
        }
        
        @keyframes holographicSweep {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        @keyframes navbarGlow {
            0%, 100% { 
                box-shadow: 
                    0 10px 50px rgba(0, 0, 0, 0.7),
                    0 0 80px rgba(0, 102, 255, 0.3);
            }
            50% { 
                box-shadow: 
                    0 10px 50px rgba(0, 0, 0, 0.7),
                    0 0 150px rgba(157, 0, 255, 0.5),
                    0 0 200px rgba(0, 217, 255, 0.3);
            }
        }
        
        /* Olympic Rings with glow */
        .olympic-rings {
            text-align: center;
            font-size: 1.8rem;
            letter-spacing: 8px;
            margin-bottom: 0.8rem;
            filter: drop-shadow(0 0 15px rgba(255, 215, 0, 0.8))
                    drop-shadow(0 0 25px rgba(0, 217, 255, 0.6));
            animation: ringsFloat 4s ease-in-out infinite;
            position: relative;
            z-index: 2;
        }
        
        @keyframes ringsFloat {
            0%, 100% { transform: translateY(0px) scale(1); }
            50% { transform: translateY(-8px) scale(1.05); }
        }
        
        /* Navbar Title - Creative Typography */
        .navbar-title {
            text-align: center;
            font-size: 2rem;
            font-weight: 900;
            font-family: 'Clash Display', 'Righteous', sans-serif;
            background: linear-gradient(135deg, 
                #FFD700 0%, #FF6B35 20%, #FF00FF 40%, #0066FF 60%, #00D9FF 80%, #00FF87 100%);
            background-size: 300% 300%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: rainbowText 6s linear infinite, titleFloat 3s ease-in-out infinite;
            letter-spacing: 0.15em;
            position: relative;
            z-index: 2;
            text-shadow: 0 0 60px rgba(255, 215, 0, 0.5);
        }
        
        @keyframes rainbowText {
            0% { background-position: 0% 50%; }
            100% { background-position: 300% 50%; }
        }
        
        @keyframes titleFloat {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-3px); }
        }
        
        /* Enhance Streamlit widgets in navbar */
        .navbar-container .stMultiSelect label,
        .navbar-container .stSelectbox label {
            color: #00D9FF !important;
            font-family: 'Space Grotesk', sans-serif !important;
            font-weight: 700 !important;
            font-size: 0.9rem !important;
            text-shadow: 0 0 15px rgba(0, 217, 255, 0.6);
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }
        
        .navbar-container .stMultiSelect > div,
        .navbar-container .stSelectbox > div {
            background: rgba(255, 255, 255, 0.95) !important;
            border-radius: 12px;
            border: 2px solid rgba(0, 217, 255, 0.4);
            box-shadow: 0 4px 20px rgba(0, 102, 255, 0.2);
            transition: all 0.3s ease;
        }
        
        .navbar-container .stMultiSelect > div:hover,
        .navbar-container .stSelectbox > div:hover {
            border-color: rgba(0, 217, 255, 0.8);
            box-shadow: 0 6px 30px rgba(0, 217, 255, 0.4);
            transform: translateY(-2px);
        }
        
        /* Checkbox styling */
        .navbar-container .stCheckbox label {
            color: white !important;
            font-family: 'Space Grotesk', sans-serif !important;
            font-weight: 600;
            text-shadow: 0 0 10px rgba(255, 255, 255, 0.4);
        }
        
        /* Expander styling */
        .navbar-container .streamlit-expanderHeader {
            background: linear-gradient(135deg, 
                rgba(0, 102, 255, 0.15), 
                rgba(157, 0, 255, 0.15)) !important;
            border-radius: 14px !important;
            border: 2px solid rgba(0, 217, 255, 0.3) !important;
            font-family: 'Space Grotesk', sans-serif !important;
            font-weight: 700 !important;
            color: #00FF87 !important;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            transition: all 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
            position: relative;
            z-index: 2;
        }
        
        .navbar-container .streamlit-expanderHeader:hover {
            background: linear-gradient(135deg, 
                rgba(0, 102, 255, 0.3), 
                rgba(157, 0, 255, 0.3)) !important;
            border-color: rgba(0, 217, 255, 0.8) !important;
            box-shadow: 
                0 6px 25px rgba(0, 217, 255, 0.4),
                0 0 40px rgba(0, 102, 255, 0.3);
            transform: translateY(-2px);
        }
        </style>
    """, unsafe_allow_html=True)


def create_navbar_filters(athletes_df, medals_total_df, events_df):
    """
    Create creative navbar with global filters
    
    Args:
        athletes_df: Athletes DataFrame (with continent column)
        medals_total_df: Medals total DataFrame (with continent column)
        events_df: Events DataFrame
        
    Returns:
        dict: Dictionary of selected filter values
    """
    # Apply navbar styles
    apply_navbar_styles()
    
    # Create navbar container
    st.markdown('<div class="navbar-container">', unsafe_allow_html=True)
    
    # Olympic Rings decoration
    st.markdown('<div class="olympic-rings">🔵 🟡 ⚫ 🟢 🔴</div>', unsafe_allow_html=True)
    
    # Navbar title
    st.markdown('<div class="navbar-title">🎯 GLOBAL FILTERS</div>', unsafe_allow_html=True)
    
    # Get unique values for filters
    all_countries = sorted(athletes_df['country'].dropna().unique())
    all_sports = sorted(events_df['sport'].dropna().unique())
    all_continents = sorted(athletes_df['continent'].dropna().unique())
    
    # Create expandable filter sections for better organization
    with st.expander("🌍 GEOGRAPHIC FILTERS", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            selected_countries = st.multiselect(
                "📍 Select Countries",
                options=all_countries,
                default=[],
                help="Filter by specific countries (leave empty for all)",
                key="navbar_countries"
            )
        
        with col2:
            selected_continents = st.multiselect(
                "🗺️ Select Continents",
                options=all_continents,
                default=[],
                help="Filter by continents (Creativity Filter!)",
                key="navbar_continents"
            )
    
    # Sports filter section
    with st.expander("⚽ SPORTS FILTERS", expanded=True):
        selected_sports = st.multiselect(
            "🏅 Select Sports",
            options=all_sports,
            default=[],
            help="Filter by specific sports (leave empty for all)",
            key="navbar_sports"
        )
    
    # Medal type filter section
    with st.expander("🏆 MEDAL TYPE FILTERS", expanded=True):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            gold_checked = st.checkbox("🥇 Gold Medal", value=True, key="navbar_gold")
        with col2:
            silver_checked = st.checkbox("🥈 Silver Medal", value=True, key="navbar_silver")
        with col3:
            bronze_checked = st.checkbox("🥉 Bronze Medal", value=True, key="navbar_bronze")
    
    # Close navbar container
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Add spacer to push content below navbar
    st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)
    
    # Prepare medal types list
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
