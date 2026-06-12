"""
Fund Recommendation System

Input:
    Investor risk level (Low / Moderate / High)

Output:
    Top 3 mutual funds based on Sharpe Ratio
"""

import pandas as pd


# Load datasets
performance = pd.read_csv(
    "data/processed/scheme_performance_clean.csv"
)

fund_master = pd.read_csv(
    "data/raw/01_fund_master.csv"
)


# Select required columns
fund_master = fund_master[
    [
        "amfi_code",
        "scheme_name",
        "risk_category"
    ]
]


# Merge fund performance with fund details
fund_data = performance.merge(
    fund_master,
    on="amfi_code",
    how="inner"
)


def recommend_funds(risk_level):
    """
    Returns top 3 funds matching risk level
    sorted by Sharpe Ratio
    """

    result = fund_data[
        fund_data["risk_category"]
        .str.lower()
        ==
        risk_level.lower()
    ]


    result = result.sort_values(
        by="sharpe_ratio",
        ascending=False
    )

    return result[
    [
        "scheme_name_x",
        "risk_category",
        "sharpe_ratio"
    ]
].head(3)


# User input
risk = input(
    "Enter risk level (Low / Moderate / High): "
)


recommendation = recommend_funds(risk)


print("\nTop 3 Recommended Funds:")
print(recommendation)