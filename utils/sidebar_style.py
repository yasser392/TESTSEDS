"""
Creative Sidebar Styling Utility
Provides consistent vibrant styling across all pages
"""

import streamlit as st

def apply_creative_sidebar_style():
    """Apply the creative vibrant sidebar and page styling"""
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700;900&family=Poppins:wght@300;400;600;700&display=swap');
        
        /* Dark vibrant background with animated gradient */
        .stApp {
            background: linear-gradient(135deg, #0F1419 0%, #1a1f2e 25%, #2d1b69 50%, #1a1f2e 75%, #0F1419 100%);
            background-size: 400% 400%;
            animation: gradientShift 15s ease infinite;
            font-family: 'Poppins', sans-serif;
        }
        
        @keyframes gradientShift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        /* CREATIVE SIDEBAR DESIGN */
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #FF6B35 0%, #F7931E 30%, #FDC830 60%, #F37335 100%) !important;
            border-right: 3px solid rgba(255, 255, 255, 0.3);
            box-shadow: 5px 0 20px rgba(255, 107, 53, 0.4);
        }
        
        section[data-testid="stSidebar"] > div {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
        }
        
        /* Sidebar header with Olympic effect */
        section[data-testid="stSidebar"]::before {
            content: "🏅 PARIS 2024";
            display: block;
            text-align: center;
            font-size: 1.8rem;
            font-weight: 900;
            padding: 20px;
            color: white;
            text-shadow: 2px 2px 8px rgba(0,0,0,0.5);
            font-family: 'Orbitron', sans-serif;
            letter-spacing: 3px;
            animation: pulse 2s ease-in-out infinite;
        }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }
        
        /* Sidebar widgets styling */
        section[data-testid="stSidebar"] .stSelectbox label,
        section[data-testid="stSidebar"] .stMultiSelect label,
        section[data-testid="stSidebar"] .stCheckbox label {
            color: white !important;
            font-weight: 600;
            font-size: 1.1rem;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.3);
        }
        
        section[data-testid="stSidebar"] .stSelectbox > div,
        section[data-testid="stSidebar"] .stMultiSelect > div {
            background: rgba(255, 255, 255, 0.9);
            border-radius: 10px;
            border: 2px solid rgba(255, 255, 255, 0.5);
        }
        
        /* Text colors */
        h1, h2, h3 {
            color: #FDC830 !important;
            font-family: 'Orbitron', sans-serif;
            text-shadow: 0 0 10px rgba(253, 200, 48, 0.3);
        }
        
        p, span, div {
            color: #E0E0E0;
        }
        
        /* Section dividers with neon effect */
        hr {
            border: none;
            height: 4px;
            background: linear-gradient(90deg, transparent, #FF6B35, #FDC830, #FF6B35, transparent);
            margin: 3rem 0;
            box-shadow: 0 0 10px rgba(255, 107, 53, 0.8);
        }
        </style>
    """, unsafe_allow_html=True)


def create_page_header(title, subtitle=""):
    """Create a creative header for each page"""
    st.markdown(f"""
        <div class="main-header">{title}</div>
        <div class="sub-header">{subtitle}</div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <style>
        .main-header {
            font-size: 3.5rem;
            font-weight: 900;
            text-align: center;
            background: linear-gradient(120deg, #FF6B35 0%, #FDC830 25%, #F7931E 50%, #FF6B35 75%, #FDC830 100%);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 0.5rem;
            animation: shineText 3s linear infinite;
            font-family: 'Orbitron', sans-serif;
            letter-spacing: 2px;
        }
        
        @keyframes shineText {
            to { background-position: 200% center; }
        }
        
        .sub-header {
            font-size: 1.5rem;
            text-align: center;
            color: #FDC830;
            margin-bottom: 2rem;
            font-weight: 400;
            text-shadow: 0 0 10px rgba(253, 200, 48, 0.5);
        }
        </style>
    """, unsafe_allow_html=True)
