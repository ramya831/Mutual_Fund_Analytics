import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------
# Load NAV History
# -----------------------------------
df = pd.read_csv("data/processed/nav_history_clean.csv")

df["date"] = pd.to_datetime(df["date"])

df = df.sort_values(["amfi_code", "date"])

fund_code = df["amfi_code"].iloc[0]

fund = df[df["amfi_code"] == fund_code].copy()

fund["daily_return"] = fund["nav"].pct_change()

fund = fund.dropna()

mean_return = fund["daily_return"].mean()
std_return = fund["daily_return"].std()

print(f"Fund Code : {fund_code}")
print(f"Average Daily Return : {mean_return:.6f}")
print(f"Daily Volatility : {std_return:.6f}")

# -----------------------------------
# Monte Carlo Parameters
# -----------------------------------
simulation_count = 1000
trading_days = 252 * 5

last_nav = fund["nav"].iloc[-1]

# -----------------------------------
# Run Simulations
# -----------------------------------

all_prices = []

for i in range(simulation_count):

    prices = [last_nav]

    for day in range(trading_days):

        random_return = np.random.normal(
            mean_return,
            std_return
        )

        next_price = prices[-1] * (1 + random_return)

        prices.append(next_price)

    all_prices.append(prices)

simulation_df = pd.DataFrame(all_prices).T

# -----------------------------------
# Save Chart
# -----------------------------------

os.makedirs("reports/charts", exist_ok=True)

plt.figure(figsize=(12,6))

plt.plot(simulation_df)

plt.title("Monte Carlo Simulation (5-Year NAV Forecast)")
plt.xlabel("Trading Days")
plt.ylabel("NAV")

plt.tight_layout()

plt.savefig(
    "reports/charts/monte_carlo_simulation.png",
    dpi=300
)

plt.show()

print("\nSimulation Completed Successfully!")
print("\nChart Saved To:")
print("reports/charts/monte_carlo_simulation.png")