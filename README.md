# Reform UK Vote Prediction - Machine Learning Project

## Overview

This project investigates the rise of Reform UK by using machine learning to predict Reform UK vote share across UK constituencies. The aim is to assess whether demographic, economic and political characteristics can explain differences in Reform UK support.

The project covers exploratory data analysis, predictive modelling and model interpretation.

## Research Question

Which demographic, economic and political factors best explain support for Reform UK across UK constituencies?

## Dataset

Each observation corresponds to a UK constituency. Constituencies where Reform did not have a candidate are dropped, as a zero vote share there reflects candidacy absence rather than voter choice.

**Target variable**
- `reform_vote_share` - Reform UK vote share (%)

**Explanatory variables**
- `leave_vote_share` - 2016 Brexit Leave vote share (%)
- `degree_pct` - share of residents with higher education qualifications (%)
- `median_age` - constituency median age
- `median_weekly_wage` - median gross weekly wage (£)
- `claimant_rate` - claimant count rate (%)
- `log_foreign_born_pct` - log-transformed foreign-born share
- `log_population_density` - log-transformed population density
- `ethnic_minority_pct` - ethnic minority share (%)
- `deprivation_score` - IMD-based deprivation score
- `is_scotland` - binary indicator for Scottish constituencies

**Final sample size:** 607 constituencies

## Methodology

### 1. Exploratory Data Analysis
- descriptive statistics and distribution analysis
- correlation matrix and bivariate scatterplots
- VIF check revealing severe multicollinearity 
- Brexit x education interaction analysis

### 2. Models

**Champion chosen: Lasso**
Chosen over OLS because VIF values reached 175, making standard regression coefficients unstable. Lasso addresses multicollinearity through L1 regularisation, achieving a cross-validated R² of 0.843 with an overfitting gap of -0.003. The small gains from Random Forest and Gradient Boosting (0.006-0.009 in cross-validated R²) did not justify the added complexity given the size of the dataset and the importance of interpretability.

**Challenger 1: Linear Regression (VIF-reduced)**
As a benchmark, variables were removed iteratively until all VIF values were below 10. This process led to leave_vote_share being excluded, leaving a four-variable demographic model with a cross-validated R² of 0.730. This model was included to compare manual variable selection with Lasso's automatic regularisation.

**Challenger 2: Random Forest**
Achieved highest test R² (0.881) but also showed an overfitting gap of 0.029, more than twice that of Gradient Boosting's. Shows the potential risk of complex ensemble methods on a relatively small dataset.

**Challenger 3: Gradient Boosting**
Best overall (CV R² = 0.849, gap = 0.012) and closest competitor to Lasso. However, the marginal CV gain (0.006) does not justify the added complexity or lower interpretability. XGBoost was also tested (CV R² = 0.845, overfitting gap = 0.018) but performed slightly worse than Gradient Boosting and was excluded from the final comparison.

### 3. Model Evaluation
All models evaluated using R², MAE, RMSE and 5-fold cross-validation. Champion selection based on CV R² and extend of overfitting, not test R².

### 4. Hyperparameter Tuning
GridSearchCV was used to tune the Random Forest and Gradient Boosting models.

## Main Findings

- The 2016 Brexit Leave vote is the strongest single predictor of Reform UK support (r = 0.88), suggesting substantial continuity between the Brexit electorate and Reform UK voters.
- Education is the second most important predictor (r = -0.69). Lower degree share consistently predicts higher support for Reform UK.
- The claimant rate shows little relationship with Reform support (r = -0.08, p = 0.060), indicating that unemployment alone does not explain variation in vote share.
- VIF analysis reveals that leave_vote_share is highly correlated with the demographic variables and is excluded when variables are removed iteratively to reduce multicollinearity.

## Repository Structure

```
.
├── data/
│   ├── raw/
│   └── processed/
├── outputs/
│   ├── figures/
│   └── model outputs/
├── src/
│   ├── clean_data.py
│   └── notebooks/
│       ├── reform_UK_analysis.ipynb  # EDA
│       ├── 02_models.ipynb
│       └── 03_results.ipynb
├── requirements.txt
└── README.md
```

## Installation

```bash
git clone https://github.com/Katpst/ml-reform-uk-votes-prediction.git
cd ml-reform-uk-votes-prediction
python -m venv venv
.\venv\Scripts\Activate.ps1   # Windows
pip install -r requirements.txt
```

## Running the project

```bash
jupyter notebook
```

Run notebooks in order: `reform_UK_analysis.ipynb` + `02_models.ipynb` + `03_results.ipynb`

## Limitations

- Constituencies where Reform UK did not field a candidate were excluded, which may introduce selection bias.
- Local candidate quality and campaign intensity are not captured in the dataset.
- Correlation does not imply causation; the project focuses on prediction rather than causal inference.
- Some relevant variables may have been omitted.

## Technologies

Python, pandas, NumPy, scikit-learn, matplotlib, seaborn, SHAP, Jupyter Notebook

## Authors

Katarzyna Pastuszka, Hanane Larbi
