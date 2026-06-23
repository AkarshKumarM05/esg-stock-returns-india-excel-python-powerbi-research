# 📊 ESG Scores vs Stock Returns — India (NIFTY 100 Large-Cap)

![PYTHON](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![POWERBI](https://img.shields.io/badge/PowerBI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![EXCEL](https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)
![RESEARCH](https://img.shields.io/badge/Research-Paper-red?style=for-the-badge)

An end-to-end empirical research project analyzing whether ESG (Environmental, Social, Governance) scores influence stock market returns among India's top 100 large-cap companies listed on NIFTY, covering the period 2020–2025. [page:3][file:7]

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Exploratory Data Analysis (EDA)](#-exploratory-data-analysis-eda)
- [Research Questions & Key Insights](#-research-questions--key-insights)
- [Dataset](#-dataset)
- [Tools & Technologies](#%EF%B8%8F-tools--technologies)
- [Project Structure](#-project-structure)
- [Methodology](#-methodology)
- [Key Findings](#-key-findings)
- [Dashboard (Power BI)](#-dashboard-power-bi)
- [How to Run This Project](#-how-to-run-this-project)
- [Excel Model](#-excel-model)
- [Research Paper](#-research-paper)
- [Dashboard View](#-dashboard-view)
- [Author & Contact](#-author--contact)

---

## 📌 Overview

This research investigates one of the most debated questions in modern sustainable finance: **Do companies with higher ESG scores generate better stock returns in the Indian market?** [file:7]

Using a dataset of **100 NIFTY large-cap companies**, this project applies Pearson correlation analysis, OLS regression, sector-level comparison, and multi-period CAGR analysis to test whether ESG performance translates into superior financial performance in India. [file:4][file:7]

---

## 📈 Exploratory Data Analysis (EDA)

The exploratory analysis begins with company-level ESG scores, market-cap characteristics, and return metrics across **1-year, 3-year, 5-year, and 10-year CAGR windows**. [file:4][file:7] The sample covers **100 companies across 17 sectors**, with ESG scores ranging from **42 to 81** and a mean ESG score of **62.43**. [file:4][file:7]

Initial EDA highlights that 5-year CAGR ranges from **-18% to 65%**, indicating substantial dispersion in individual stock performance. [file:7] It also shows that High-ESG firms tend to be larger and more profitable on average, which is important because those variables can confound a simple ESG-versus-return interpretation. [file:7]

---

## 🔍 Research Questions & Key Insights

### Research Questions

1. Is there a statistically significant relationship between ESG scores and stock returns across 1Y, 3Y, 5Y, and 10Y CAGR periods? [page:3][file:7]
2. Do High-ESG companies outperform Low-ESG companies on average across holding periods? [file:7]
3. Does the ESG-return relationship remain significant after adding control variables such as market cap, P/E ratio, ROE, FII holding, and promoter holding? [file:7]
4. How much do sector effects influence the ESG-return relationship in Indian large-cap stocks? [file:7]

### Key Insights

- High-ESG companies outperform Low-ESG companies across all four holding periods on average, with the widest gap at the **3-year horizon (+3.24 pp)**. [file:7]
- The Pearson correlation between ESG score and 5-year CAGR is **0.179** with **p = 0.075**, which is weak and only marginally significant. [file:7]
- Once financial controls are added, the ESG coefficient becomes statistically insignificant, suggesting the apparent premium is largely explained by **size and valuation effects** rather than independent ESG repricing. [file:7]
- Sector heterogeneity matters a lot, because Low-ESG companies lead in sectors such as **IT, Pharma, Finance (Non-Banking), and Construction**. [file:7]

---

## 📂 Dataset

| Attribute | Details |
|---|---|
| Source | ESG disclosures, NSRAL, CRISIL, SES, Screener.in [file:4][file:7] |
| Universe | 100 NIFTY Large-Cap Companies [file:4][file:7] |
| Period | 2020–2025 [file:7] |
| Format | CSV (`data/ESG_DATA.csv`) [page:3][file:4] |

### Key Columns

| Column | Description |
|---|---|
| `Company` | Company name [file:4] |
| `NSESymbol` | NSE ticker symbol [file:4] |
| `Industry` | Industry/sector classification [file:4] |
| `ESGScoreNumeric` | Overall ESG score (0–100) [file:4] |
| `MarketCapCr` | Market capitalization in ₹ crore [file:4] |
| `PERatio` | Price-to-Earnings ratio [file:4] |
| `ROE3Y` | 3-year average Return on Equity [file:4] |
| `FIIHolding` | Foreign Institutional Investor holding (%) [file:4] |
| `PromoterHolding` | Promoter holding (%) [file:4] |
| `StockCAGR1Y` | 1-Year CAGR (%) [file:4] |
| `StockCAGR3Y` | 3-Year CAGR (%) [file:4] |
| `StockCAGR5Y` | 5-Year CAGR (%) [file:4] |
| `StockCAGR10Y` | 10-Year CAGR (%) [file:4] |

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|---|---|
| Microsoft Excel | Data cleaning, structuring, pivot analysis [page:3] |
| Python | Correlation analysis, regression, EDA [page:3] |
| pandas, scipy, statsmodels | Statistical analysis libraries [page:3] |
| matplotlib, seaborn | Visualization support [page:3] |
| Power BI | Interactive dashboard [page:3] |
| GitHub | Version control and portfolio presentation [page:3] |

---

## 📁 Project Structure

```text
esg-stock-returns-india-excel-python-powerbi-research/
│
├── README.md
├── data/
│   └── ESG_DATA.csv
├── analysis/
│   └── esg_analysis.py
├── dashboard/
│   └── ESG_Dashboard.pbix
├── paper/
│   └── ESG_Research_Paper_Final.pdf
├── excel/
│   └── ESG_vs_Returns_Analysis.xlsx
└── assets/
    └── screenshots/
```

This structure is already present in your live repository, with folders for `analysis`, `assets/screenshots`, `dashboard`, `data`, `excel`, and `paper`. [page:3]

---

## 🔬 Methodology

### 1. Data Collection & Cleaning
- ESG scores were compiled from public ESG disclosure channels and cross-referenced where needed. [file:7]
- Stock return CAGRs and financial controls were collected from Screener.in and related public company data. [file:4][file:7]

### 2. High-ESG vs Low-ESG Classification
- Companies were split at the **median ESG score of 63**. [file:7]
- This produced **51 High-ESG companies** and **49 Low-ESG companies**. [file:7]

### 3. Statistical Analysis
- Pearson correlation was used to test ESG score versus all CAGR windows. [file:7]
- OLS regression tested whether ESG score predicts 5-year CAGR before and after controls. [file:7]
- Sector-wise comparison measured whether the ESG premium is uniform across industries. [file:7]

---

## 📊 Key Findings

| Holding Period | High-ESG CAGR | Low-ESG CAGR | Outperformance |
|---|---|---|---|
| 1-Year | 13.94% [file:7] | 12.63% [file:7] | +1.31 pp [file:7] |
| 3-Year | 12.63% [file:7] | 9.39% [file:7] | **+3.24 pp** [file:7] |
| 5-Year | 13.80% [file:7] | 10.94% [file:7] | +2.87 pp [file:7] |
| 10-Year | 13.69% [file:7] | 13.37% [file:7] | +0.32 pp [file:7] |

### Correlation Results

| Metric | Pearson r | p-value | Interpretation |
|---|---|---|---|
| ESG vs 1Y CAGR | 0.006 [file:7] | 0.954 [file:7] | Negligible [file:7] |
| ESG vs 3Y CAGR | 0.154 [file:7] | 0.127 [file:7] | Weak positive [file:7] |
| ESG vs 5Y CAGR | **0.179** [file:7] | **0.075** [file:7] | Weak positive, 10% only [file:7] |
| ESG vs 10Y CAGR | 0.132 [file:7] | 0.191 [file:7] | Weak positive [file:7] |

---

## 📈 Dashboard (Power BI)

The Power BI dashboard section should present the main project visuals, including KPI cards, a holding-period comparison, ESG-vs-return scatter, sector breakdown, and top performers by ESG group. [file:6][file:7] Your current screenshot already shows KPI cards such as **Companies Analysed = 100**, **ESG Premium (5Y CAGR) = 2.90**, **High ESG Sector Wins = 7/11**, and **Pearson r = 0.18**. [file:6]

You can keep this section near the middle for feature explanation, and then add a dedicated demo-style visual section at the end for display. [page:3][file:6]

---

## ▶️ How to Run This Project

```bash
git clone https://github.com/AkarshKumarM05/esg-stock-returns-india-excel-python-powerbi-research.git
cd esg-stock-returns-india-excel-python-powerbi-research
pip install pandas numpy scipy statsmodels matplotlib seaborn openpyxl
python analysis/esg_analysis.py
```

This project already contains an `analysis/esg_analysis.py` script in the repository, and the repository page shows the analysis folder live on `main`. [page:3] The script is intended to read `data/ESG_DATA.csv`, compute descriptive statistics, run correlations and OLS regressions, and generate visuals for the project. [page:3][file:4][file:7]

---

## 📋 Excel Model

The Excel workbook belongs in `excel/ESG_vs_Returns_Analysis.xlsx`, which matches the project structure you wanted for this repo. [page:3] Your attached workbook can later support raw data checks, pivot tables, sector summaries, and presentation tables for the GitHub project. [file:5]

---

## 📄 Research Paper

The full paper is intended for `paper/ESG_Research_Paper_Final.pdf`, and your attached PDF contains the 14-page write-up titled *Do ESG Scores Predict Stock Returns? Evidence from Indian Large-Cap Companies (2020–2025)*. [page:3][file:7] It includes the abstract, literature review, methodology, findings, regression analysis, policy implications, limitations, and references. [file:7]

---

## 🖼️ Dashboard View

Add this section at the **end of the README** so it works like a demo showcase area, similar to how portfolio repos often present visuals after the technical explanation. [page:3] For now, you can use a placeholder like this and replace it later when you add the final image file: [file:6]

```md
## 🖼️ Dashboard View

![ESG Dashboard Preview](assets/screenshots/esg-dashboard-preview.png)

> Interactive Power BI dashboard showing ESG premium, holding-period returns, sector comparison, correlation, and top performers.
```

Since your repo already has an `assets/screenshots` folder, this is the best place to store the future dashboard image you want to demonstrate at the end. [page:3]

---

## 👤 Author & Contact

**Akarsh Kumar Pandey**  
Bachelor of Commerce (Honours) — University of Lucknow [page:3]

- GitHub: [AkarshKumarM05](https://github.com/AkarshKumarM05) [page:3]
- LinkedIn: Add your current profile link here.
- Email: Add your preferred contact email here.


