# Reform UK Vote Prediction — Machine Learning Project

## Project Overview

This project investigates the rise of Reform UK by using machine learning models to predict Reform UK vote share across UK constituencies.

The objective is not to take a political position, but to analyze whether demographic, economic and political characteristics can help explain variations in Reform UK support.

The project combines:
- exploratory data analysis,
- predictive modelling,
- model interpretation,
- and political/economic analysis.

---

# Research Question

> Which demographic, economic and political factors best explain support for Reform UK across UK constituencies?

---

# Dataset

Each observation corresponds to a UK constituency.

## Target Variable
- `reform_vote_share` → Reform UK vote share (%)

## Explanatory Variables
- `leave_vote_share`
- `degree_pct`
- `median_age`
- `median_weekly_wage`
- `claimant_rate`
- `foreign_born_pct`
- `population_density`
- `ethnic_minority_pct`
- `deprivation_score`

The dataset contains:
- 630 constituencies
- no missing values

---

# Methodology

The project follows a standard machine learning workflow:

## 1. Exploratory Data Analysis (EDA)
- descriptive statistics
- histograms
- correlation analysis
- scatterplots
- residual analysis

## 2. Machine Learning Models
The following models are estimated:
- Linear Regression
- Random Forest
- Gradient Boosting
- XGBoost

## 3. Model Evaluation
Models are evaluated using:
- R²
- MAE
- RMSE
- 5-fold cross-validation

## 4. Hyperparameter Tuning
GridSearchCV is used to optimize:
- Random Forest
- Gradient Boosting
- XGBoost

## 5. Model Interpretation
Interpretability techniques include:
- standardized coefficients
- feature importance
- SHAP values
- residual analysis

---

# Main Findings

The results suggest that:
- Brexit Leave vote share is one of the strongest predictors of Reform UK support;
- educational attainment is negatively associated with Reform UK vote share;
- ensemble methods outperform the linear regression baseline;
- non-linear relationships contribute to explaining Reform UK support.

The project also highlights that:
- some constituencies remain difficult to predict,
- indicating that local political dynamics and omitted variables may still play an important role.

---

# Repository Structure

```text
.
├── data/
│   ├── raw/
│   └── processed/
│
├── outputs/
│   ├── figures
│   └── model outputs
│
├── src/
│   ├── clean_data.py
│   └── notebooks/
│       ├── 02_models.ipynb
│       ├── 03_results.ipynb
│       └── reform_UK_analysis.ipynb
│
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/USERNAME/REPOSITORY.git
cd REPOSITORY
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

### Windows
```bash
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the Project

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Main notebooks:
- `reform_UK_analysis.ipynb`
- `02_models.ipynb`
- `03_results.ipynb`

---

# Limitations

This project has several limitations:
- constituency-level data does not reflect individual-level behaviour;
- correlation does not imply causation;
- local political dynamics may not be fully captured;
- some relevant variables may be omitted;
- the project focuses on prediction rather than causal inference.

---

# Technologies Used

- Python
- pandas
- NumPy
- scikit-learn
- XGBoost
- matplotlib
- SHAP
- Jupyter Notebook

---

# Authors
- Katarzyna Pastuszka
- Hanane Larbi


---

# Academic Context

This project was developed as part of a Machine Learning course focusing on applied predictive modelling and model interpretation using real-world data.