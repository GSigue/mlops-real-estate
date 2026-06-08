from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib
import os

print("Loading California housing dataset...")
data = fetch_california_housing(as_frame=True)
X = data.data
y = data.target

print(f"Data shape: {X.shape}")
print(f"Features: {list(X.columns)}")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Training samples: {len(X_train)}")
print(f"Test samples: {len(X_test)}")

print("Training Random Forest model...")
model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

score = model.score(X_test, y_test)
print(f"R² score: {score:.4f}")

os.makedirs("outputs", exist_ok=True)
joblib.dump(model, "outputs/model.pkl")
print("Model saved to outputs/model.pkl")
