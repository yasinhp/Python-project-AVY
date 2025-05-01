# xgboost_model_test.py

import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
import joblib
import matplotlib.pyplot as plt
from xgboost import plot_importance
# === Load data ===
df = pd.read_csv("filtered_real_estate_data.csv")

# === Feature Engineering ===
df['price_per_sqft'] = df['price'] / df['sqft_living']
df['affordability_score'] = 1 / df['price_per_sqft']
df['quality_score'] = df['condition'] + df['grade'] + df['view'] + df['waterfront']
df['investment_score'] = (
    df['affordability_score'].rank(pct=True) * 0.5 +
    df['quality_score'].rank(pct=True) * 0.5
) * 100

# === Feature selection ===
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

# === Train XGBoost Regressor ===
model = xgb.XGBRegressor(n_estimators=100, max_depth=6, learning_rate=0.1, random_state=42)
model.fit(X_train, y_train)

# === Evaluate ===
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"R^2 Score: {r2:.4f}")
print(f"RMSE: {rmse:.4f}")
joblib.dump(model, "xgboost_investment_model.pkl")
plt.figure(figsize=(8,5))
plt.scatter(y_test, y_pred, alpha=0.4, edgecolors='k')
plt.xlabel("Actual Investment Score")
plt.ylabel("Predicted Investment Score")
plt.title("XGBoost - Actual vs Predicted Investment Scores")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--r')  # ideal line
plt.grid(True)
plt.tight_layout()
plt.show()
plt.figure(figsize=(12, 6))
plot_importance(model, importance_type='gain', max_num_features=6, show_values=False)
plt.title("Top 6 Feature Importances (XGBoost)")
plt.tight_layout()
plt.show()