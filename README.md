# 🧠 Stroke Prediction Model

### Healthcare Machine Learning | Dr. Natheer Soliman, MD

A healthcare machine-learning project exploring patient-level factors associated with stroke and demonstrating a classification workflow for imbalanced clinical data.

## 🎯 Objective

Build a reproducible machine-learning workflow that demonstrates preprocessing, feature scaling, class-imbalance handling, model persistence, and clinically responsible interpretation.

## ⚙️ Pipeline

1. Data preprocessing
2. Feature scaling with `StandardScaler`
3. Class-imbalance handling with `SMOTE`
4. Classification using `GradientBoostingClassifier`
5. Model persistence with `joblib`
6. Evaluation with clinically relevant classification metrics when the full training workflow is available

## 📦 Repository Contents

- `stroke_model.joblib` — trained model artifact
- `medical_features.joblib` — stored feature information
- `requirements.txt` — Python dependencies

## ▶️ Loading the Model

```python
import joblib

model = joblib.load("stroke_model.joblib")
```

The model must receive data prepared with the **same feature structure and preprocessing assumptions** used during training.

## 📊 Model Evaluation

The repository currently contains the trained model artifacts but does not yet expose the full training notebook or a verified evaluation table. For that reason, this README intentionally does **not** claim accuracy, recall, F1, or ROC-AUC values that cannot be reproduced from the files currently published.

A future revision should add:

- train/test split methodology
- confusion matrix
- precision, recall, F1-score
- ROC-AUC and/or PR-AUC
- calibration assessment
- feature importance or interpretable model analysis

## 🩺 Clinical Perspective

In stroke screening, class imbalance and false-negative risk matter. Model performance should therefore be judged with more than accuracy alone, particularly recall/sensitivity, precision, discrimination, calibration, and external validation.

## ⚠️ Important Note

This project is for **educational and portfolio purposes**. A machine-learning prediction is not a medical diagnosis and should not be used for clinical decision-making without appropriate validation and clinical oversight.

## 👨‍⚕️ Author

**Dr. Natheer Soliman, MD**  
Healthcare Data Analyst | Clinical Data & AI
