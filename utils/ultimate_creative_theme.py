"""
Ultimate Creative Olympic Theme with Dark/Light Mode Toggle
Features: Animations, Gradients, 3D Effects, Bold Typography, Mode Switcher
"""
import streamlit as st


def apply_ultimate_creative_theme():
    """Apply ultra-creative theme with dark/light mode support"""
    
    # Initialize session state for theme
    if 'dark_mode' not in st.session_state:
        st.session_state.dark_mode = True
    
    # Get current theme colors
    if st.session_state.dark_mode:
        # DARK MODE - Vibrant & Bold
        bg_primary = "#0B0C1A"
        bg_secondary = "#1A1D35"
        bg_card = "rgba(255, 255, 255, 0.05)"
        text_primary = "#FFFFFF"
        text_secondary = "#B8B9C4"
        navbar_bg = "linear-gradient(135deg, #1A1D35 0%, #2D1B4E 50%, #1A1D35 100%)"
    else:
        # LIGHT MODE - Clean & Bright
        bg_primary = "#FFFFFF"
        bg_secondary = "#F5F7FA"
        bg_card = "#FFFFFF"
        text_primary = "#1A1D35"
        text_secondary = "#5E6278"
        navbar_bg = "linear-gradient(135deg, #FFFFFF 0%, #F3E5F5 50%, #FFFFFF 100%)"
    
    st.markdown(f"""
        <!-- Lucide Icons -->
        <script src="https://unpkg.com/lucide@latest"></script>
        
        <style>
        /* Import Premium Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&family=Bebas+Neue&family=Righteous&display=swap');
        
        /* Icon Styling */
        .lucide {{
            width: 20px;
            height: 20px;
            stroke: currentColor;
            stroke-width: 2;
            vertical-align: middle;
        }}
        
        .lucide-lg {{
            width: 32px;
            height: 32px;
        }}
        
        .lucide-xl {{
            width: 48px;
            height: 48px;
        }}
        
        /* === GLOBAL STYLES === */
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        /* Hide Streamlit Elements */
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        header[data-testid="stHeader"] {{display: none;}}
        
        /* Main Background with Animation */
        .stApp {{
            background: linear-gradient(135deg, 
                {'#0B0C1A 0%, #1A1D35 25%, #2D1B4E 50%, #1A1D35 75%, #0B0C1A 100%' if st.session_state.dark_mode else '#FFFFFF 0%, #F5F7FA 25%, #E8EAF6 50%, #F5F7FA 75%, #FFFFFF 100%'});
            background-size: 400% 400%;
            animation: gradientShift 15s ease infinite;
            font-family: 'Poppins', sans-serif;
            color: {text_primary};
        }}
        
        @keyframes gradientShift {{
            0%, 100% {{ background-position: 0% 50%; }}
            50% {{ background-position: 100% 50%; }}
        }}
        
        /* === CREATIVE NAVBAR === */
        .creative-navbar {{
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            min-height: 80px;
            background: {navbar_bg};
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            box-shadow: {'0 8px 32px rgba(0, 0, 0, 0.5)' if st.session_state.dark_mode else '0 4px 20px rgba(0, 0, 0, 0.1)'};
            z-index: 999999;
            display: flex;
            flex-direction: column;
            padding: 15px 2rem;
            border-bottom: 3px solid;
            border-image: linear-gradient(90deg, #FF6B6B, #4ECDC4, #45B7D1, #FFA07A, #98D8C8) 1;
            transition: all 0.3s ease;
        }}
        
        .navbar-top {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 10px;
        }}
        
        .nav-brand {{
            display: flex;
            align-items: center;
            gap: 15px;
        }}
        
        .nav-logo {{
            font-family: 'Bebas Neue', cursive;
            font-size: 2.2rem;
            background: linear-gradient(135deg, #FF6B6B, #4ECDC4, #45B7D1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: rainbow 3s linear infinite;
            letter-spacing: 2px;
            text-shadow: 0 0 30px rgba(78, 205, 196, 0.3);
        }}
        
        @keyframes rainbow {{
            0%, 100% {{ filter: hue-rotate(0deg); }}
            50% {{ filter: hue-rotate(180deg); }}
        }}
        
        .olympic-rings {{
            font-size: 1.8rem;
            filter: drop-shadow(0 4px 8px rgba(0,0,0,0.3));
            animation: bounce 2s infinite;
        }}
        
        @keyframes bounce {{
            0%, 100% {{ transform: translateY(0); }}
            50% {{ transform: translateY(-5px); }}
        }}
        
        .navbar-filters {{
            display: flex;
            gap: 15px;
            align-items: center;
            flex-wrap: wrap;
        }}
        
        .filter-section {{
            display: flex;
            align-items: center;
            gap: 8px;
            background: {'rgba(255,255,255,0.1)' if st.session_state.dark_mode else 'rgba(0,0,0,0.05)'};
            padding: 8px 15px;
            border-radius: 20px;
            border: 1px solid rgba(78, 205, 196, 0.3);
            transition: all 0.3s ease;
        }}
        
        .filter-section:hover {{
            background: {'rgba(255,255,255,0.2)' if st.session_state.dark_mode else 'rgba(0,0,0,0.1)'};
            border-color: #4ECDC4;
            transform: translateY(-2px);
        }}
        
        .filter-label {{
            font-weight: 700;
            font-size: 0.85rem;
            color: #4ECDC4;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        
        /* Mode Toggle Button */
        .mode-toggle {{
            width: 60px;
            height: 30px;
            background: linear-gradient(135deg, #FF6B6B, #4ECDC4);
            border-radius: 30px;
            cursor: pointer;
            position: relative;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(78, 205, 196, 0.4);
        }}
        
        .mode-toggle:hover {{
            transform: scale(1.1);
        }}
        
        /* === MAIN CONTENT === */
        .main .block-container {{
            padding-top: 120px !important;
            max-width: 1600px;
            padding-left: 3rem;
            padding-right: 3rem;
        }}
        
        /* === CREATIVE PAGE HEADER === */
        .creative-header {{
            text-align: center;
            margin: 3rem 0;
            position: relative;
            padding: 2rem;
            background: {bg_card};
            border-radius: 30px;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 20px 40px rgba(0,0,0,0.2);
        }}
        
        .header-icon {{
            font-size: 6rem;
            animation: float 3s ease-in-out infinite;
            filter: drop-shadow(0 10px 30px rgba(255, 107, 107, 0.5));
            margin-bottom: 1rem;
            display: inline-block;
        }}
        
        @keyframes float {{
            0%, 100% {{ transform: translateY(0px) rotate(0deg); }}
            50% {{ transform: translateY(-20px) rotate(5deg); }}
        }}
        
        .header-title {{
            font-family: 'Bebas Neue', cursive;
            font-size: 5rem;
            background: linear-gradient(135deg, #FF6B6B 0%, #4ECDC4 25%, #45B7D1 50%, #FFA07A 75%, #98D8C8 100%);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: gradientFlow 4s linear infinite;
            letter-spacing: 3px;
            margin: 0;
            line-height: 1.1;
        }}
        
        @keyframes gradientFlow {{
            0% {{ background-position: 0% center; }}
            100% {{ background-position: 200% center; }}
        }}
        
        .header-subtitle {{
            font-size: 1.4rem;
            color: {text_secondary};
            font-weight: 500;
            margin-top: 1rem;
            font-family: 'Poppins', sans-serif;
        }}
        
        /* === ULTRA PREMIUM METRIC CARDS === */
        [data-testid="stMetric"] {{
            background: {bg_card};
            backdrop-filter: blur(30px);
            -webkit-backdrop-filter: blur(30px);
            border-radius: 25px;
            padding: 1.5rem !important;
            border: 1px solid rgba(255, 255, 255, 0.1);
            position: relative;
            overflow: hidden;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            box-shadow: {'0 10px 30px rgba(0, 0, 0, 0.3)' if st.session_state.dark_mode else '0 10px 30px rgba(0, 0, 0, 0.05)'};
        }}
        
        [data-testid="stMetric"]::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0) 100%);
            z-index: 0;
        }}
        
        [data-testid="stMetric"]:hover {{
            transform: translateY(-10px) scale(1.02);
            box-shadow: 0 20px 40px rgba(78, 205, 196, 0.2);
            border-color: #4ECDC4;
        }}
        
        [data-testid="stMetricLabel"] {{
            font-family: 'Poppins', sans-serif !important;
            font-weight: 600 !important;
            font-size: 0.9rem !important;
            color: {text_secondary} !important;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            z-index: 1;
            position: relative;
        }}
        
        [data-testid="stMetricValue"] {{
            font-family: 'Bebas Neue', cursive !important;
            font-size: 3.5rem !important;
            font-weight: 400 !important;
            background: linear-gradient(135deg, #FF6B6B, #4ECDC4);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            z-index: 1;
            position: relative;
        }}
        
        /* === CHARTS === */
        [data-testid="stPlotlyChart"] {{
            background: {bg_card};
            backdrop-filter: blur(30px);
            -webkit-backdrop-filter: blur(30px);
            border-radius: 25px;
            padding: 1rem;
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: {'0 15px 50px rgba(0,0,0,0.3)' if st.session_state.dark_mode else '0 15px 50px rgba(0,0,0,0.05)'};
            transition: all 0.4s ease;
        }}
        
        [data-testid="stPlotlyChart"]:hover {{
            transform: scale(1.01);
            box-shadow: 0 20px 60px rgba(69, 183, 209, 0.2);
            border-color: #45B7D1;
        }}
        
        /* === TYPOGRAPHY === */
        h1 {{
            font-family: 'Righteous', cursive !important;
            font-size: 3.5rem !important;
            background: linear-gradient(135deg, #FF6B6B, #4ECDC4);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin: 2rem 0 1rem 0 !important;
            text-shadow: 0 10px 30px rgba(255, 107, 107, 0.3);
        }}
        
        h2 {{
            font-family: 'Poppins', sans-serif !important;
            font-weight: 800 !important;
            font-size: 2.2rem !important;
            color: {text_primary} !important;
            margin: 2.5rem 0 1.5rem 0 !important;
            position: relative;
            display: inline-block;
        }}
        
        h2::after {{
            content: '';
            position: absolute;
            bottom: -10px;
            left: 0;
            width: 50px;
            height: 4px;
            background: linear-gradient(90deg, #FF6B6B, #4ECDC4);
            border-radius: 2px;
            transition: width 0.3s ease;
        }}
        
        h2:hover::after {{
            width: 100%;
        }}
        
        h3 {{
            font-family: 'Poppins', sans-serif !important;
            font-weight: 700 !important;
            font-size: 1.6rem !important;
            background: linear-gradient(135deg, #45B7D1, #98D8C8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 1rem !important;
        }}
        
        p, span, div, label {{
            color: {text_primary} !important;
        }}
        
        /* === FORM ELEMENTS === */
        .stSelectbox label, .stMultiSelect label {{
            font-weight: 700 !important;
            color: #4ECDC4 !important;
            text-transform: uppercase;
            letter-spacing: 1px;
            font-size: 0.8rem !important;
        }}
        
        .stSelectbox > div > div, .stMultiSelect > div > div {{
            background: {bg_card} !important;
            border: 1px solid rgba(78, 205, 196, 0.5) !important;
            border-radius: 15px !important;
            backdrop-filter: blur(20px);
        }}
        
        .stCheckbox label {{
            color: {text_primary} !important;
            font-weight: 500;
        }}
        
        /* === EXPANDERS === */
        .streamlit-expanderHeader {{
            background: linear-gradient(135deg, rgba(255,107,107,0.1), rgba(78,205,196,0.1)) !important;
            border-radius: 15px !important;
            border: 1px solid rgba(78, 205, 196, 0.3) !important;
            font-weight: 600 !important;
            color: {text_primary} !important;
            transition: all 0.3s ease;
        }}
        
        .streamlit-expanderHeader:hover {{
            background: linear-gradient(135deg, rgba(255,107,107,0.2), rgba(78,205,196,0.2)) !important;
            transform: translateX(5px);
            box-shadow: 0 5px 15px rgba(78, 205, 196, 0.2);
        }}
        
        /* === DIVIDERS === */
        hr {{
            border: none;
            height: 2px;
            background: linear-gradient(90deg, transparent, #FF6B6B, #4ECDC4, #45B7D1, #4ECDC4, #FF6B6B, transparent);
            margin: 3rem 0;
            opacity: 0.5;
        }}
        
        /* === SCROLLBAR === */
        ::-webkit-scrollbar {{
            width: 10px;
        }}
        
        ::-webkit-scrollbar-track {{
            background: {bg_secondary};
        }}
        
        ::-webkit-scrollbar-thumb {{
            background: linear-gradient(135deg, #FF6B6B, #4ECDC4);
            border-radius: 5px;
        }}
        
        /* === SIDEBAR === */
        [data-testid="stSidebar"] {{
            background: {bg_secondary} !important;
            border-right: 1px solid rgba(255,255,255,0.1);
            backdrop-filter: blur(20px);
            min-width: 400px !important;
            max-width: 400px !important;
        }}
        
        </style>
    """, unsafe_allow_html=True)


def create_ultimate_navbar(athletes_df, medals_total_df, events_df):
    """Create ultra-creative navbar with filters below"""
    
    # Get unique values for filters
    all_countries = sorted(athletes_df['country'].dropna().unique())
    all_sports = sorted(events_df['sport'].dropna().unique())
    all_continents = sorted(athletes_df['continent'].dropna().unique())
    
    # Mode toggle in sidebar
    with st.sidebar:
        st.markdown("### Theme Mode")
        mode = st.toggle("Dark Mode", value=st.session_state.dark_mode, key="theme_toggle")
        if mode != st.session_state.dark_mode:
            st.session_state.dark_mode = mode
            st.rerun()
            
        st.markdown("---")
        st.markdown("### Global Filters")
    
        # Filters section in sidebar
        with st.expander("GEOGRAPHIC FILTERS", expanded=True):
            selected_countries = st.multiselect(
                "Countries",
                options=all_countries,
                default=[],
                key="navbar_countries"
            )
            selected_continents = st.multiselect(
                "Continents",
                options=all_continents,
                default=[],
                key="navbar_continents"
            )
        
        with st.expander("SPORTS FILTERS", expanded=True):
            selected_sports = st.multiselect(
                "Sports",
                options=all_sports,
                default=[],
                key="navbar_sports"
            )
        
        with st.expander("MEDAL FILTERS", expanded=True):
            col1, col2, col3 = st.columns(3)
            with col1:
                gold_checked = st.checkbox("Gold", value=True, key="navbar_gold")
            with col2:
                silver_checked = st.checkbox("Silver", value=True, key="navbar_silver")
            with col3:
                bronze_checked = st.checkbox("Bronze", value=True, key="navbar_bronze")
    
    # Prepare medal types
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


def create_ultimate_header(title, subtitle="", icon="🏅"):
    """Create spectacular animated header"""
    st.markdown(f"""
        <div class="creative-header">
            <div class="header-icon">{icon}</div>
            <h1 class="header-title">{title}</h1>
            <p class="header-subtitle">{subtitle}</p>
        </div>
    """, unsafe_allow_html=True)
