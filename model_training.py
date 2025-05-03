# model_training.py

import os  # NEW: for creating model folder
import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error

# === Load cleaned dataset ===
df = pd.read_csv("filtered_real_estate_data.csv")  # Adjust path as needed

# === Feature Engineering ===
df['price_per_sqft'] = df['price'] / df['sqft_living']
df['affordability_score'] = 1 / df['price_per_sqft']
df['quality_score'] = df['condition'] + df['grade'] + df['view'] + df['waterfront']
df['investment_score'] = (
    df['affordability_score'].rank(pct=True) * 0.5 +
    df['quality_score'].rank(pct=True) * 0.5
) * 100

# === Select Features & Target ===
features = [
    'bedrooms', 'bathrooms', 'sqft_living', 'floors',
    'grade', 'condition', 'view', 'waterfront',
    'lat', 'long', 'zipcode'
]
target = 'investment_score'

X = df[features]
y = df[target]

# === Train/Test Split ===
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# === Train Model ===
model = RandomForestRegressor(
    n_estimators=200,  # CHANGED: increased from 100 to 200 for potentially better accuracy
    max_depth=15,      # NEW: added depth limit for regularization
    random_state=42,
    n_jobs=-1          # NEW: use all CPU cores for faster training
)
model.fit(X_train, y_train)

# === Evaluate ===
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"R^2 Score: {r2:.4f}")  # CHANGED: formatted output
print(f"RMSE: {rmse:.4f}")     # CHANGED: formatted output

# === Save model ===
os.makedirs("model", exist_ok=True)  # NEW: Ensure model folder exists
joblib.dump(model, "model/investment_score_model.pkl")
print("Model saved to model/investment_score_model.pkl")
# Previous Accuracy with n_estimators=100 and no depth filter
#R^2 Score: 0.8675600003844721
#RMSE: 6.5716870381362105