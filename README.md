# 🧠 Stroke Prediction Model

### Healthcare Machine Learning | Dr. Natheer Soliman, MD

A machine-learning project exploring patient-level factors associated with stroke and building a classification model as a healthcare analytics exercise.

## 🎯 Objective

Develop a reproducible machine-learning pipeline that demonstrates how clinical data can be prepared and modeled while accounting for the **class imbalance** commonly found in healthcare datasets.

## ⚙️ Pipeline

1. Data preprocessing
2. Feature scaling with `StandardScaler`
3. Class-imbalance handling with `SMOTE`
4. Classification using `GradientBoostingClassifier`
5. Model evaluation using appropriate classification metrics

## 🧰 Tech Stack

- Python
- Pandas
- Scikit-learn
- Joblib
- SMOTE

## 📦 Model Files

- `stroke_model.joblib` — trained model
- `medical_features.joblib` — feature information used by the model

## ▶️ Loading the Model

```python
import joblib

model = joblib.load("stroke_model.joblib")
```

The model should receive data prepared with the same feature structure and preprocessing assumptions used during training.

## ⚠️ Important Note

This project is for **educational and portfolio purposes**. A machine-learning prediction is not a medical diagnosis and should not be used for clinical decision-making without appropriate validation and clinical oversight.

## 👨‍⚕️ Author

**Dr. Natheer Soliman, MD**  
Healthcare Data Analyst | Clinical Data & AI
