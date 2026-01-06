import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import warnings
warnings.filterwarnings('ignore')

def simulate_gbm_manual(S0=100, sigma=0.157, n_days=248):
    """
    Simulate Geometric Brownian Motion manually using the formula from the PDF.
    
    Parameters:
    -----------
    S0 : float
        Initial asset price (default: 100)
    sigma : float
        Annual volatility (default: 0.157 = 15.7%)
    n_days : int
        Number of trading days (default: 248)
    seed : int, optional
        Random seed for reproducibility
        
    Returns:
    --------
    tuple : (time array, price array)
    """
    # Generate random numbers from standard normal distribution
    W = np.random.randn(n_days)
    
    # Time step (1 trading day, assuming 248 trading days per year)
    t = 1/248
    sqrt_t = np.sqrt(t)
    
    # Initialize price array
    prices = np.zeros(n_days + 1)
    prices[0] = S0
    
    # Calculate prices using the GBM formula from PDF
    for i in range(1, n_days + 1):
        drift_term = -0.5 * sigma**2 * t
        random_term = sigma * sqrt_t * W[i-1]
        prices[i] = prices[i-1] * np.exp(drift_term + random_term)
    
    time = np.arange(0, n_days + 1)

    return time, prices

def plot_gbm(S0, sigma, n_simulations, n_days):
    plt.figure(figsize=(12,6))
    
    for _ in range(n_simulations):
        time, prices = simulate_gbm_manual(S0, sigma, n_days)

    plt.plot(time, prices)
    plt.title("geometric brownie motion simulation")
    plt.xlabel("days")
    plt.ylabel("prices")
    plt.show()

if __name__ == "__main__":
    plot_gbm(S0=81, sigma=0.18, n_simulations=1, n_days=248)