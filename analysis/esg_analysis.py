# ============================================================
# ESG vs Stock Returns — India (NIFTY 100 Large-Cap)
# Author  : Akarsh Kumar Mishra
# Dataset : 100 companies | 2020-2025 | NIFTY Large-Cap
# Tools   : Python, pandas, scipy, statsmodels, matplotlib
# ============================================================

import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# -----------------------------------------------------------
# 1. LOAD DATA
# -----------------------------------------------------------
df = pd.read_csv('../data/ESG_DATA.csv')
print(f"Dataset shape: {df.shape}")
print(df.head())

# -----------------------------------------------------------
# 2. DESCRIPTIVE STATISTICS
# -----------------------------------------------------------
print("\n=== Descriptive Statistics ===")
print(df[['ESG_Score','CAGR_1Y','CAGR_3Y','CAGR_5Y','CAGR_10Y']].describe().round(2))

# -----------------------------------------------------------
# 3. HIGH vs LOW ESG SPLIT (Median = 63)
# -----------------------------------------------------------
median_esg = df['ESG_Score'].median()
df['ESG_Group'] = np.where(df['ESG_Score'] >= median_esg, 'High-ESG', 'Low-ESG')
print(f"\nMedian ESG Score: {median_esg}")
print(df.groupby('ESG_Group')[['CAGR_1Y','CAGR_3Y','CAGR_5Y','CAGR_10Y']].mean().round(2))

# -----------------------------------------------------------
# 4. PEARSON CORRELATION
# -----------------------------------------------------------
print("\n=== Pearson Correlation (ESG Score vs CAGR) ===")
for col in ['CAGR_1Y','CAGR_3Y','CAGR_5Y','CAGR_10Y']:
    r, p = stats.pearsonr(df['ESG_Score'].dropna(), df[col].dropna())
    print(f"  {col}: r = {r:.3f}, p-value = {p:.4f}")

# -----------------------------------------------------------
# 5. OLS REGRESSION
# -----------------------------------------------------------
print("\n=== OLS Regression: CAGR_5Y ~ ESG_Score ===")
model1 = smf.ols('CAGR_5Y ~ ESG_Score', data=df).fit()
print(model1.summary())

print("\n=== OLS Regression: CAGR_5Y ~ ESG_Score + Market_Cap_Cr + PE_Ratio + Beta ===")
model2 = smf.ols('CAGR_5Y ~ ESG_Score + Market_Cap_Cr + PE_Ratio + Beta', data=df).fit()
print(model2.summary())

# -----------------------------------------------------------
# 6. VISUALISATION
# -----------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Scatter: ESG Score vs 5Y CAGR
axes[0].scatter(df['ESG_Score'], df['CAGR_5Y'], alpha=0.6, color='steelblue', edgecolors='white')
m, b = np.polyfit(df['ESG_Score'], df['CAGR_5Y'], 1)
axes[0].plot(df['ESG_Score'], m*df['ESG_Score']+b, color='red', linewidth=2)
axes[0].set_xlabel('ESG Score')
axes[0].set_ylabel('5-Year CAGR (%)')
axes[0].set_title('ESG Score vs 5-Year CAGR (NIFTY 100)')
axes[0].grid(True, alpha=0.3)

# Boxplot: High vs Low ESG
df.boxplot(column='CAGR_5Y', by='ESG_Group', ax=axes[1], grid=False)
axes[1].set_title('5Y CAGR: High-ESG vs Low-ESG')
axes[1].set_xlabel('ESG Group')
axes[1].set_ylabel('5-Year CAGR (%)')

plt.tight_layout()
plt.savefig('../assets/esg_vs_returns_scatter.png', dpi=150, bbox_inches='tight')
plt.show()
print("\nChart saved to assets/esg_vs_returns_scatter.png")
