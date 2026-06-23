# 📊 ESG Scores vs Stock Returns — India (NIFTY 100 Large-Cap)

![PYTHON](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![POWERBI](https://img.shields.io/badge/PowerBI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![EXCEL](https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white)
![RESEARCH](https://img.shields.io/badge/Research-Paper-red?style=for-the-badge)

An end-to-end empirical research project analyzing whether ESG (Environmental, Social, Governance) scores influence stock market returns among India's top 100 large-cap companies listed on NIFTY, covering the period 2020–2025.

---

## 📌 Overview

This research investigates one of the most debated questions in modern sustainable finance:

> **Do companies with higher ESG scores generate better stock returns in the Indian market?**

Using a dataset of **100 NIFTY large-cap companies**, this project applies Pearson correlation analysis, OLS regression, and multi-period CAGR comparisons to test whether ESG performance translates into superior financial performance.

---

## 🔍 Research Questions

1. Is there a statistically significant relationship between ESG scores and stock returns (1Y, 3Y, 5Y, 10Y CAGR)?
2. Do High-ESG companies consistently outperform Low-ESG companies across holding periods?
3. Does the ESG-return relationship remain significant after controlling for firm size, valuation (P/E), and market risk (Beta)?
4. Which ESG sub-score (Environmental, Social, or Governance) has the strongest correlation with returns?

---

## 📂 Dataset

| Attribute | Details |
|---|---|
| **Source** | NSE / BSE, Refinitiv Eikon, Sustainalytics, Bloomberg |
| **Universe** | 100 NIFTY Large-Cap Companies |
| **Period** | 2020 – 2025 |
| **Format** | CSV (`data/ESG_DATA.csv`) |

### Key Columns

| Column | Description |
|---|---|
| `Company` | Company name |
| `Ticker` | NSE/BSE ticker symbol |
| `Sector` | Industry sector (GICS classification) |
| `ESG_Score` | Overall ESG score (0–100) |
| `Environmental_Score` | Environmental sub-score |
| `Social_Score` | Social sub-score |
| `Governance_Score` | Governance sub-score |
| `CAGR_1Y` | 1-Year CAGR (%) |
| `CAGR_3Y` | 3-Year CAGR (%) |
| `CAGR_5Y` | 5-Year CAGR (%) |
| `CAGR_10Y` | 10-Year CAGR (%) |
| `Market_Cap_Cr` | Market capitalization (INR Crores) |
| `PE_Ratio` | Price-to-Earnings Ratio |
| `Beta` | Market risk (Beta) |

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|---|---|
| **Microsoft Excel** | Data collection, cleaning, pivot analysis, charts |
| **Python** | Correlation analysis, OLS regression, visualizations |
| **pandas, scipy, statsmodels** | Statistical analysis libraries |
| **matplotlib, seaborn** | Data visualization |
| **Power BI** | Interactive dashboard |
| **GitHub** | Version control & portfolio presentation |

---

## 📁 Project Structure

```
esg-stock-returns-india-excel-python-powerbi-research/
│
├── README.md                          ← Project documentation
├── data/
│   └── ESG_DATA.csv                   ← Master dataset (100 companies)
├── analysis/
│   └── esg_analysis.py                ← Python: correlation + OLS regression
├── dashboard/
│   └── ESG_Dashboard.pbix             ← Power BI interactive dashboard
├── paper/
│   └── ESG_Research_Paper_Final.pdf   ← Full research paper (PDF)
├── excel/
│   └── ESG_vs_Returns_Analysis.xlsx   ← Excel model & pivot analysis
└── assets/
    └── screenshots/                   ← Dashboard & chart screenshots
```

---

## 🔬 Methodology

### 1. Data Collection & Cleaning
- ESG scores sourced from Refinitiv / Sustainalytics for 100 NIFTY large-cap companies
- Stock return CAGRs calculated from adjusted closing prices (NSE/BSE)
- Removed companies with missing ESG data or <3 years of trading history
- Winsorized outliers at 1st and 99th percentile for CAGR columns

### 2. High-ESG vs Low-ESG Classification
- Companies split at **median ESG score (63)** into two equal groups
- High-ESG: Score ≥ 63 (50 companies)
- Low-ESG: Score < 63 (50 companies)

### 3. Statistical Analysis
- **Pearson Correlation**: ESG Score vs CAGR across all 4 time horizons
- **OLS Regression Model 1**: CAGR_5Y ~ ESG_Score (simple)
- **OLS Regression Model 2**: CAGR_5Y ~ ESG_Score + Market_Cap + PE_Ratio + Beta (controlled)

---

## 📊 Key Findings

| Holding Period | High-ESG CAGR | Low-ESG CAGR | Outperformance |
|---|---|---|---|
| 1-Year | Higher | Lower | +1.8 pp |
| 3-Year | Higher | Lower | **+3.24 pp** |
| 5-Year | Higher | Lower | +2.1 pp |
| 10-Year | Higher | Lower | +1.5 pp |

### Correlation Results

| Metric | Pearson r | p-value | Significant? |
|---|---|---|---|
| ESG vs CAGR_1Y | 0.12 | 0.231 | ❌ No |
| ESG vs CAGR_3Y | 0.21 | 0.036 | ✅ Yes (5%) |
| ESG vs CAGR_5Y | **0.179** | **0.074** | ⚠️ Marginal (10%) |
| ESG vs CAGR_10Y | 0.15 | 0.142 | ❌ No |

### Regression Conclusion

- **Simple OLS**: ESG Score is a weak but positive predictor of 5Y CAGR (R² = 0.032)
- **Controlled OLS**: Once Market Cap, P/E, and Beta are added, ESG significance drops — suggesting **firm size and valuation dominate** return explanation
- ESG investing in India shows **modest but directionally positive** return premium, strongest at the **3-year horizon**

---

## 📈 Dashboard (Power BI)

The interactive Power BI dashboard includes:

- **KPI Cards**: Average ESG Score, Median CAGR (5Y), High vs Low ESG count
- **Scatter Plot**: ESG Score vs 5-Year CAGR with regression trendline
- **Bar Chart**: Sector-wise average ESG scores
- **Line Chart**: CAGR comparison across 4 holding periods (High vs Low ESG)
- **Heatmap**: Correlation matrix of ESG sub-scores and returns
- **Slicer Filters**: Sector, ESG Group, Market Cap Range

> 📁 File: `dashboard/ESG_Dashboard.pbix`

---

## ▶️ How to Run the Python Analysis

```bash
# 1. Clone the repository
git clone https://github.com/AkarshKumarM05/esg-stock-returns-india-excel-python-powerbi-research.git
cd esg-stock-returns-india-excel-python-powerbi-research

# 2. Install dependencies
pip install pandas numpy scipy statsmodels matplotlib seaborn

# 3. Run the analysis script
python analysis/esg_analysis.py
```

**Output:**
- Descriptive statistics printed to console
- Pearson correlation results for all 4 CAGR horizons
- OLS regression summaries (simple + controlled)
- Scatter plot saved to `assets/esg_vs_returns_scatter.png`

---

## 📋 Excel Model

The Excel file (`excel/ESG_vs_Returns_Analysis.xlsx`) contains:

- **Sheet 1 — Raw Data**: Full 100-company dataset
- **Sheet 2 — Descriptive Stats**: Mean, median, SD by ESG group
- **Sheet 3 — Pivot Analysis**: Sector-wise ESG and CAGR breakdown
- **Sheet 4 — Correlation Matrix**: Pearson r table (all variables)
- **Sheet 5 — Charts**: Bar, scatter, and line charts for visual analysis

---

## 🏁 Final Conclusions

1. **High-ESG companies outperform Low-ESG peers** across all 4 holding periods, with the widest gap at the **3-year horizon (+3.24 pp)**
2. The ESG-return correlation is **weak (r = 0.179)** and only marginally significant — ESG alone does not predict returns
3. **Sector composition matters**: IT and Financial sectors dominate high-ESG rankings and also deliver stronger returns, creating a confounding effect
4. After controlling for Market Cap, P/E, and Beta, ESG's statistical significance weakens — suggesting **ESG is a secondary factor** in Indian large-cap returns
5. The findings are consistent with the **"ESG integration as risk management"** view — ESG reduces downside risk but does not guarantee alpha

---

## 📄 Research Paper

The full research paper is available in the `paper/` directory:

> `paper/ESG_Research_Paper_Final.pdf`

Covering: Literature Review, Data & Methodology, Results, Discussion, Limitations, and References.

---

## 👤 Author & Contact

**Akarsh Kumar Mishra**
Bachelor of Commerce (Honours) — University of Lucknow

- 🔗 [GitHub](https://github.com/AkarshKumarM05)
- 💼 [LinkedIn](https://www.linkedin.com/in/akarshkumarmishra)
- 📧 Open to research collaborations and feedback

---

*This project is part of a research portfolio in sustainable finance and data analytics.*
