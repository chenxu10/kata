import numpy as np

def generate_brownian_motion(n, T, sigma):
    """
    Generate a Brownian motion path.
    
    :param n: Number of steps
    :param T: Total time
    :param sigma: Volatility
    :return: Array representing the Brownian motion path
    
    Proof of why standard deviation is proportional to square root of time:
    
    1. In Brownian motion, increments are independent and normally distributed.
    2. For a single step, the variance is: Var(dW) = dt
    3. For n steps (total time T), we have: T = n * dt
    4. The total change over time T is the sum of n independent increments:
       W(T) = dW_1 + dW_2 + ... + dW_n
    5. Since increments are independent, variances add:
       Var(W(T)) = Var(dW_1) + Var(dW_2) + ... + Var(dW_n)
                 = n * Var(dW) = n * dt = T
    6. Standard deviation is the square root of variance:
       Std(W(T)) = sqrt(Var(W(T))) = sqrt(T)
    7. Including volatility σ, we get:
       Std(σW(T)) = σ * sqrt(T)
    
    Thus, the standard deviation of Brownian motion is proportional to sqrt(T).
    """
    dt = T / n
    dW = np.random.normal(0, np.sqrt(dt), n)
    W = np.cumsum(dW)
    return np.insert(sigma * W, 0, 0)