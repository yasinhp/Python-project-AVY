# GeoProp Analyzer - Real Estate Analysis Tool

## Overview
An interactive dashboard for analyzing real estate properties with geospatial visualization and investment scoring.

## Features
- Interactive map with property locations
- Price per square foot visualization
- XGBoost-based investment scoring
- 12-month price projections
- Filters for:
  - Zipcode
  - Bedrooms/Bathrooms/Floors
  - Square footage range
  - Price range

## Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Required Libraries
```bash
pip install dash plotly pandas scikit-learn xgboost joblib
```

### Detailed Dependency List
| Package | Version | Purpose |
|---------|---------|---------|
| dash | >=2.0.0 | Web framework |
| plotly | >=5.0.0 | Interactive visualizations |
| pandas | >=1.0.0 | Data processing |
| scikit-learn | >=1.0.0 | Model support |
| xgboost | >=1.5.0 | ML model |
| joblib | >=1.0.0 | Model serialization |

### Installation Steps
1. Clone the repository:
```bash
git clone https://github.com/yourusername/GeoProp-Analyzer.git
cd GeoProp-Analyzer
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## File Structure
```
GeoProp-Analyzer/
├── data/
│   └── filtered_real_estate_data.csv       # Sample dataset
├── gui/
│   ├── main_window.py                      # Dashboard implementation
│   └── xgboost_investment_model.pkl        # Trained model
├── models/
│   ├── data_processor.py                   # Data handling
│   └── real_estate.py                      # Property class
├── main.py                                 # Entry point
└── README.md                               # Documentation
```

## Running the Application
1. Start the server:
```bash
python main.py
```

2. Access the dashboard:
- Open your web browser
- Navigate to: `http://localhost:8050/`

## Troubleshooting
If the page doesn't load:
1. Verify the server is running (you should see output in your terminal)
2. Check your firewall settings
3. Try accessing `http://127.0.0.1:8050/` instead
4. Ensure no other application is using port 8050

## Notes
- The application requires the model file (`xgboost_investment_model.pkl`) to be present in the gui folder
- Sample data should be placed in the data folder
- First run may take longer as it loads the ML model
