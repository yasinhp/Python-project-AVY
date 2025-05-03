# Python-project-AVY
Course project of AAI-551C - Programming python - Real Estate study
Overview
GeoProp Analyzer is an interactive geospatial analysis tool for real estate data. It provides visualizations of property distributions, price trends, and investment potential across different zip codes. The application is built using Python with Dash for the web interface and Plotly for interactive visualizations.

Features
Interactive map showing property locations with filtering capabilities

Price per square foot visualization

Investment score predictions using an XGBoost model

12-month price projection trends

Filter by:

Zip code

Number of bedrooms/bathrooms/floors

Square footage range

Price range

File Structure

GeoProp-Analyzer/
├── data/
│   └── filtered_real_estate_data.csv       # Sample real estate data
├── gui/
│   ├── main_window.py                      # Main Dash application
│   └── xgboost_investment_model.pkl        # Trained XGBoost model
├── models/
│   ├── data_processor.py                   # Data processing utilities
│   └── real_estate.py                      # Property class definition
├── main.py                                 # Application entry point
└── README.md                               # This file
Installation
Clone the repository:

bash
git clone https://github.com/yourusername/GeoProp-Analyzer.git
cd GeoProp-Analyzer
Create and activate a virtual environment:

bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
Install dependencies:

bash
pip install dash plotly pandas scikit-learn xgboost joblib
Usage
Run the application:

bash
python main.py
Then open your web browser to http://127.0.0.1:8050/

How to Upload to GitHub
Initial Setup (if new repository):
Go to github.com and click the "+" icon in the top right, then select "New repository"

Name your repository (e.g., "GeoProp-Analyzer")

Choose public/private and initialize with a README (you can replace it with this one)

Click "Create repository"

Uploading Files:
On your local machine, navigate to your project folder

Initialize git if not already done:

bash
git init
Add all files:

bash
git add .
Commit changes:

bash
git commit -m "Initial commit with GeoProp Analyzer application"
Connect to your GitHub repository:

bash
git remote add origin https://github.com/yourusername/GeoProp-Analyzer.git
Push your code:

bash
git push -u origin main
Alternative Method via Web Interface:
On your GitHub repository page, click "Add file" → "Upload files"

Drag and drop your entire folder structure or select files manually

Click "Commit changes"

Dependencies
Python 3.7+

dash

plotly

pandas

scikit-learn

xgboost

joblib
