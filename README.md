# GeoProp Analyzer

## Overview
GeoProp Analyzer is an interactive geospatial analysis tool for real estate data. It provides visualizations of property distributions, price trends, and investment potential across different zip codes.

## Features
- Interactive map with property locations
- Price per square foot visualization
- Investment score predictions (XGBoost model)
- 12-month price projections
- Filter by zipcode, bedrooms, bathrooms, floors, sqft, and price

## File Structure
```
GeoProp-Analyzer/
├── data/
│   └── filtered_real_estate_data.csv
├── gui/
│   ├── main_window.py
│   └── xgboost_investment_model.pkl
├── models/
│   ├── data_processor.py
│   └── real_estate.py
├── main.py
└── README.md
```

## Installation
```bash
git clone https://github.com/yourusername/GeoProp-Analyzer.git
cd GeoProp-Analyzer
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install dash plotly pandas scikit-learn xgboost joblib
```

## Usage
```bash
python main.py
```
Then visit http://127.0.0.1:8050/
