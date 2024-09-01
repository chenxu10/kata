import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def generate_brownian_motion(n, T, sigma):
    """
    Generate a Brownian motion path.
    
    :param n: Number of steps
    :param T: Total time
    :param sigma: Volatility
    :return: Array representing the Brownian motion path
    """
    dt = T / n
    dW = np.random.normal(0, np.sqrt(dt), n)
    W = np.cumsum(dW)
    return np.insert(sigma * W, 0, 0)

def test_brownian_motion():
    """
    This tests generate_brownian_motion function and illustrates the Central Limit Theorem
    """
    n = 10000  # number of steps (increased for better illustration)
    T = 1.0   # total time
    sigma = 1.0  # volatility
    
    path = generate_brownian_motion(n, T, sigma)
    
    # Test 1: Check if the length of the path is correct
    assert len(path) == n + 1, "Path length is incorrect"
    
    # Test 2: Check if the path starts at 0
    assert path[0] == 0, "Path should start at 0"
    
    # Test 3: Check if the increments are normally distributed
    increments = np.diff(path)
    expected_mean = 0
    expected_std = sigma * np.sqrt(T / n)
    
    assert np.abs(np.mean(increments) - expected_mean) < 0.1, "Mean of increments is off"
    assert np.abs(np.std(increments) - expected_std) < 0.1, "Standard deviation of increments is off"


if __name__ == "__main__":
    test_brownian_motion()
