"""
Creative Theme System for Paris 2024 Olympic Dashboard
Premium typography, modern visual effects, and vibrant Olympic-inspired design
"""
import streamlit as st


def apply_creative_global_styles():
    """Apply creative global styling with premium fonts and visual effects"""
    st.markdown("""
        <style>
        /* Import Premium Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Righteous&family=JetBrains+Mono:wght@400;500;600;700&display=swap');
        @import url('https://api.fontshare.com/v2/css?f[]=clash-display@200,400,700,600,500,300&display=swap');
        
        /* Global Reset & Base Styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        /* Main App Background - Animated Gradient */
        .stApp {
            background: linear-gradient(135deg, 
                #0A0E27 0%, 
                #1A1F3A 20%, 
                #2D1B4E 40%, 
                #1A1F3A 60%, 
                #0A0E27 80%, 
                #1A1F3A 100%);
            background-size: 400% 400%;
            animation: cosmicGradient 20s ease infinite;
            font-family: 'Space Grotesk', sans-serif;
            color: #E8E8E8;
        }
        
        @keyframes cosmicGradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        /* Hide Streamlit Branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Scrollbar Styling */
        ::-webkit-scrollbar {
            width: 12px;
        }
        
        ::-webkit-scrollbar-track {
            background: rgba(10, 14, 39, 0.5);
        }
        
        ::-webkit-scrollbar-thumb {
            background: linear-gradient(180deg, #0066FF, #9D00FF);
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(157, 0, 255, 0.5);
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(180deg, #00FF87, #00D9FF);
        }
        
        /* Typography System */
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Clash Display', 'Space Grotesk', sans-serif !important;
            font-weight: 700 !important;
            background: linear-gradient(135deg, #00D9FF 0%, #0066FF 50%, #9D00FF 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            letter-spacing: -0.02em;
            line-height: 1.2;
        }
        
        h1 {
            font-size: 3.5rem !important;
            font-weight: 900 !important;
        }
        
        h2 {
            font-size: 2.5rem !important;
        }
        
        h3 {
            font-size: 1.8rem !important;
        }
        
        p, span, div, label {
            font-family: 'Space Grotesk', sans-serif !important;
            color: #E8E8E8 !important;
            line-height: 1.6;
        }
        
        /* Premium Glassmorphic Cards */
        .element-container, [data-testid="stVerticalBlock"] > div {
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(30px);
            -webkit-backdrop-filter: blur(30px);
            border-radius: 24px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 0;
            transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
        }
        
        /* Enhanced Metric Cards */
        .stMetric {
            background: linear-gradient(135deg, 
                rgba(0, 102, 255, 0.1) 0%, 
                rgba(157, 0, 255, 0.1) 100%);
            backdrop-filter: blur(40px);
            border-radius: 28px;
            border: 2px solid transparent;
            background-clip: padding-box;
            position: relative;
            padding: 2rem !important;
            box-shadow: 
                0 8px 32px rgba(0, 102, 255, 0.2),
                0 0 80px rgba(157, 0, 255, 0.1),
                inset 0 0 40px rgba(255, 255, 255, 0.05);
            transition: all 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
            overflow: hidden;
        }
        
        .stMetric::before {
            content: '';
            position: absolute;
            top: -2px;
            left: -2px;
            right: -2px;
            bottom: -2px;
            background: linear-gradient(45deg, 
                #0066FF, #9D00FF, #00FF87, #FFD700, #FF6B35, #0066FF);
            background-size: 400% 400%;
            border-radius: 28px;
            z-index: -1;
            animation: rainbowBorder 8s ease infinite;
            opacity: 0;
            transition: opacity 0.5s;
        }
        
        .stMetric:hover::before {
            opacity: 1;
        }
        
        @keyframes rainbowBorder {
            0%, 100% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
        }
        
        .stMetric:hover {
            transform: translateY(-15px) scale(1.05);
            box-shadow: 
                0 20px 60px rgba(0, 102, 255, 0.4),
                0 0 120px rgba(157, 0, 255, 0.3),
                inset 0 0 60px rgba(255, 255, 255, 0.1);
        }
        
        [data-testid="stMetricLabel"] {
            font-family: 'Space Grotesk', sans-serif !important;
            font-weight: 600 !important;
            font-size: 1rem !important;
            color: #00D9FF !important;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            text-shadow: 0 0 20px rgba(0, 217, 255, 0.5);
        }
        
        [data-testid="stMetricValue"] {
            font-family: 'JetBrains Mono', monospace !important;
            font-size: 3.5rem !important;
            font-weight: 700 !important;
            background: linear-gradient(135deg, #FFD700 0%, #FF6B35 50%, #FF00FF 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-shadow: 0 0 40px rgba(255, 215, 0, 0.3);
            animation: numberGlow 3s ease-in-out infinite;
        }
        
        @keyframes numberGlow {
            0%, 100% { filter: brightness(1); }
            50% { filter: brightness(1.3); }
        }
        
        /* Plotly Chart Containers - Neon Glow */
        [data-testid="stPlotlyChart"] {
            background: rgba(10, 14, 39, 0.6);
            backdrop-filter: blur(20px);
            border-radius: 24px;
            padding: 1.5rem;
            border: 1px solid rgba(0, 217, 255, 0.2);
            box-shadow: 
                0 8px 32px rgba(0, 0, 0, 0.4),
                0 0 60px rgba(0, 102, 255, 0.2),
                inset 0 0 30px rgba(0, 217, 255, 0.05);
            transition: all 0.4s ease;
        }
        
        [data-testid="stPlotlyChart"]:hover {
            transform: scale(1.02);
            border-color: rgba(0, 217, 255, 0.5);
            box-shadow: 
                0 12px 48px rgba(0, 0, 0, 0.6),
                0 0 100px rgba(0, 102, 255, 0.4),
                inset 0 0 50px rgba(0, 217, 255, 0.1);
        }
        
        /* Section Dividers - Neon Glow */
        hr {
            border: none;
            height: 2px;
            background: linear-gradient(90deg, 
                transparent 0%, 
                #0066FF 20%, 
                #00D9FF 40%, 
                #00FF87 50%, 
                #FFD700 60%, 
                #FF6B35 80%, 
                transparent 100%);
            margin: 3rem 0;
            box-shadow: 
                0 0 30px rgba(0, 217, 255, 0.8),
                0 0 60px rgba(0, 102, 255, 0.5);
            animation: neonPulse 3s ease-in-out infinite;
            position: relative;
        }
        
        @keyframes neonPulse {
            0%, 100% { 
                opacity: 0.6;
                box-shadow: 0 0 20px rgba(0, 217, 255, 0.6);
            }
            50% { 
                opacity: 1;
                box-shadow: 0 0 60px rgba(0, 217, 255, 1);
            }
        }
        
        /* Buttons & Interactive Elements */
        .stButton > button {
            background: linear-gradient(135deg, #0066FF 0%, #9D00FF 100%);
            color: white;
            font-family: 'Space Grotesk', sans-serif;
            font-weight: 600;
            border: none;
            border-radius: 16px;
            padding: 0.8rem 2rem;
            font-size: 1rem;
            letter-spacing: 0.05em;
            text-transform: uppercase;
            box-shadow: 
                0 8px 24px rgba(0, 102, 255, 0.4),
                0 0 40px rgba(157, 0, 255, 0.3);
            transition: all 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
            cursor: pointer;
        }
        
        .stButton > button:hover {
            transform: translateY(-5px) scale(1.05);
            box-shadow: 
                0 15px 40px rgba(0, 102, 255, 0.6),
                0 0 80px rgba(157, 0, 255, 0.5);
            background: linear-gradient(135deg, #00FF87 0%, #00D9FF 100%);
        }
        
        /* Select Boxes & Input Fields */
        .stSelectbox, .stMultiSelect, .stTextInput {
            font-family: 'Space Grotesk', sans-serif !important;
        }
        
        .stSelectbox label, .stMultiSelect label, .stTextInput label {
            color: #00D9FF !important;
            font-weight: 600 !important;
            text-shadow: 0 0 10px rgba(0, 217, 255, 0.5);
        }
        
        /* Checkbox Styling */
        .stCheckbox label {
            color: #E8E8E8 !important;
            font-family: 'Space Grotesk', sans-serif !important;
        }
        
        /* Expander Styling */
        .streamlit-expanderHeader {
            background: rgba(0, 102, 255, 0.1) !important;
            border-radius: 12px !important;
            border: 1px solid rgba(0, 217, 255, 0.3) !important;
            font-family: 'Space Grotesk', sans-serif !important;
            font-weight: 600 !important;
            color: #00D9FF !important;
            transition: all 0.3s ease;
        }
        
        .streamlit-expanderHeader:hover {
            background: rgba(0, 102, 255, 0.2) !important;
            border-color: rgba(0, 217, 255, 0.6) !important;
            box-shadow: 0 0 30px rgba(0, 217, 255, 0.3);
        }
        
        /* Dataframe Styling */
        .stDataFrame {
            border-radius: 16px;
            overflow: hidden;
            box-shadow: 0 8px 32px rgba(0, 102, 255, 0.2);
        }
        
        /* Tabs Styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 1rem;
            background: rgba(0, 0, 0, 0.3);
            padding: 0.5rem;
            border-radius: 16px;
        }
        
        .stTabs [data-baseweb="tab"] {
            font-family: 'Space Grotesk', sans-serif !important;
            font-weight: 600;
            background: rgba(0, 102, 255, 0.1);
            border-radius: 12px;
            color: #00D9FF;
            border: 1px solid rgba(0, 217, 255, 0.3);
            transition: all 0.3s ease;
        }
        
        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, #0066FF, #9D00FF) !important;
            color: white !important;
            box-shadow: 0 0 30px rgba(157, 0, 255, 0.6);
        }
        </style>
    """, unsafe_allow_html=True)


def create_hero_section(title, subtitle="", emoji="🏅"):
    """Create an animated hero section with particles effect"""
    st.markdown(f"""
        <div class="hero-section">
            <div class="hero-particles"></div>
            <div class="hero-content">
                <div class="hero-emoji">{emoji}</div>
                <h1 class="hero-title">{title}</h1>
                <p class="hero-subtitle">{subtitle}</p>
            </div>
        </div>
        
        <style>
        .hero-section {{
            position: relative;
            text-align: center;
            padding: 4rem 2rem;
            margin: -2rem -2rem 3rem -2rem;
            background: linear-gradient(135deg, 
                rgba(0, 102, 255, 0.1) 0%, 
                rgba(157, 0, 255, 0.1) 50%,
                rgba(0, 255, 135, 0.1) 100%);
            border-radius: 0 0 40px 40px;
            overflow: hidden;
            border-bottom: 2px solid rgba(0, 217, 255, 0.3);
        }}
        
        .hero-emoji {{
            font-size: 5rem;
            animation: floatEmoji 3s ease-in-out infinite;
            filter: drop-shadow(0 0 30px rgba(255, 215, 0, 0.6));
        }}
        
        @keyframes floatEmoji {{
            0%, 100% {{ transform: translateY(0px) rotate(0deg); }}
            50% {{ transform: translateY(-20px) rotate(5deg); }}
        }}
        
        .hero-title {{
            font-size: 4.5rem !important;
            font-family: 'Clash Display', sans-serif !important;
            font-weight: 900 !important;
            margin: 1rem 0 !important;
            background: linear-gradient(135deg, #FFD700 0%, #FF6B35 25%, #FF00FF 50%, #0066FF 75%, #00FF87 100%);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: rainbowShift 8s linear infinite, titlePulse 2s ease-in-out infinite;
            text-shadow: 0 0 80px rgba(255, 215, 0, 0.5);
            letter-spacing: -0.03em;
        }}
        
        @keyframes rainbowShift {{
            0% {{ background-position: 0% 50%; }}
            100% {{ background-position: 200% 50%; }}
        }}
        
        @keyframes titlePulse {{
            0%, 100% {{ transform: scale(1); }}
            50% {{ transform: scale(1.02); }}
        }}
        
        .hero-subtitle {{
            font-size: 1.3rem !important;
            font-family: 'Space Grotesk', sans-serif !important;
            color: #00D9FF !important;
            font-weight: 500 !important;
            text-shadow: 0 0 20px rgba(0, 217, 255, 0.5);
            animation: subtitleFade 2s ease-in-out infinite;
        }}
        
        @keyframes subtitleFade {{
            0%, 100% {{ opacity: 0.8; }}
            50% {{ opacity: 1; }}
        }}
        
        .hero-particles {{
            position: absolute;
            width: 100%;
            height: 100%;
            top: 0;
            left: 0;
            overflow: hidden;
            z-index: 0;
        }}
        
        .hero-content {{
            position: relative;
            z-index: 1;
        }}
        </style>
    """, unsafe_allow_html=True)


def create_neon_divider():
    """Create a neon glowing divider"""
    st.markdown("""
        <div class="neon-divider-container">
            <div class="neon-divider"></div>
            <div class="neon-orb"></div>
        </div>
        
        <style>
        .neon-divider-container {
            position: relative;
            height: 40px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 3rem 0;
        }
        
        .neon-divider {
            width: 100%;
            height: 3px;
            background: linear-gradient(90deg, 
                transparent 0%,
                #0066FF 20%,
                #00D9FF 40%,
                #00FF87 50%,
                #FFD700 60%,
                #FF6B35 80%,
                transparent 100%);
            box-shadow: 
                0 0 20px rgba(0, 217, 255, 0.8),
                0 0 40px rgba(0, 102, 255, 0.6),
                0 0 60px rgba(0, 255, 135, 0.4);
            animation: dividerPulse 3s ease-in-out infinite;
        }
        
        @keyframes dividerPulse {
            0%, 100% { opacity: 0.6; transform: scaleX(1); }
            50% { opacity: 1; transform: scaleX(1.02); }
        }
        
        .neon-orb {
            position: absolute;
            width: 20px;
            height: 20px;
            background: radial-gradient(circle, #00FF87, #00D9FF);
            border-radius: 50%;
            box-shadow: 
                0 0 30px rgba(0, 255, 135, 1),
                0 0 60px rgba(0, 217, 255, 0.8);
            animation: orbFloat 4s ease-in-out infinite;
        }
        
        @keyframes orbFloat {
            0%, 100% { transform: translateX(-100px) scale(1); }
            50% { transform: translateX(100px) scale(1.2); }
        }
        </style>
    """, unsafe_allow_html=True)
