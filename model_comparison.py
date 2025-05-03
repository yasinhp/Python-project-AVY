import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("filtered_real_estate_data.csv")

# Recreate investment_score
df['price_per_sqft'] = df['price'] / df['sqft_living']
df['affordability_score'] = 1 / df['price_per_sqft']
df['quality_score'] = df['condition'] + df['grade'] + df['view'] + df['waterfront']
df['investment_score'] = (
    df['affordability_score'].rank(pct=True) * 0.5 +
    df['quality_score'].rank(pct=True) * 0.5
) * 100

# Features & Target
features = [
    'bedrooms', 'bathrooms', 'sqft_living', 'floors',
    'grade', 'condition', 'view', 'waterfront',
    'lat', 'long', 'zipcode'
]
X = df[features]
y = df['investment_score']

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Load Models
rf_model = joblib.load("model/investment_score_model.pkl")
xgb_model = joblib.load("model/xgboost_investment_model.pkl")
log_model = joblib.load("model/logistic_investment_model.pkl")

# Predict
y_pred_rf = rf_model.predict(X_test)
y_pred_xgb = xgb_model.predict(X_test)
y_pred_log = log_model.predict(X_test)

# Create comparison DataFrame
comparison_df = pd.DataFrame({
    'Actual': y_test,
    'Random Forest': y_pred_rf,
    'XGBoost': y_pred_xgb,
    'Logistic Regression': y_pred_log
})

# Plot
fig, axs = plt.subplots(1, 3, figsize=(20, 6))

for idx, model in enumerate(['Random Forest', 'XGBoost', 'Logistic Regression']):
    sns.scatterplot(ax=axs[idx], x='Actual', y=model, data=comparison_df, alpha=0.5, edgecolor='k')
    axs[idx].plot([y.min(), y.max()], [y.min(), y.max()], '--r', linewidth=1.5)
    axs[idx].set_title(f"{model}\nR²: {r2_score(y_test, comparison_df[model]):.2f}, RMSE: {np.sqrt(mean_squared_error(y_test, comparison_df[model])):.2f}")
    axs[idx].set_xlabel("Actual Investment Score")
    axs[idx].set_ylabel("Predicted Score")

plt.suptitle("Model Performance: Actual vs Predicted Investment Score", fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()