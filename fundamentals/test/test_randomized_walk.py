import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import warnings
warnings.filterwarnings('ignore')

def simulate_gbm_manual(S0=100, sigma=0.157, n_days=248, seed=None):
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
    if seed is not None:
        np.random.seed(seed)
    
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
    
    # Create time array
    time = np.arange(0, n_days + 1)
    
    return time, prices

def plot_gbm_simulation(S0=100, sigma=0.157, n_days=248, seed=None, 
                        n_simulations=1, figsize=(12, 6)):
    """
    Plot GBM simulations similar to Figure A.2 in the PDF.
    
    Parameters:
    -----------
    S0 : float
        Initial asset price
    sigma : float
        Annual volatility
    n_days : int
        Number of trading days
    seed : int, optional
        Random seed
    n_simulations : int
        Number of simulation paths to plot
    figsize : tuple
        Figure size
    """
    plt.figure(figsize=figsize)
    
    for i in range(n_simulations):
        if seed is not None:
            current_seed = seed + i
        else:
            current_seed = None
            
        time, prices = simulate_gbm_manual(S0, sigma, n_days, current_seed)
        
        plt.plot(time, prices, alpha=0.7 if n_simulations > 1 else 1.0,
                label=f'Simulation {i+1}' if n_simulations > 1 else None)
    
    plt.xlabel('Trading Days', fontsize=12)
    plt.ylabel('Asset Price', fontsize=12)
    plt.title(f'Geometric Brownian Motion Simulation\n'
              f'S₀={S0}, σ={sigma*100:.1f}%, {n_days} trading days',
              fontsize=14, fontweight='bold')
    
    if n_simulations > 1:
        plt.legend()
    
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    
if __name__ == "__main__":
    print("GBM Simulation Example (Matching PDF Figure A.2)")
    print("=" * 50)
    plot_gbm_simulation(S0=81, sigma=0.1813, n_days=248, 
                       seed=None, n_simulations=10)