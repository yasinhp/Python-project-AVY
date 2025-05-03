# logistic_model_test.py

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import KBinsDiscretizer, StandardScaler
import joblib
import os
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay


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

# === Convert investment_score to categorical classes using quantile binning ===
binner = KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='quantile')
df['investment_class'] = binner.fit_transform(df[['investment_score']]).astype(int)

# === Feature selection ===
features = [
    'bedrooms', 'bathrooms', 'sqft_living', 'floors',
    'grade', 'condition', 'view', 'waterfront',
    'lat', 'long', 'zipcode'
]
target = 'investment_class'

X = df[features]
y = df[target]

# === Train/Test Split ===
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# === Scale Features ===
scaler = StandardScaler()
X_train_scaled = pd.DataFrame(scaler.fit_transform(X_train), columns=X_train.columns)
X_test_scaled = pd.DataFrame(scaler.transform(X_test), columns=X_test.columns)

# === Train Logistic Regression Model ===
model = LogisticRegression(max_iter=1000, solver='lbfgs')
model.fit(X_train_scaled, y_train)

# === Evaluate Model ===
y_pred = model.predict(X_test_scaled)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
# Save the trained model
joblib.dump(model, "model/logistic_investment_model.pkl")
print("Logistic model saved to model/logistic_investment_model.pkl")
os.makedirs("model", exist_ok=True)
# Plot confusion matrix
ConfusionMatrixDisplay.from_predictions(y_test, y_pred, cmap='Blues')
plt.title("Confusion Matrix - Logistic Regression")
plt.show()