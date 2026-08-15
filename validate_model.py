"""Basic integrity checks for the published stroke model artifacts.

This script does not claim model performance because the original training dataset
and training notebook are not currently published in this repository.
"""
from pathlib import Path
import joblib

MODEL_PATH = Path("stroke_model.joblib")
FEATURES_PATH = Path("medical_features.joblib")

for path in (MODEL_PATH, FEATURES_PATH):
    if not path.exists():
        raise FileNotFoundError(f"Required artifact not found: {path}")

model = joblib.load(MODEL_PATH)
features = joblib.load(FEATURES_PATH)

if not hasattr(model, "predict"):
    raise TypeError("stroke_model.joblib does not expose a predict() method")

if not hasattr(features, "__len__"):
    raise TypeError("medical_features.joblib is not a feature collection")

print("Model class:", type(model).__name__)
print("Feature artifact class:", type(features).__name__)
print("Number of stored features:", len(features))
print("Published model artifacts loaded successfully.")
