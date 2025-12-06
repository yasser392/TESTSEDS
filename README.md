# 🏅 Paris 2024 Olympic Games Dashboard

A comprehensive multi-page Streamlit dashboard for analyzing the Paris 2024 Olympic Summer Games data, created for the LA28 Volunteer Selection Challenge.

## 📋 Overview

This interactive dashboard provides deep insights into the Paris 2024 Olympics through:
- **Data Cleaning & Preprocessing**: Handles missing values, calculates athlete ages, and adds continent mappings
- **Multi-Page Structure**: 4 dedicated pages for different analytical perspectives
- **Interactive Visualizations**: 20+ charts including choropleth maps, sunbursts, treemaps, and Gantt timelines
- **Global Filters**: Consistent filtering across pages by Country, Sport, Medal Type, and Continent

## 🚀 Quick Start

### Installation

1. Clone or download this repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

### Running the Dashboard

Navigate to the project directory and run:

```bash
streamlit run 1_🏠_Overview.py
```

The dashboard will open in your default web browser at `http://localhost:8501`

## 📊 Dashboard Pages

### 1. 🏠 Overview (Main Page)
- **KPI Metrics**: Total Athletes, Countries, Sports, Medals, Events
- **Global Medal Distribution**: Pie/Donut chart showing Gold, Silver, Bronze distribution
- **Top 10 Medal Standings**: Horizontal bar chart of leading countries

### 2. 🗺️ Global Analysis
- **World Medal Map**: Interactive choropleth showing medal counts by country
- **Medal Hierarchy**: Sunburst and Treemap visualizations (Continent → Country → Medal Type)
- **Continent Comparison**: Grouped bar charts for continental and country-level analysis

### 3. 👤 Athlete Performance
- **Athlete Profile Card**: Searchable athlete details with personal information
- **Age Distribution**: Violin plots showing age ranges by sport and gender
- **Gender Distribution**: Pie and bar charts analyzing participation by continent
- **Top Athletes**: Ranking of athletes by medal count

### 4. 🏟️ Sports and Events
- **Event Schedule**: Interactive Gantt chart/timeline of competitions
- **Medal Count by Sport**: Treemap visualization of sports performance
- **Venue Map**: Interactive map showing Olympic venue locations in Paris
- **Event Statistics**: Key metrics about sports and venues

## 🎯 Key Features

### Data Cleaning & Preprocessing
- **Missing Value Handling**: Replaces 0.0 values in height/weight with NaN
- **Age Calculation**: Computes athlete ages relative to Olympics start date (July 26, 2024)
- **Continent Mapping**: Comprehensive NOC code to continent mapping for 200+ countries
- **Data Validation**: Ensures data quality across all datasets

### Global Filters (Sidebar)
Available on all pages:
- **Country Selection**: Multi-select filter for specific nations
- **Sport Selection**: Filter by Olympic sports
- **Continent Selection**: ⭐ **Creativity Challenge** - unique continent-level filtering
- **Medal Type**: Checkboxes for Gold, Silver, Bronze medals

### Technologies Used
- **Streamlit**: Interactive web application framework
- **Pandas**: Data manipulation and analysis
- **Plotly**: Advanced interactive visualizations
- **NumPy**: Numerical computations

## 📁 Project Structure

```
TESTSEDS/
├── 1_🏠_Overview.py              # Main landing page
├── pages/
│   ├── 2_🗺️_Global_Analysis.py   # Geographic analysis
│   ├── 3_👤_Athlete_Performance.py # Athlete-centric views
│   └── 4_🏟️_Sports_and_Events.py  # Sports and venues
├── utils/
│   ├── data_loader.py            # Cached data loading
│   ├── data_cleaning.py          # Preprocessing functions
│   └── filter_helpers.py         # Shared filter logic
├── *.csv                         # Olympic datasets
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## 🎨 Design Choices

### Multi-Page Architecture
- Streamlit's native multi-page app feature for clean navigation
- Each page focuses on a specific analytical perspective
- Consistent layout and styling across all pages

### Data Processing
- **Caching Strategy**: `@st.cache_data` decorator for optimal performance
- **Modular Design**: Separated data loading, cleaning, and filtering logic
- **Continent Mapping**: Custom dictionary-based mapping for geographic analysis

### Visualization Strategy
- **Color Consistency**: Medal colors (Gold: #FFD700, Silver: #C0C0C0, Bronze: #CD7F32)
- **Interactive Charts**: Hover details, zoom, pan capabilities on all visualizations
- **Responsive Layout**: Streamlit columns and containers for optimal space usage

## 📊 Data Source

Dataset: [Paris 2024 Olympic Summer Games](https://www.kaggle.com/datasets/piterfm/paris-2024-olympic-summer-games)

Includes:
- `athletes.csv`: 11,000+ athlete profiles
- `medals_total.csv`: Medal counts by country
- `events.csv`: 330+ Olympic events
- `venues.csv`: Olympic venue information
- And more...

## 🏆 Creativity Features

1. **Continent Filter**: Added as a global filter enabling continent-level analysis across all pages
2. **Age Calculation**: Dynamic age computation relative to Olympics start date
3. **Hierarchical Visualizations**: Drill-down capability in sunburst and treemap charts
4. **Athlete Search**: Type-ahead search functionality for athlete profiles
5. **Comprehensive Data Cleaning**: Robust preprocessing pipeline handling edge cases

## 👥 Team Information

This project was created for the LA28 Volunteer Selection Challenge by demonstrating proficiency in:
- Data Science & Analytics
- Streamlit Dashboard Development
- Data Cleaning & Preprocessing
- Interactive Visualization Design

## 📝 License

This project uses publicly available Olympic Games data from Kaggle for educational and demonstration purposes.

## 🙏 Acknowledgments

- Paris 2024 Olympics for the incredible event
- Kaggle community for the comprehensive dataset
- Streamlit team for the amazing framework
- LA28 organizing committee for this opportunity

---

**Created with ❤️ for the LA28 Volunteer Selection Challenge**
