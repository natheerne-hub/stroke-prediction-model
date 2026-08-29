# 🧠 Stroke Prediction Model

[![Validate Model Artifacts](https://github.com/natheerne-hub/stroke-prediction-model/actions/workflows/validate-model.yml/badge.svg)](https://github.com/natheerne-hub/stroke-prediction-model/actions/workflows/validate-model.yml)

### Healthcare Machine Learning | Dr. Natheer Soliman, MD

A healthcare machine-learning portfolio project demonstrating publication, integrity validation, and responsible documentation of a trained stroke-prediction artifact.

## 🎯 Objective

Demonstrate a healthcare classification workflow involving preprocessing, feature management, class-imbalance handling, Gradient Boosting, model persistence, and clinically responsible interpretation.

## ✅ What Is Published

- A serialized trained model: `stroke_model.joblib`
- Stored feature information: `medical_features.joblib`
- Automated artifact-integrity validation
- Reproducible Python dependencies
- A transparent model card describing intended use and limitations

## ⚙️ Documented Workflow

1. Patient-data preprocessing
2. Feature preparation and scaling
3. Class-imbalance handling with SMOTE
4. Classification with `GradientBoostingClassifier`
5. Model and feature persistence with `joblib`
6. Automated verification that the published artifacts load correctly

> The original training notebook and dataset are not currently published. Therefore, this repository does not claim performance metrics that cannot be reproduced from the available files.

## 📦 Repository Contents

- [`stroke_model.joblib`](./stroke_model.joblib) — serialized trained model
- [`medical_features.joblib`](./medical_features.joblib) — stored feature information
- [`validate_model.py`](./validate_model.py) — model-artifact integrity checks
- [`MODEL_CARD.md`](./MODEL_CARD.md) — intended use, limitations, and responsible-use notes
- [`requirements.txt`](./requirements.txt) — Python dependencies
- [`.github/workflows/validate-model.yml`](./.github/workflows/validate-model.yml) — automated validation workflow

## ▶️ Validate the Published Artifacts

```bash
pip install -r requirements.txt
python validate_model.py
```

The validation confirms that:

- both published artifact files exist
- both artifacts can be loaded with `joblib`
- the model exposes a `predict()` method
- the stored feature artifact behaves as a feature collection

## 📊 Model Evaluation Status

A verified evaluation table cannot yet be reproduced from the published repository because the original dataset, train/test split, and full training notebook are not included.

A future complete release should add:

- dataset source and data dictionary
- full preprocessing and training pipeline
- train/test split methodology
- confusion matrix
- precision, recall, F1-score
- ROC-AUC and PR-AUC
- calibration assessment
- subgroup/fairness analysis
- feature importance or interpretable-model analysis

## 🩺 Clinical Perspective

In stroke screening, class imbalance and false-negative risk are clinically important. Accuracy alone is insufficient; sensitivity, precision, discrimination, calibration, subgroup performance, external validation, and clinical workflow impact must all be assessed.

## ⚠️ Important Note

This repository is for **educational and portfolio purposes**. The published model is not a medical device, does not provide a diagnosis, and must not be used for patient-care decisions without full technical validation, external clinical validation, governance, and professional oversight.

## 👨‍⚕️ Author

**Dr. Natheer Soliman, MD**  
Healthcare Data Analyst | Clinical Data & AI

🔗 [GitHub Profile](https://github.com/natheerne-hub)  
💼 [LinkedIn](https://www.linkedin.com/in/nather-suliaman-64866342a/)
