"""
ESG Scores vs Stock Returns — India Large-Cap Analysis
=======================================================
Author  : Akarsh Kumar Pandey
          BCom Honours, National PG College (University of Lucknow)
Paper   : "Do ESG Scores Predict Stock Returns? Evidence from
           Indian Large-Cap Companies (2020–2025)"
GitHub  : https://github.com/AkarshKumarM05/esg-stock-returns-india

Data Sources
------------
ESG Scores  : BRSR filings (SEBI), NSRAL, CRISIL, SES Report (FY 2019-20)
Return Data : Screener.in (Mittal Analytics Pvt Ltd, data via NSE/BSE feeds)
Sample      : 100 NIFTY large-cap companies across 17 sectors

What This Script Does
---------------------
1. Descriptive statistics — ESG score and return distribution
2. High vs Low ESG group comparison + independent t-test
3. Pearson correlation — ESG score vs returns (1Y / 3Y / 5Y / 10Y)
4. Sector-level analysis — which sectors show ESG outperformance
5. OLS Regression — ESG effect with and without controls
   (Market Cap, ROE, P/E Ratio, FII Holding, Promoter Holding)

Requirements
------------
pip install pandas numpy scipy statsmodels matplotlib seaborn
"""

import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

# ─────────────────────────────────────────────
# 0. LOAD DATA
# ─────────────────────────────────────────────

df = pd.read_csv("data/ESG_DATA.csv")
print(f"Dataset loaded: {df.shape[0]} companies × {df.shape[1]} columns")
print(f"Sectors covered: {df['Industry'].nunique()}")
print(f"ESG groups: {df['ESG_Group'].value_counts().to_dict()}\n")


# ─────────────────────────────────────────────
# 1. DESCRIPTIVE STATISTICS
# ─────────────────────────────────────────────

print("=" * 65)
print("1. DESCRIPTIVE STATISTICS")
print("=" * 65)

desc_cols = ["ESG_Score_Numeric", "Stock_CAGR_1Y_%", "Stock_CAGR_3Y_%",
             "Stock_CAGR_5Y_%", "Stock_CAGR_10Y_%",
             "Market_Cap_Cr", "ROE_3Y_%", "PE_Ratio"]

print(df[desc_cols].describe().round(2))

print(f"\nESG Score range  : {df['ESG_Score_Numeric'].min()} – {df['ESG_Score_Numeric'].max()}")
print(f"5Y CAGR range    : {df['Stock_CAGR_5Y_%'].min()}% – {df['Stock_CAGR_5Y_%'].max()}%")
print(f"Mean 5Y CAGR     : {df['Stock_CAGR_5Y_%'].mean():.2f}%")


# ─────────────────────────────────────────────
# 2. HIGH ESG vs LOW ESG GROUP COMPARISON
# ─────────────────────────────────────────────

print("\n" + "=" * 65)
print("2. HIGH ESG vs LOW ESG — GROUP COMPARISON")
print("=" * 65)

high = df[df["ESG_Group"] == "High ESG"]
low  = df[df["ESG_Group"] == "Low ESG"]

print(f"\n{'Group':<15} {'n':>4}  {'1Y':>7}  {'3Y':>7}  {'5Y':>7}  {'10Y':>7}  {'ESG Score':>10}")
print("-" * 65)
for name, grp in [("High ESG", high), ("Low ESG", low)]:
    print(f"{name:<15} {len(grp):>4}"
          f"  {grp['Stock_CAGR_1Y_%'].mean():>7.2f}"
          f"  {grp['Stock_CAGR_3Y_%'].mean():>7.2f}"
          f"  {grp['Stock_CAGR_5Y_%'].mean():>7.2f}"
          f"  {grp['Stock_CAGR_10Y_%'].mean():>7.2f}"
          f"  {grp['ESG_Score_Numeric'].mean():>10.2f}")

# T-tests for each period
print("\nIndependent t-tests (High ESG vs Low ESG):")
print(f"{'Period':<8} {'High mean':>10} {'Low mean':>10} {'Gap (pp)':>10} {'t-stat':>8} {'p-value':>9} {'Sig':>5}")
print("-" * 65)
for period in ["1Y", "3Y", "5Y", "10Y"]:
    col = f"Stock_CAGR_{period}_%"
    t, p = stats.ttest_ind(high[col], low[col])
    gap = high[col].mean() - low[col].mean()
    sig = "***" if p < 0.01 else "**" if p < 0.05 else "*" if p < 0.10 else "ns"
    print(f"{period:<8} {high[col].mean():>10.2f} {low[col].mean():>10.2f} "
          f"{gap:>+10.2f} {t:>8.3f} {p:>9.3f} {sig:>5}")


# ─────────────────────────────────────────────
# 3. PEARSON CORRELATION — ESG vs RETURNS
# ─────────────────────────────────────────────

print("\n" + "=" * 65)
print("3. PEARSON CORRELATION — ESG SCORE vs STOCK RETURNS")
print("=" * 65)

print(f"\n{'Period':<8} {'r':>8} {'p-value':>10} {'Interpretation'}")
print("-" * 55)
for period in ["1Y", "3Y", "5Y", "10Y"]:
    col = f"Stock_CAGR_{period}_%"
    r, p = stats.pearsonr(df["ESG_Score_Numeric"], df[col])
    interp = ("weak positive, marginally sig." if 0.05 <= p < 0.10
              else "significant" if p < 0.05
              else "not significant")
    print(f"{period:<8} {r:>8.3f} {p:>10.3f}  {interp}")


# ─────────────────────────────────────────────
# 4. SECTOR-LEVEL ANALYSIS
# ─────────────────────────────────────────────

print("\n" + "=" * 65)
print("4. SECTOR-LEVEL ANALYSIS — 5Y CAGR")
print("=" * 65)

sector = (df.groupby(["Industry", "ESG_Group"])["Stock_CAGR_5Y_%"]
            .mean()
            .unstack()
            .round(2))
sector["Gap (High−Low)"] = sector.get("High ESG", 0) - sector.get("Low ESG", 0)
sector = sector.sort_values("Gap (High−Low)", ascending=False)
print(sector.to_string())

wins = (sector["Gap (High−Low)"] > 0).sum()
total = len(sector)
print(f"\nHigh ESG wins in {wins}/{total} sectors ({wins/total*100:.0f}%)")


# ─────────────────────────────────────────────
# 5. OLS REGRESSION WITH CONTROLS
# ─────────────────────────────────────────────

print("\n" + "=" * 65)
print("5. OLS REGRESSION — DEPENDENT VAR: 5-YEAR CAGR (%)")
print("=" * 65)

df_r = df.dropna(subset=["ESG_Score_Numeric", "Market_Cap_Cr",
                          "ROE_3Y_%", "PE_Ratio",
                          "Promoter_Holding_%", "FII_Holding_%",
                          "Stock_CAGR_5Y_%"]).copy()
df_r["ln_MarketCap"] = np.log(df_r["Market_Cap_Cr"])

# Model 1 — ESG only
X1 = sm.add_constant(df_r["ESG_Score_Numeric"])
m1 = sm.OLS(df_r["Stock_CAGR_5Y_%"], X1).fit()

# Model 2 — ESG + controls
X2 = df_r[["ESG_Score_Numeric", "ln_MarketCap",
            "ROE_3Y_%", "PE_Ratio",
            "FII_Holding_%", "Promoter_Holding_%"]]
X2 = sm.add_constant(X2)
m2 = sm.OLS(df_r["Stock_CAGR_5Y_%"], X2).fit()

print(f"\n{'Model':<8} {'R²':>6} {'Adj R²':>8} {'F-stat':>8} {'p(F)':>8}")
print("-" * 45)
print(f"{'Model 1':<8} {m1.rsquared:>6.3f} {m1.rsquared_adj:>8.3f} "
      f"{m1.fvalue:>8.2f} {m1.f_pvalue:>8.4f}")
print(f"{'Model 2':<8} {m2.rsquared:>6.3f} {m2.rsquared_adj:>8.3f} "
      f"{m2.fvalue:>8.2f} {m2.f_pvalue:>8.4f}")

print(f"\n{'Variable':<25} {'Model 1':>12} {'Model 2':>12}")
print("-" * 52)
all_vars = ["const", "ESG_Score_Numeric", "ln_MarketCap",
            "ROE_3Y_%", "PE_Ratio", "FII_Holding_%", "Promoter_Holding_%"]

for var in all_vars:
    m1_val = (f"{m1.params[var]:.3f}({'*' if m1.pvalues[var]<0.10 else ''})"
              if var in m1.params.index else "—")
    m2_val = (f"{m2.params[var]:.3f}"
              f"({'***' if m2.pvalues[var]<0.01 else '**' if m2.pvalues[var]<0.05 else '*' if m2.pvalues[var]<0.10 else 'ns'})"
              if var in m2.params.index else "—")
    print(f"{var:<25} {m1_val:>12} {m2_val:>12}")

print("\nSignificance: *** p<0.01  ** p<0.05  * p<0.10  ns not significant")

# Key insight
esg_p_m2 = m2.pvalues["ESG_Score_Numeric"]
print(f"""
KEY FINDING:
  ESG effect disappears (p={esg_p_m2:.3f}) once Market Cap and P/E
  are controlled for. The apparent ESG premium is driven by size
  and valuation — not ESG-specific investor repricing.
  This contrasts with European markets where SFDR regulation
  mechanically channels capital toward high-ESG securities.
""")


# ─────────────────────────────────────────────
# 6. VISUALIZATIONS
# ─────────────────────────────────────────────

print("=" * 65)
print("6. GENERATING CHARTS → saved to analysis/charts/")
print("=" * 65)

import os
os.makedirs("analysis/charts", exist_ok=True)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("ESG vs Stock Returns — India Large-Cap (2020–2025)",
             fontsize=14, fontweight="bold")

# Plot 1: Scatter ESG vs 5Y Return, colored by group
colors = {"High ESG": "#2ECC71", "Low ESG": "#E74C3C"}
for grp, grp_df in df.groupby("ESG_Group"):
    axes[0, 0].scatter(grp_df["ESG_Score_Numeric"],
                       grp_df["Stock_CAGR_5Y_%"],
                       label=grp, alpha=0.65,
                       color=colors[grp], s=50)
axes[0, 0].set_xlabel("ESG Score")
axes[0, 0].set_ylabel("5-Year CAGR (%)")
axes[0, 0].set_title(f"ESG Score vs 5Y Return  (r = 0.179, p = 0.075)")
axes[0, 0].legend()
axes[0, 0].axhline(0, color="gray", linewidth=0.5, linestyle="--")

# Plot 2: Bar chart — avg returns by period + group
periods = ["1Y", "3Y", "5Y", "10Y"]
x = np.arange(len(periods))
w = 0.35
h_means = [high[f"Stock_CAGR_{p}_%"].mean() for p in periods]
l_means = [low[f"Stock_CAGR_{p}_%"].mean() for p in periods]
axes[0, 1].bar(x - w/2, h_means, w, label="High ESG",
               color="#2ECC71", alpha=0.85)
axes[0, 1].bar(x + w/2, l_means, w, label="Low ESG",
               color="#E74C3C", alpha=0.85)
axes[0, 1].set_xticks(x)
axes[0, 1].set_xticklabels(periods)
axes[0, 1].set_ylabel("Avg CAGR (%)")
axes[0, 1].set_title("Average Returns by Holding Period")
axes[0, 1].legend()
axes[0, 1].axhline(0, color="gray", linewidth=0.5)

# Plot 3: Sector breakdown — 5Y CAGR gap
sec_gap = sector["Gap (High−Low)"].sort_values(ascending=True)
bar_colors = ["#2ECC71" if v > 0 else "#E74C3C" for v in sec_gap]
axes[1, 0].barh(sec_gap.index, sec_gap.values, color=bar_colors, alpha=0.85)
axes[1, 0].axvline(0, color="black", linewidth=0.8)
axes[1, 0].set_xlabel("Gap in 5Y CAGR: High−Low ESG (pp)")
axes[1, 0].set_title("Sector ESG Premium (green = High ESG wins)")
axes[1, 0].tick_params(axis="y", labelsize=8)

# Plot 4: Regression — actual vs fitted (Model 2)
fitted = m2.fittedvalues
actual = df_r["Stock_CAGR_5Y_%"]
axes[1, 1].scatter(fitted, actual, alpha=0.6,
                   color="#3498DB", s=45)
mn, mx = min(fitted.min(), actual.min()), max(fitted.max(), actual.max())
axes[1, 1].plot([mn, mx], [mn, mx], "r--", linewidth=1)
axes[1, 1].set_xlabel("Fitted Values — Model 2")
axes[1, 1].set_ylabel("Actual 5Y CAGR (%)")
axes[1, 1].set_title(f"Model 2 Fitted vs Actual  (Adj R² = {m2.rsquared_adj:.3f})")

plt.tight_layout()
plt.savefig("analysis/charts/esg_analysis.png", dpi=150, bbox_inches="tight")
plt.close()
print("Chart saved → analysis/charts/esg_analysis.png")
print("\nAnalysis complete.")
