import numpy as np
import matplotlib.pyplot as plt

# Step 1: Free Cash Flow Forecasts (in millions)
fcf = [10, 12, 14, 16, 18]  # Forecast for next 5 years
growth_rate = 0.03          # Perpetual growth rate after year 5
discount_rate = 0.10        # Weighted Average Cost of Capital (WACC)

# Step 2: Discount Future Cash Flows
years = np.arange(1, 6)
discounted_fcf = [fcf[i] / (1 + discount_rate)**years[i] for i in range(5)]

# Step 3: Terminal Value
terminal_value = fcf[-1] * (1 + growth_rate) / (discount_rate - growth_rate)
discounted_terminal = terminal_value / (1 + discount_rate)**5

# Step 4: Enterprise Value
enterprise_value = sum(discounted_fcf) + discounted_terminal

# Optional Visualization
plt.plot(years, discounted_fcf, marker='o', label='Discounted FCF')
plt.axhline(y=discounted_terminal, color='r', linestyle='--', label='Discounted Terminal Value')
plt.title('Discounted Cash Flow Valuation')
plt.xlabel('Year')
plt.ylabel('USD (Millions)')
plt.legend()
plt.grid(True)
plt.show()

print(f"\nEstimated Enterprise Value: ${enterprise_value:.2f} million")