# 📊 ESG vs Stock Returns — India Large-Cap Analysis (2020–2025)

![Power BI](https://img.shields.io/badge/PowerBI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)
![Research](https://img.shields.io/badge/Research-Paper-blue?style=for-the-badge)
![NIFTY](https://img.shields.io/badge/NIFTY-Large--Cap-green?style=for-the-badge)

> An end-to-end quantitative research project examining whether ESG scores predict stock returns for 100 NIFTY large-cap Indian companies over 2020–2025, using Python (regression + correlation), Excel financial modelling, and Power BI dashboards.

---

## 📌 Table of Contents

- • [Overview](#-overview)
- • [Research Questions](#-research-questions)
- • [Dataset](#-dataset)
- • [Tools & Technologies](#%EF%B8%8F-tools--technologies)
- • [Project Structure](#%EF%B8%8F-project-structure)
- • [Data Sources & Methodology](#-data-sources--methodology)
- • [Key Findings](#-key-findings)
- • [Sector-Level Analysis](#-sector-level-analysis)
- • [Regression Results](#-regression-results)
- • [Dashboard Preview](#-dashboard-preview)
- • [How to Run This Project](#-how-to-run-this-project)
- • [Research Paper](#-research-paper)
- • [Policy Implications](#-policy-implications)
- • [Author & Contact](#-author--contact)

---

## 📖 Overview

This project investigates the relationship between corporate ESG (Environmental, Social and Governance) performance and financial returns for **100 NIFTY large-cap Indian companies** over the period **2020–2025**. The study addresses a key question in emerging-market sustainable finance: does ESG outperformance translate into stock market returns in India, or is the ESG premium — well-documented in European markets — still nascent here?

The analysis uses four holding periods (1Y, 3Y, 5Y, 10Y), Pearson correlation, OLS regression with financial controls, and sector-level breakdown across 17 industries. Results are visualised through a fully interactive **Power BI dashboard** and documented in a peer-ready **research paper**.

---

## 🔬 Research Questions

1. **Do High-ESG companies deliver superior average stock returns** relative to Low-ESG peers across multiple holding periods?
2. **Is there a statistically significant linear correlation** between ESG scores and CAGR at the individual company level?
3. **Are sector effects large enough** to moderate or reverse the aggregate ESG–return relationship?

---

## 📁 Dataset

- **Source:** BRSR disclosures (SEBI), NSRAL ratings, CRISIL, SES, S&P Global, Screener.in
- **File:** `data/ESG_DATA.csv`
- **Companies:** 100 NIFTY large-cap companies across 17 sectors
- **ESG Score Range:** 42 to 81 (mean: 62.43, SD: 7.68)
- **Primary Return Metric:** 5-Year CAGR (%) — proxy for 2020–2025 holding period
- **High-ESG Group:** 51 companies (mean ESG score: 68.29)
- **Low-ESG Group:** 49 companies (mean ESG score: 56.33)

### Key Columns

| Column | Description |
|---|---|
| `Company` | Company name |
| `NSESymbol` | NSE ticker symbol |
| `Industry` | Sector classification (17 sectors) |
| `ESGGrade` | Letter grade: A+, A, B+, B, C+ |
| `ESGScoreNumeric` | ESG score on 0–100 scale |
| `MarketCapCr` | Market capitalisation (₹ crore) |
| `ROE3Y` | 3-year average Return on Equity (%) |
| `PERatio` | Price-to-Earnings ratio |
| `PromoterHolding` | Promoter holding (%) |
| `FIIHolding` | Foreign Institutional Investor holding (%) |
| `StockCAGR1Y` | 1-year CAGR (%) |
| `StockCAGR3Y` | 3-year CAGR (%) |
| `StockCAGR5Y` | 5-year CAGR (%) ⭐ Primary variable |
| `StockCAGR10Y` | 10-year CAGR (%) |

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|---|---|
| **Python 3.11** | Pearson correlation, OLS regression, EDA (pandas, scipy, statsmodels) |
| **Power BI Desktop** | Interactive multi-visual ESG dashboard |
| **Microsoft Excel** | Financial modelling, ESG scoring framework, pivot analysis |
| **GitHub** | Version control & research documentation |

---

## 🗂️ Project Structure

```
esg-stock-returns-india-excel-python-powerbi-research/
│
├── 📁 assets/                        ← Dashboard screenshots & visuals
├── 📁 data/
│   └── ESG_DATA.csv                  ← Full 100-company verified dataset
├── 📁 analysis/
│   └── esg_analysis.py               ← Python: correlation, regression, EDA
├── 📁 dashboard/
│   └── ESG_Dashboard.pbix            ← Power BI interactive dashboard
├── 📁 paper/
│   └── ESG_Research_Paper_Final.pdf  ← Full research paper (14 pages)
├── 📁 excel/
│   └── ESG_vs_Returns_Analysis.xlsx  ← Excel financial model & pivot tables
└── README.md
```

---

## 🔍 Data Sources & Methodology

### ESG Score Sources (cross-referenced)
- ✅ SEBI BRSR disclosures (SEBI Circular SEBI/LAP/GEN/2021/0000000009)
- ✅ NSRAL (NSE Sustainability Ratings and Analytics Ltd.) — FY 2024–25
- ✅ CRISIL ESG assessment summaries
- ✅ Stakeholders Empowerment Services (SES) ESG ratings
- ✅ S&P Global ESG data

### Return Data
- All CAGR figures sourced from **Screener.in** — price-adjusted returns from NSE/BSE exchange feeds, accounting for stock splits and bonus issues.

### Analytical Approach
- **Median split:** ESG score ≥ 63 = High-ESG (n=51); < 63 = Low-ESG (n=49)
- **Pearson correlation:** `scipy.stats.pearsonr` — two-tailed p-values
- **OLS regression:** Two models via `statsmodels` — ESG-only baseline vs. full controls (ln(Market Cap), ROE, P/E, FII Holding, Promoter Holding)
- **Sector analysis:** Mean 5Y CAGR compared across 11 sectors with both ESG groups represented

---

## 💡 Key Findings

### 📈 Group-Level Outperformance

High-ESG companies outperformed Low-ESG companies **across all four holding periods**:

| Holding Period | High-ESG CAGR (%) | Low-ESG CAGR (%) | Difference (pp) |
|---|---|---|---|
| 1-Year | 13.94 | 12.63 | +1.31 |
| **3-Year** | **12.63** | **9.39** | **+3.24 ↑ Widest gap** |
| 5-Year ⭐ | 13.80 | 10.94 | +2.87 |
| 10-Year | 13.69 | 13.37 | +0.32 |

### 📉 Pearson Correlation (ESG Score vs. 5Y CAGR)

| Metric | Value |
|---|---|
| Pearson r | 0.179 |
| p-value | 0.075† |
| R² | 0.032 |
| Interpretation | Weak positive — significant at 10% only |

> ⚠️ ESG scores explain only **3.2% of the variation** in 5-year individual company returns. The group-level premium does not reflect a strong linear ESG–return relationship.

### 🔑 KPI Summary

| KPI | Value |
|---|---|
| Companies Analysed | 100 |
| ESG Premium (5Y CAGR avg) | +2.90 pp |
| High ESG Sector Wins | 7/11 |
| Pearson r (ESG vs 5Y) | 0.18 |
| p-value | 0.075 (Weak) |
| Top High-ESG Performer | Adani Green Energy — 65% CAGR |
| Top Low-ESG Performer | Trent Ltd — 55% CAGR |

---

## 🏭 Sector-Level Analysis

The aggregate ESG advantage is **not uniform across sectors**. Low-ESG companies lead in 4 of 11 sectors:

| Sector | High-ESG 5Y CAGR (%) | n | Low-ESG 5Y CAGR (%) | n | Leader |
|---|---|---|---|---|---|
| Automobile | 16.4 | 5 | 8.8 | 4 | **High ESG** |
| Banks | 10.4 | 5 | −5.3 | 3 | **High ESG** |
| Cement | 15.5 | 2 | 10.7 | 3 | **High ESG** |
| Construction | 15.0 | 1 | 28.0 | 1 | **Low ESG** |
| Consumer Goods | 12.2 | 14 | 11.4 | 9 | **High ESG** |
| Finance: Non-Banking | 8.2 | 4 | 10.4 | 5 | **Low ESG** |
| IT | 10.1 | 7 | 19.0 | 1 | **Low ESG** |
| Metals & Mining | 15.2 | 4 | 11.5 | 2 | **High ESG** |
| Pharma | 6.8 | 4 | 11.0 | 11 | **Low ESG** |
| Power† | 65.0 | 1 | 35.0 | 1 | **High ESG** |
| Telecom | 25.0 | 1 | −2.0 | 1 | **High ESG** |

> † Power sector High-ESG figure driven by Adani Green Energy Ltd. (5Y CAGR 65%). Reflects idiosyncratic firm performance, not a sector-wide ESG premium.

---

## 📐 Regression Results

Two OLS models estimated with **5-Year CAGR** as the dependent variable:

| Variable | Model 1 (ESG Only) | Model 2 (Full Controls) |
|---|---|---|
| ESG Score | 0.267† (p=0.075) | 0.061 (p=0.664) — **insignificant** |
| ln(Market Cap) | — | **4.200*** (p<0.001) |
| P/E Ratio | — | **0.222*** (p<0.001) |
| ROE 3Y avg (%) | — | 0.006 (p=0.905) |
| FII Holding (%) | — | 0.032 (p=0.828) |
| Promoter Holding (%) | — | 0.067 (p=0.402) |
| **R²** | **0.032** | **0.372** |
| **Adj. R²** | **0.022** | **0.331** |
| **F-stat** | 3.19 (p=0.075) | **9.16 (p<0.001)** |

> **Critical finding:** Once market cap and P/E controls are added, the ESG coefficient becomes statistically zero (p=0.664). The group-level ESG premium is confounded by **firm size and valuation** — not independent ESG investor repricing.

---

## 📊 Dashboard Preview

**Power BI Dashboard — ESG vs Returns India Large-Cap**

![ESG Dashboard](assets/ESG_Dashboard_Screenshot.png)

The interactive dashboard covers:
- 📌 KPI cards: Companies analysed, ESG Premium (5Y CAGR), High ESG Sector Wins, Pearson r
- 📊 Average return by holding period — High vs Low ESG bar chart
- 🔵 ESG score vs 5-year return scatter plot (r = 0.18, p = 0.075)
- 🏭 Sector breakdown — 5Y CAGR High vs Low ESG
- 🏆 Top 10 performers per group (5Y CAGR %)

---

## 🚀 How to Run This Project

### Prerequisites

- [Power BI Desktop](https://powerbi.microsoft.com/desktop/) (free)
- Python 3.11+ with: `pandas`, `scipy`, `statsmodels`, `matplotlib`, `seaborn`
- Microsoft Excel or any CSV viewer
- Git (optional, for cloning)

### Steps

**1. Clone the repository:**
```bash
git clone https://github.com/AkarshKumarM05/esg-stock-returns-india-excel-python-powerbi-research.git
```

**2. Navigate to the project folder:**
```bash
cd esg-stock-returns-india-excel-python-powerbi-research
```

**3. Install Python dependencies:**
```bash
pip install pandas scipy statsmodels matplotlib seaborn openpyxl
```

**4. Run the Python analysis:**
```bash
cd analysis
python esg_analysis.py
```
This will output:
- Descriptive statistics for all 100 companies
- Pearson correlation table (all 4 holding periods)
- OLS regression results (Model 1 and Model 2)
- Sector-level CAGR comparison

**5. Open the Excel model:**
- Navigate to `excel/ESG_vs_Returns_Analysis.xlsx`
- Contains pivot tables, ESG scoring framework, and financial summary tabs

**6. Open the Power BI Dashboard:**
- Open `dashboard/ESG_Dashboard.pbix` in **Power BI Desktop**
- If prompted, update the data source path to point to `data/ESG_DATA.csv` on your local machine
- Go to **Home → Refresh** to load the latest data

**7. Read the full research paper:**
- Open `paper/ESG_Research_Paper_Final.pdf` for the complete 14-page academic write-up

---

## 📄 Research Paper

**Title:** *Do ESG Scores Predict Stock Returns? Evidence from Indian Large-Cap Companies (2020–2025)*

**Author:** Akarsh Kumar Pandey, B.Com (Hons), University of Lucknow

**Abstract Summary:** High-ESG companies outperformed Low-ESG peers across all four holding periods, with the widest gap at the 3-year horizon (+3.24 pp). However, the Pearson correlation between ESG score and 5-year CAGR is weak (r = 0.179, p = 0.075), and once size and valuation controls are added via OLS regression, the ESG coefficient becomes statistically insignificant. The ESG premium in India appears nascent and largely confounded by firm size — contrasting with European markets where SFDR-mandated capital flows create structural demand for high-ESG securities.

**Keywords:** ESG scores, stock returns, India, large-cap, Pearson correlation, NIFTY, sustainable finance, SEBI BRSR

**Related Work:** [Bridging the Impact Gap — Sustainable Finance for Indian SMEs (SSRN #6603859)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6603859)

---

## 🏛️ Policy Implications

**For SEBI & Indian Regulators:**
- Strengthen and expand the BRSR framework — align with ISSB (IFRS S1/S2) and GRI Standards
- Consider an Indian ESG fund classification framework analogous to EU SFDR to build the institutional demand channel

**For Institutional Investors:**
- Avoid sector-agnostic ESG screening — sector heterogeneity is substantial
- Governance quality (the "G" in ESG) may be the primary performance channel in India

**For Researchers:**
- Use multivariate panel regression with sector fixed effects to isolate marginal ESG effects
- Track ESG–return relationship longitudinally as BRSR matures and ESG fund products expand

---

## 👨‍💻 Author & Contact

**Akarsh Kumar Pandey**  
B.Com (Hons) | Data Analytics Enthusiast

[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:tulnama02@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/akarshkpandey)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/AkarshKumarM05)
---

> ⭐ If you found this project useful, please give it a star — it helps a lot!



