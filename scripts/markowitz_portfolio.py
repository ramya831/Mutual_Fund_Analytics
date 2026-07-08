import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Load cleaned NAV data
df = pd.read_csv("data/processed/nav_history_clean.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Pivot table
price_data = df.pivot(
    index="date",
    columns="amfi_code",
    values="nav"
)

# Remove missing values
price_data = price_data.dropna(axis=1)

# Daily returns
returns = price_data.pct_change().dropna()
# Calculate annual return and covariance
mean_returns = returns.mean() * 252
cov_matrix = returns.cov() * 252

# Number of funds
num_assets = len(mean_returns)

print("Number of Funds:", num_assets)
# Portfolio simulation settings
num_portfolios = 5000

results = np.zeros((3, num_portfolios))

weights_record = []
for i in range(num_portfolios):

    weights = np.random.random(num_assets)
    weights /= np.sum(weights)

    weights_record.append(weights)

    portfolio_return = np.sum(weights * mean_returns)

    portfolio_risk = np.sqrt(
        np.dot(
            weights.T,
            np.dot(cov_matrix, weights)
        )
    )

    sharpe_ratio = portfolio_return / portfolio_risk

    results[0, i] = portfolio_return
    results[1, i] = portfolio_risk
    results[2, i] = sharpe_ratio
# Find portfolio with highest Sharpe Ratio
max_sharpe_index = np.argmax(results[2])

best_return = results[0, max_sharpe_index]
best_risk = results[1, max_sharpe_index]
best_sharpe = results[2, max_sharpe_index]

best_weights = weights_record[max_sharpe_index]

print("\nBest Portfolio")
print("-------------------------")
print(f"Expected Return : {best_return:.4f}")
print(f"Risk            : {best_risk:.4f}")
print(f"Sharpe Ratio    : {best_sharpe:.4f}")
# Save portfolio allocation
portfolio_df = pd.DataFrame({
    "Fund": mean_returns.index,
    "Weight": best_weights
})

portfolio_df = portfolio_df.sort_values(
    by="Weight",
    ascending=False
)

os.makedirs("reports", exist_ok=True)

portfolio_df.to_csv(
    "reports/portfolio_allocation.csv",
    index=False
)

print("\nPortfolio allocation saved.")
# Plot Efficient Frontier
os.makedirs("reports/charts", exist_ok=True)

plt.figure(figsize=(10, 6))

plt.scatter(
    results[1],
    results[0],
    c=results[2],
    alpha=0.4
)

plt.scatter(
    best_risk,
    best_return,
    marker="*",
    s=300
)

plt.title("Markowitz Efficient Frontier")
plt.xlabel("Risk (Volatility)")
plt.ylabel("Expected Return")

plt.colorbar(label="Sharpe Ratio")

plt.tight_layout()

plt.savefig(
    "reports/charts/efficient_frontier.png",
    dpi=300
)

# Don't use plt.show() because it can freeze on Windows
plt.close()

print("\nEfficient Frontier chart saved.")
print("reports/charts/efficient_frontier.png")