# Bitcoin Price Forecasting Platform

**AI-Powered Cryptocurrency Risk Intelligence & Next-Day Price Prediction**

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CRISP-DM](https://img.shields.io/badge/Methodology-CRISP--DM-green.svg)]()

> A practical machine learning system that predicts Bitcoin’s next-day closing price to support risk management and data-driven investment decisions.

---

## Project Overview

Cryptocurrency markets, especially Bitcoin, are highly volatile and influenced by market sentiment, global events, and regulatory changes. Traditional forecasting methods often fail in this environment.

This project applies the **CRISP-DM** methodology to build a reliable, interpretable forecasting model using historical Bitcoin data. The goal is to help traders, investors, and analysts make better risk-aware decisions.

**Key Result**:  
After comparing four models (Linear Regression, Random Forest, XGBoost, and RNN), **Linear Regression** delivered the best performance on unseen data.

---

## Key Results

| Model               | MSE          | RMSE     | MAE      | R² Score |
|---------------------|--------------|----------|----------|----------|
| **Linear Regression** | **4,388,892** | **2,094.96** | **1,511.21** | **0.98** |
| RNN (Rescaled)      | 20,977,670   | 4,580.13 | 3,552.79 | -25.28   |
| Random Forest       | 346,923,519  | 18,625.88| 12,817.99| -0.52    |
| XGBoost             | 362,583,954  | 19,041.63| 13,328.94| -0.59    |

**Winner**: Linear Regression — highest accuracy, best trend tracking, and strongest generalization.

---

## Dataset

- **Source**: Kaggle – BTC-Price-1M (minute-level Bitcoin data)
- **Size**: ~4 million records
- **Time Range**: 2017 – early 2025
- **Final Frequency**: Daily (resampled from minute-level data)

**Features used**:
- Open, High, Low, Close, Volume
- Engineered features: `close_lag1`, `close_ma7` (7-day moving average), `daily_return`

**Target**: Next day’s closing price

---

## Methodology (CRISP-DM)

1. **Business Understanding** – Defined forecasting goal and success criteria focused on risk management
2. **Data Understanding** – Explored 4M+ minute-level records
3. **Data Preparation** – Cleaning, resampling to daily, feature engineering
4. **Modeling** – Trained and compared Linear Regression, Random Forest, XGBoost, and RNN
5. **Evaluation** – Used MSE, RMSE, MAE, and R² with time-ordered splits
6. **Deployment** – Designed as a practical decision-support tool

---

## Project Structure

```bash
bitcoin-price-forecasting/
├── data/
│   ├── raw/                  # Original minute-level data
│   └── processed/            # Daily resampled data
├── notebooks/                # Exploratory analysis & experiments
├── src/
│   ├── data/                 # Data loading & preprocessing
│   ├── models/               # Model training scripts
│   └── evaluation/           # Metrics and visualization
├── assets/                   # Charts and screenshots
├── requirements.txt
└── README.md
