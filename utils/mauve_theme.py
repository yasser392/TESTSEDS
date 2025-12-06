"""
Unified Mauve/Purple Color Scheme
All pages use the same beautiful purple gradient
"""

MAUVE_CSS = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700;900&family=Poppins:wght@300;400;600;700&display=swap');
    
    /* Beautiful Mauve/Purple Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #9B59B6 0%, #8E44AD 25%, #BB8FCE 50%, #8E44AD 75%, #9B59B6 100%);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
        font-family: 'Poppins', sans-serif;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Mauve Sidebar - Same gradient */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #9B59B6 0%, #8E44AD 30%, #BB8FCE 60%, #8E44AD 90%, #9B59B6 100%) !important;
        border-right: 4px solid rgba(255, 255, 255, 0.4);
        box-shadow: 5px 0 30px rgba(0, 0, 0, 0.3);
    }
    
    section[data-testid="stSidebar"] > div {
        background: transparent;
    }
    
    /* Sidebar Olympic header */
    section[data-testid="stSidebar"]::before {
        content: "🏅 PARIS 2024 OLYMPICS";
        display: block;
        text-align: center;
        font-size: 1.6rem;
        font-weight: 900;
        padding: 25px 10px;
        color: white;
        text-shadow: 3px 3px 10px rgba(0,0,0,0.5);
        font-family: 'Orbitron', sans-serif;
        letter-spacing: 2px;
        background: rgba(0,0,0,0.2);
        border-radius: 15px;
        margin: 10px;
        animation: pulse 2s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.03); opacity: 0.95; }
    }
    
    /* Sidebar widgets */
    section[data-testid="stSidebar"] .stSelectbox label,
    section[data-testid="stSidebar"] .stMultiSelect label,
    section[data-testid="stSidebar"] .stCheckbox label {
        color: white !important;
        font-weight: 700;
        font-size: 1.05rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        background: rgba(0,0,0,0.15);
        padding: 8px;
        border-radius: 8px;
    }
    
    section[data-testid="stSidebar"] .stSelectbox > div,
    section[data-testid="stSidebar"] .stMultiSelect > div {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 12px;
        border: 3px solid rgba(255, 255, 255, 0.6);
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    /* Headers and text - White for contrast */
    h1, h2, h3 {
        color: white !important;
        font-family: 'Orbitron', sans-serif;
        text-shadow: 2px 2px 6px rgba(0,0,0,0.6);
    }
    
    p, span, div, label {
        color: white !important;
    }
    
    .stMarkdown {
        color: white !important;
    }
    
    /* Glassmorphism metric cards */
    .stMetric {
        background: linear-gradient(135deg, rgba(0, 0, 0, 0.4) 0%, rgba(255, 255, 255, 0.1) 100%);
        backdrop-filter: blur(20px);
        border-radius: 20px;
        border: 3px solid rgba(255, 255, 255, 0.5);
        padding: 25px;
        box-shadow: 
            0 10px 40px 0 rgba(0, 0, 0, 0.4),
            inset 0 0 30px rgba(255, 255, 255, 0.1);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    
    .stMetric:hover {
        transform: translateY(-12px) scale(1.05);
        box-shadow: 
            0 20px 60px 0 rgba(0, 0, 0, 0.5),
            0 0 40px rgba(255, 255, 255, 0.4);
        border-color: white;
    }
    
    [data-testid="stMetricLabel"] {
        font-weight: 700;
        font-size: 1.2rem;
        color: white;
        text-transform: uppercase;
        letter-spacing: 2px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    
    [data-testid="stMetricValue"] {
        font-size: 2.8rem;
        font-weight: 900;
        color: white;
        font-family: 'Orbitron', sans-serif;
        text-shadow: 3px 3px 8px rgba(0,0,0,0.6);
    }
    
    /* Section dividers */
    hr {
        border: none;
        height: 4px;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.8), transparent);
        margin: 3rem 0;
        box-shadow: 0 0 15px rgba(255, 255, 255, 0.5);
        animation: dividerGlow 2s ease-in-out infinite alternate;
    }
    
    @keyframes dividerGlow {
        from { box-shadow: 0 0 5px rgba(255, 255, 255, 0.3); }
        to { box-shadow: 0 0 20px rgba(255, 255, 255, 0.8); }
    }
    
    /* Chart containers */
    [data-testid="stPlotlyChart"] {
        background: rgba(0, 0, 0, 0.25);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 15px;
        border: 2px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 0 25px rgba(0, 0, 0, 0.3);
    }
    </style>
"""
