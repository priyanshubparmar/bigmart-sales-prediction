# 📊 BigMart Sales Prediction – Case Study for Students

Welcome to the **BigMart Sales Prediction Case Study**!  
This project is designed for students to practice **forecasting / regression modeling** using a real retail dataset.

Original dataset: **Analytics Vidhya – Practice Problem: BigMart Sales III**  
**Link:** https://www.analyticsvidhya.com/datahack/contest/practice-problem-big-mart-sales-iii/

> **Classroom note:** If this repository contains the CSV files, they are provided solely for classroom use. All rights remain with the original owners (Analytics Vidhya / BigMart). Please check the competition terms before any public redistribution.

---

## 📌 Problem Statement
BigMart has collected **2013 sales data for 1559 products across 10 stores in different cities**.  
The goal is to **predict the sales of each product at a particular outlet**.

By analyzing this data, BigMart wants to understand which **product and outlet attributes** play important roles in driving sales.

---

## 📂 Repository Structure
```
.
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
├── data
│   ├── raw/                # place train.csv, test.csv, sample_submission.csv here
│   └── processed/          # any intermediate files you create
├── notebooks
│   └── 01_eda_baseline.ipynb
├── src
│   ├── data_prep.py
│   └── metrics.py
├── reports
│   └── figures/            # charts, plots
└── submissions/            # your model prediction files
```

### Expected Files in `data/raw/`
- `train.csv` → Training set (8523 rows) with features + target (`Item_Outlet_Sales`)  
- `test.csv` → Test set (5681 rows), **no** `Item_Outlet_Sales`  
- `sample_submission.csv` → Required submission format

### Data Dictionary
| Variable | Description |
|----------|-------------|
| Item_Identifier | Unique product ID |
| Item_Weight | Weight of product |
| Item_Fat_Content | Low Fat / Regular |
| Item_Visibility | Share of display area allocated to the product |
| Item_Type | Product category |
| Item_MRP | Maximum Retail Price |
| Outlet_Identifier | Unique store ID |
| Outlet_Establishment_Year | Year the store was established |
| Outlet_Size | Store size (e.g., Small/Medium/High) |
| Outlet_Location_Type | City tier (e.g., Tier 1/2/3) |
| Outlet_Type | Grocery store vs supermarket |
| Item_Outlet_Sales | **Target** (sales of the product in the outlet) |

---

## 🎯 Objective
> Build a predictive model to **forecast `Item_Outlet_Sales`** for the test dataset using the features provided.

---

## 🧮 Evaluation Metric
Use **Root Mean Squared Error (RMSE)** between predicted and actual sales.
- **Public score:** 25% of test data
- **Private score:** 75% of test data

---

## 🚀 Quickstart
1. Create a virtual env and install requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Place `train.csv`, `test.csv`, and `sample_submission.csv` in `data/raw/`.
3. Open `notebooks/01_eda_baseline.ipynb` to start exploring.
4. Produce predictions for `test.csv` and save to `submissions/your_submission.csv` in the format:
   ```
   Item_Identifier,Outlet_Identifier,Item_Outlet_Sales
   ```
5. (Optional) Submit on Analytics Vidhya to see your ranking.

---

## 🏆 Suggested Student Tasks
- Handle **missing values** in `Item_Weight` and `Outlet_Size`  
- Fix inconsistent categories in `Item_Fat_Content`  
- Engineer features: `item_age`, `outlet_age`, `visibility_ratio`, log-transform of `Item_MRP`, interactions  
- Try multiple models (Linear Regression → Ridge/Lasso → RandomForest → XGBoost/CatBoost/LightGBM)  
- Compare models using RMSE; keep a leaderboard in your class

---

## 🧰 Reproducibility
- Keep code in `notebooks/` or modularize into `src/`  
- Save artifacts (models/encoders) with versioned filenames if needed  
- Seed your splits for reproducibility

---

## 📖 References
- Analytics Vidhya – Practice Problem: BigMart Sales III  
  https://www.analyticsvidhya.com/datahack/contest/practice-problem-big-mart-sales-iii/

---

## 👤 Author
Maintained by **Vijay Barai**.  
If you find this useful, please ⭐ the repo and follow for more case studies!
