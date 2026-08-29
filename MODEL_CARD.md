# Model Card — Stroke Prediction Model

## Model Summary

This repository contains a serialized stroke-prediction model and a stored feature artifact. It is presented as a healthcare machine-learning portfolio artifact with automated integrity checks.

## Intended Use

- Educational demonstration
- Healthcare data-science portfolio review
- Technical inspection of model serialization and validation
- Future reproducibility work when the training data and notebook are available

## Out-of-Scope Use

The model must not be used for:

- clinical diagnosis
- patient triage
- treatment decisions
- population screening
- autonomous clinical decision-making
- deployment in a healthcare environment without full validation and governance

## Published Artifacts

| Artifact | Purpose |
|---|---|
| `stroke_model.joblib` | Serialized prediction model |
| `medical_features.joblib` | Stored feature information |
| `validate_model.py` | Basic artifact integrity validation |
| `validate-model.yml` | Automated GitHub Actions validation |

## Current Validation

The automated check confirms that the files exist, load successfully, and expose the minimum expected interfaces. This is an integrity check—not a clinical or performance validation.

## Performance Status

No accuracy, precision, recall, F1, ROC-AUC, PR-AUC, calibration, or subgroup-performance values are claimed because the original training dataset, split methodology, and complete training workflow are not currently published.

## Key Limitations

- Training data provenance is not documented in the current release.
- The complete preprocessing pipeline is not published.
- Model performance cannot be independently reproduced.
- External validation has not been demonstrated.
- Calibration and subgroup fairness have not been assessed.
- Clinical utility and workflow impact have not been evaluated.

## Requirements Before Clinical Consideration

A future clinical-grade evaluation would require documented data provenance, reproducible preprocessing, leakage controls, temporal and external validation, calibration analysis, subgroup evaluation, clinical-impact assessment, privacy review, governance, monitoring, and regulatory review where applicable.

## Responsible Interpretation

A machine-learning output is not a diagnosis. Stroke risk is clinically complex and requires qualified professional assessment using validated clinical information and appropriate care pathways.

## Author

**Dr. Natheer Soliman, MD**  
Healthcare Data Analyst | Clinical Data & AI
