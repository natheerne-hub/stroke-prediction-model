# 🧠 Stroke Prediction Model — Artifact Audit

[![Validate Model Artifacts](https://github.com/natheerne-hub/stroke-prediction-model/actions/workflows/validate-model.yml/badge.svg)](https://github.com/natheerne-hub/stroke-prediction-model/actions/workflows/validate-model.yml)

### Healthcare ML Governance & Reproducibility | Dr. Natheer Soliman, MD

This repository is best understood as a **model-artifact audit**, not a fully reproducible stroke-prediction study.

It demonstrates how I handle an incomplete healthcare ML artifact responsibly: verify what is actually available, automate integrity checks, document the intended workflow, and avoid publishing performance claims that cannot be independently reproduced.

## Why this repository matters

In healthcare AI, recognizing what **cannot** be validated is as important as reporting what can. The original training dataset, train/test split and complete training notebook are not published here. For that reason, this repository intentionally does **not** present unsupported accuracy, ROC-AUC, sensitivity or other clinical-performance claims.

That limitation is treated as a governance finding rather than hidden as a portfolio weakness.

## Published artifacts

- `stroke_model.joblib` — serialized trained model artifact
- `medical_features.joblib` — stored feature information
- `validate_model.py` — automated artifact-integrity checks
- `MODEL_CARD.md` — intended use, limitations and responsible-use documentation
- `requirements.txt` — Python dependencies
- GitHub Actions workflow for repeatable artifact validation

## Documented historical workflow

The available project documentation describes a workflow involving:

1. patient-data preprocessing,
2. feature preparation,
3. class-imbalance handling with SMOTE,
4. `GradientBoostingClassifier`,
5. artifact persistence with `joblib`,
6. automated checks that the published artifacts remain loadable.

Because the original training materials are unavailable in this repository, these steps should not be interpreted as a fully reproducible training pipeline.

## Reproducible check available today

```bash
pip install -r requirements.txt
python validate_model.py
```

The validation checks that the published artifacts exist, load successfully, expose the expected model interface, and contain a feature collection.

## Reproducibility gap

A complete model-development release would need, at minimum:

- verified dataset source and data dictionary,
- reproducible preprocessing and training code,
- train/test methodology,
- confusion matrix and threshold definition,
- sensitivity, specificity, precision and recall,
- ROC-AUC and PR-AUC,
- calibration assessment,
- subgroup/fairness analysis,
- model interpretation,
- external validation before clinical use.

## Clinical governance perspective

Stroke prediction is a high-consequence use case. Class imbalance, false negatives, calibration, population shift and threshold selection can materially change clinical usefulness. A saved model file alone is therefore insufficient evidence of clinical performance.

This repository demonstrates a principle I apply across healthcare analytics: **trace the evidence, make limitations visible, and do not convert an unverifiable result into a portfolio claim.**

## Status

**Artifact integrity:** testable  
**Training reproducibility:** incomplete  
**Performance claims:** intentionally withheld  
**Clinical use:** not appropriate

## Author

**Dr. Natheer Soliman, MD**  
Healthcare Data Analytics · Clinical Analytics · Responsible Healthcare AI

[GitHub Profile](https://github.com/natheerne-hub)
