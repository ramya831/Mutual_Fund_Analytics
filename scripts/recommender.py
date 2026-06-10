import pandas as pd


# Load files
performance = pd.read_csv(
    "data/processed/scheme_performance_clean.csv"
)

fund = pd.read_csv(
    "data/raw/01_fund_master.csv"
)


# Merge performance + fund details
df = performance.merge(
    fund[
        [
            "amfi_code",
            "scheme_name",
            "risk_category"
        ]
    ],
    on="amfi_code",
    how="inner"
)


def recommend(risk):

    result = df[
        df["risk_category"]
        .str.lower()
        ==
        risk.lower()
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


recommendation = recommend(risk)


print("\nTop 3 Recommended Funds:")
print(recommendation)