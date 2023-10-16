import numpy as np

# Simulated stock prices for 100 days
stock_prices = np.array([50, 51, 52.5, 53, 54, 52, 53, 54, 56, 57])

# Calculate daily percentage changes
daily_changes = np.diff(stock_prices) / stock_prices[:-1] * 100

# Compute mean and standard deviation of daily changes
mean_change = np.mean(daily_changes)
std_change = np.std(daily_changes)

print(f"Average Daily Change: {mean_change:.2f}%")
print(f"Volatility: {std_change:.2f}%")
