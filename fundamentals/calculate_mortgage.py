import numpy as np
import matplotlib.pyplot as plt

# Mortgage details
principal = 665000
annual_interest_rate = 0.02375

# Function to calculate the number of years to pay off the mortgage
def years_to_payoff(monthly_payment):
    monthly_interest_rate = annual_interest_rate / 12
    n = np.log(monthly_payment / (monthly_payment - principal * monthly_interest_rate)) / np.log(1 + monthly_interest_rate)
    return n / 12

# Generate data for the plot
monthly_payments = np.linspace(2000, 5000, 100)
years_to_payoff_values = [years_to_payoff(payment) for payment in monthly_payments]

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(monthly_payments, years_to_payoff_values)
plt.xlabel('Monthly Payment ($)')
plt.ylabel('Years to Pay Off Mortgage')
plt.title('Mortgage Payoff Time vs. Monthly Payment')
plt.grid(True)
plt.show()