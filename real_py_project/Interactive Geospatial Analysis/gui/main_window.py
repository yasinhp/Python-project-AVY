import os
import sys
import pandas as pd
import joblib
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# === Load model ===
# Base path logic (works in .exe too)
base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

# Load model
model_path = os.path.join(base_path, 'xgboost_investment_model.pkl')
model = joblib.load(model_path)

# Load data
csv_path = os.path.join(os.path.dirname(base_path), 'data', 'filtered_real_estate_data.csv')
df = pd.read_csv(csv_path)
df["price_per_sqft"] = df["price"] / df["sqft_living"]
df["address"] = df["address"]  # Address already exists

zipcodes = sorted(df["zipcode"].unique())


# === Initialize Dash app ===
app = Dash(__name__)
app.title = "GeoProp Analyzer"

app.layout = html.Div([
    html.H1("GeoProp Analyzer", style={"textAlign": "center"}),

    html.Label("Select Zipcode:"),
    dcc.Dropdown(
        id='zipcode-dropdown',
        options=[{"label": str(z), "value": z} for z in zipcodes],
        value=zipcodes[0]
    ),

    html.Label("Bedrooms:"),
    dcc.Slider(
        id='bedroom-slider',
        min=0, max=10, step=1, value=0,
        marks={i: {'label': 'Any' if i == 0 else str(i)} for i in range(0, 11)},
        tooltip={"placement": "bottom", "always_visible": True}
    ),

    html.Label("Bathrooms:"),
    dcc.Slider(
        id='bathroom-slider',
        min=0, max=10, step=1, value=0,
        marks={i: {'label': 'Any' if i == 0 else str(i)} for i in range(0, 11)},
        tooltip={"placement": "bottom", "always_visible": True}
    ),

    html.Label("Floors:"),
    dcc.Slider(
        id='floor-slider',
        min=0, max=4, step=1, value=0,
        marks={i: {'label': 'Any' if i == 0 else str(i)} for i in range(0, 5)},
        tooltip={"placement": "bottom", "always_visible": True}
    ),

    html.Label("Sqft Range:"),
    dcc.RangeSlider(
        id='sqft-slider',
        min=500, max=10000, step=100,
        value=[1000, 3000],
        marks={i: str(i) for i in range(500, 10001, 2000)},
        tooltip={"placement": "bottom", "always_visible": True}
    ),

    html.Label("Price Range:"),
    dcc.RangeSlider(
        id='price-slider',
        min=50000, max=3000000, step=50000,
        value=[300000, 1000000],
        marks={i: str(i//1000) + 'K' for i in range(50000, 3000001, 500000)},
        tooltip={"placement": "bottom", "always_visible": True}
    ),

    html.Label("Options:"),
    dcc.Checklist(
        id='price-toggle',
        options=[
            {'label': 'Show Price per Sqft', 'value': 'pps'},
            {'label': 'Use Predicted Investment Score', 'value': 'pred'}
        ],
        value=[]
    ),

    html.Br(),

    dcc.Graph(id='scatter-plot', style={'height': '800px'}),
    html.Hr(),
    dcc.Graph(id='trend-line')
])

@app.callback(
    Output('scatter-plot', 'figure'),
    Input('zipcode-dropdown', 'value'),
    Input('bedroom-slider', 'value'),
    Input('bathroom-slider', 'value'),
    Input('floor-slider', 'value'),
    Input('sqft-slider', 'value'),
    Input('price-slider', 'value'),
    Input('price-toggle', 'value')
)
def update_map(zipcode, min_beds, min_baths, min_floors, sqft_range, price_range, toggle_vals):
    filtered = df[df['zipcode'] == zipcode]
    if min_beds > 0:
        filtered = filtered[filtered['bedrooms'] >= min_beds]
    if min_baths > 0:
        filtered = filtered[filtered['bathrooms'] >= min_baths]
    if min_floors > 0:
        filtered = filtered[filtered['floors'] >= min_floors]
    filtered = filtered[
        (filtered['sqft_living'] >= sqft_range[0]) & (filtered['sqft_living'] <= sqft_range[1]) &
        (filtered['price'] >= price_range[0]) & (filtered['price'] <= price_range[1])
    ]

    filtered['predicted_score'] = model.predict(filtered[[
        'bedrooms', 'bathrooms', 'sqft_living', 'floors', 'grade',
        'condition', 'view', 'waterfront', 'lat', 'long', 'zipcode'
    ]])

    min_price = filtered["price"].min()
    max_price = filtered["price"].max()
    avg_price = filtered["price"].mean()

    color_by = 'price_per_sqft' if 'pps' in toggle_vals else (
        'predicted_score' if 'pred' in toggle_vals else 'price')

    fig = px.scatter_mapbox(
        filtered,
        lat="lat", lon="long", color=color_by,
        size="sqft_living", zoom=10,
        hover_name="address",
        hover_data={
            "sqft_living": True,
            "price": True,
            "price_per_sqft": True,
            "predicted_score": True,
            "lat": False,
            "long": False,
            "min_price": [min_price] * len(filtered),
            "max_price": [max_price] * len(filtered),
            "avg_price": [avg_price] * len(filtered),
        },
        mapbox_style="open-street-map",
        title=f"Properties in Zipcode {zipcode}"
    )
    return fig

@app.callback(
    Output('trend-line', 'figure'),
    Input('zipcode-dropdown', 'value')
)
def update_projection(zipcode):
    avg = df[df['zipcode'] == zipcode]['price'].mean()
    monthly_growth = 0.01  # 1% growth assumption
    projection = [avg * ((1 + monthly_growth) ** i) for i in range(1, 13)]
    months = [f"Month {i}" for i in range(1, 13)]

    fig = px.line(
        x=months,
        y=projection,
        labels={'x': 'Month', 'y': 'Projected Price'},
        title='Investment Projection (12 Months)'
    )
    return fig

def run_app(debug=False):
    app.run_server(debug=debug)

def run_app(debug=False):
    app.run(debug=debug)