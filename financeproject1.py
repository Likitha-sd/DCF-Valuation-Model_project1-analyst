import numpy as np
import matplotlib.pyplot as plt

def forecast_fcf(years, base_fcf, increment):
    """Generates forecasted Free Cash Flows (FCF) for given years."""
    return [base_fcf + i * increment for i in range(years)]

def discount_cash_flows(fcf, discount_rate):
    """Discounts each FCF to present value."""
    return [fcf[i] / (1 + discount_rate)**(i + 1) for i in range(len(fcf))]

def calculate_terminal_value(last_fcf, growth_rate, discount_rate, year):
    """Calculates and discounts terminal value."""
    terminal_value = last_fcf * (1 + growth_rate) / (discount_rate - growth_rate)
    discounted_terminal = terminal_value / (1 + discount_rate)**year
    return discounted_terminal

def compute_enterprise_value(discounted_fcf, discounted_terminal):
    """Sums discounted FCFs and terminal value to get enterprise value."""
    return sum(discounted_fcf) + discounted_terminal

def plot_valuation(years, discounted_fcf, discounted_terminal):
    """Visualizes the discounted cash flows and terminal value."""
    plt.plot(years, discounted_fcf, marker='o', label='Discounted FCF')
    plt.axhline(y=discounted_terminal, color='r', linestyle='--', label='Discounted Terminal Value')
    plt.title('Discounted Cash Flow Valuation')
    plt.xlabel('Year')
    plt.ylabel('USD (Millions)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    # Inputs
    forecast_years = 5
    base_fcf = 10
    increment = 2
    growth_rate = 0.03
    discount_rate = 0.10

    # Step 1: Forecast FCF
    fcf = forecast_fcf(forecast_years, base_fcf, increment)

    # Step 2: Discount FCF
    discounted_fcf = discount_cash_flows(fcf, discount_rate)

    # Step 3: Terminal Value
    discounted_terminal = calculate_terminal_value(fcf[-1], growth_rate, discount_rate, forecast_years)

    # Step 4: Enterprise Value
    enterprise_value = compute_enterprise_value(discounted_fcf, discounted_terminal)

    # Step 5: Visualization
    years = np.arange(1, forecast_years + 1)
    plot_valuation(years, discounted_fcf, discounted_terminal)

    print(f"\nEstimated Enterprise Value: ${enterprise_value:.2f} million")

if __name__ == "__main__":
    main()
