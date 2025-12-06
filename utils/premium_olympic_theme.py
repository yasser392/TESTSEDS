"""
Premium Olympic Theme for Paris 2024 Dashboard
Clean, professional, and truly creative design with proper navigation
"""
import streamlit as st


def apply_premium_olympic_theme():
    """Apply premium Olympic-themed styling"""
    st.markdown("""
        <style>
        /* Import Premium Fonts - Clean & Modern */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Montserrat:wght@400;500;600;700;800;900&display=swap');
        
        /* === GLOBAL RESET === */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        /* Hide Streamlit Branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header[data-testid="stHeader"] {display: none;}
        
        /* === MAIN BACKGROUND === */
        .stApp {
            background: linear-gradient(135deg, #F8F9FA 0%, #E8EAF6 50%, #F3E5F5 100%);
            font-family: 'Inter', sans-serif;
        }
        
        /* === NAVIGATION BAR === */
        .olympic-navbar {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            height: 70px;
            background: linear-gradient(135deg, #5E35B1 0%, #673AB7 50%, #7E57C2 100%);
            box-shadow: 0 4px 20px rgba(94, 53, 177, 0.3);
            z-index: 1000;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 3rem;
        }
        
        .nav-logo {
            display: flex;
            align-items: center;
            gap: 12px;
        }
        
        .nav-logo-text {
            font-family: 'Montserrat', sans-serif;
            font-size: 1.4rem;
            font-weight: 800;
            color: white;
            letter-spacing: 1px;
        }
        
        .nav-links {
            display: flex;
            gap: 2rem;
            align-items: center;
        }
        
        .nav-link {
            color: white;
            text-decoration: none;
            font-weight: 600;
            font-size: 0.95rem;
            padding: 8px 16px;
            border-radius: 8px;
            transition: all 0.3s ease;
        }
        
        .nav-link:hover {
            background: rgba(255, 255, 255, 0.2);
            transform: translateY(-2px);
        }
        
        /* === MAIN CONTENT AREA === */
        .main .block-container {
            padding-top: 90px !important;
            max-width: 1400px;
            padding-left: 2rem;
            padding-right: 2rem;
        }
        
        /* === TYPOGRAPHY === */
        h1 {
            font-family: 'Montserrat', sans-serif !important;
            font-weight: 900 !important;
            font-size: 3rem !important;
            color: #5E35B1 !important;
            margin-bottom: 1rem !important;
        }
        
        h2 {
            font-family: 'Montserrat', sans-serif !important;
            font-weight: 700 !important;
            font-size: 2rem !important;
            color: #673AB7 !important;
            margin: 2rem 0 1rem 0 !important;
        }
        
        h3 {
            font-family: 'Montserrat', sans-serif !important;
            font-weight: 600 !important;
            font-size: 1.5rem !important;
            color: #7E57C2 !important;
            margin: 1.5rem 0 1rem 0 !important;
        }
        
        p, span, div, label {
            font-family: 'Inter', sans-serif !important;
            color: #37474F !important;
        }
        
        /* === PREMIUM METRIC CARDS === */
        .stMetric {
            background: white;
            border-radius: 16px;
            padding: 1.5rem !important;
            box-shadow: 0 4px 16px rgba(94, 53, 177, 0.1);
            border: 2px solid transparent;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
        }
        
        .stMetric::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, #5E35B1, #E91E63, #FFC107, #4CAF50, #2196F3);
            opacity: 0;
            transition: opacity 0.3s ease;
        }
        
        .stMetric:hover {
            transform: translateY(-8px);
            box-shadow: 0 12px 32px rgba(94, 53, 177, 0.2);
            border-color: #7E57C2;
        }
        
        .stMetric:hover::before {
            opacity: 1;
        }
        
        [data-testid="stMetricLabel"] {
            font-family: 'Inter', sans-serif !important;
            font-weight: 600 !important;
            font-size: 0.85rem !important;
            color: #7E57C2 !important;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        [data-testid="stMetricValue"] {
            font-family: 'Montserrat', sans-serif !important;
            font-size: 2.5rem !important;
            font-weight: 800 !important;
            color: #5E35B1 !important;
        }
        
        /* === CHARTS & VISUALIZATIONS === */
        [data-testid="stPlotlyChart"] {
            background: white;
            border-radius: 16px;
            padding: 1.5rem;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
            transition: all 0.3s ease;
        }
        
        [data-testid="stPlotlyChart"]:hover {
            box-shadow: 0 8px 24px rgba(94, 53, 177, 0.15);
        }
        
        /* === FILTER PANEL === */
        .filter-panel {
            background: white;
            border-radius: 16px;
            padding: 1.5rem;
            margin-bottom: 2rem;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
            border-left: 4px solid #5E35B1;
        }
        
        .filter-title {
            font-family: 'Montserrat', sans-serif;
            font-size: 1.2rem;
            font-weight: 700;
            color: #5E35B1;
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        /* === FORM ELEMENTS === */
        .stSelectbox label, .stMultiSelect label {
            font-family: 'Inter', sans-serif !important;
            font-weight: 600 !important;
            color: #5E35B1 !important;
            font-size: 0.9rem !important;
        }
        
        .stSelectbox > div, .stMultiSelect > div {
            border-radius: 10px !important;
            border: 2px solid #E0E0E0 !important;
            transition: all 0.3s ease;
        }
        
        .stSelectbox > div:hover, .stMultiSelect > div:hover {
            border-color: #7E57C2 !important;
        }
        
        .stCheckbox label {
            font-family: 'Inter', sans-serif !important;
            font-weight: 500 !important;
            color: #37474F !important;
        }
        
        /* === BUTTONS === */
        .stButton > button {
            background: linear-gradient(135deg, #5E35B1, #7E57C2);
            color: white;
            font-family: 'Inter', sans-serif;
            font-weight: 600;
            border: none;
            border-radius: 10px;
            padding: 0.7rem 2rem;
            transition: all 0.3s ease;
            box-shadow: 0 4px 12px rgba(94, 53, 177, 0.3);
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(94, 53, 177, 0.4);
        }
        
        /* === EXPANDERS === */
        .streamlit-expanderHeader {
            background: linear-gradient(135deg, #F3E5F5, #EDE7F6) !important;
            border-radius: 12px !important;
            border: 2px solid #E1BEE7 !important;
            font-family: 'Inter', sans-serif !important;
            font-weight: 600 !important;
            color: #5E35B1 !important;
            padding: 1rem !important;
            transition: all 0.3s ease;
        }
        
        .streamlit-expanderHeader:hover {
            background: linear-gradient(135deg, #EDE7F6, #D1C4E9) !important;
            border-color: #CE93D8 !important;
        }
        
        /* === DIVIDERS === */
        hr {
            border: none;
            height: 2px;
            background: linear-gradient(90deg, transparent, #7E57C2, transparent);
            margin: 2.5rem 0;
        }
        
        /* === SIDEBAR (for navigation) === */
        section[data-testid="stSidebar"] {
            background: white;
            border-right: 1px solid #E0E0E0;
        }
        
        section[data-testid="stSidebar"] .stMarkdown {
            color: #37474F !important;
        }
        
        /* === OLYMPIC RINGS DECORATION === */
        .olympic-rings-decor {
            display: inline-flex;
            gap: 6px;
            font-size: 1.5rem;
            filter: drop-shadow(0 2px 4px rgba(0,0,0,0.1));
        }
        
        /* === DATA TABLES === */
        .stDataFrame {
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        }
        
        /* === TABS === */
        .stTabs [data-baseweb="tab-list"] {
            gap: 1rem;
            background: white;
            padding: 0.5rem;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
        }
        
        .stTabs [data-baseweb="tab"] {
            font-family: 'Inter', sans-serif !important;
            font-weight: 600;
            color: #5E35B1;
            border-radius: 8px;
            padding: 0.5rem 1.5rem;
        }
        
        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, #5E35B1, #7E57C2) !important;
            color: white !important;
        }
        
        /* === SCROLLBAR === */
        ::-webkit-scrollbar {
            width: 10px;
            height: 10px;
        }
        
        ::-webkit-scrollbar-track {
            background: #F5F5F5;
        }
        
        ::-webkit-scrollbar-thumb {
            background: linear-gradient(135deg, #5E35B1, #7E57C2);
            border-radius: 10px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(135deg, #4A148C, #5E35B1);
        }
        </style>
    """, unsafe_allow_html=True)


def create_navigation_bar(current_page="Overview"):
    """Create professional navigation bar"""
    pages = {
        "🏠 Overview": "1_🏠_Overview.py",
        "🗺️ Global Analysis": "pages/2_🗺️_Global_Analysis.py",
        "👤 Athletes": "pages/3_👤_Athlete_Performance.py",
        "🏟️ Sports & Events": "pages/4_🏟️_Sports_and_Events.py",
        "🎨 3D Insights": "pages/5_🎨_3D_Insights.py"
    }
    
    st.markdown(f"""
        <div class="olympic-navbar">
            <div class="nav-logo">
                <span class="olympic-rings-decor">🔵🟡⚫🟢🔴</span>
                <span class="nav-logo-text">PARIS 2024</span>
            </div>
            <div class="nav-links">
                <a class="nav-link" href="/" target="_self">🏠 Home</a>
                <a class="nav-link" href="#analysis" target="_self">📊 Analysis</a>
                <a class="nav-link" href="#athletes" target="_self">👤 Athletes</a>
                <a class="nav-link" href="#sports" target="_self">🏟️ Sports</a>
                <a class="nav-link" href="#insights" target="_self">🎨 Insights</a>
            </div>
        </div>
    """, unsafe_allow_html=True)


def create_filter_section():
    """Create clean filter panel"""
    st.markdown("""
        <div class="filter-panel">
            <div class="filter-title">🎯 Filter Dashboard Data</div>
        </div>
    """, unsafe_allow_html=True)


def create_page_header(title, subtitle="", icon="🏅"):
    """Create clean page header"""
    st.markdown(f"""
        <div style="text-align: center; margin: 2rem 0 3rem 0;">
            <div style="font-size: 4rem; margin-bottom: 1rem;">{icon}</div>
            <h1 style="margin: 0;">{title}</h1>
            <p style="font-size: 1.2rem; color: #7E57C2; font-weight: 500; margin-top: 0.5rem;">{subtitle}</p>
        </div>
    """, unsafe_allow_html=True)
