import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sts
from scipy.stats import pareto
from math import sqrt

def clt_simulation_from_uniform(draw_times=300):
    n = 1000
    alpha = 2
    x = [pareto.pdf(np.linspace(-5, 5, n), scale=1, b=alpha) for _ in range(draw_times)]
    # print(x)
    # x = [np.random.uniform(0,5,size=n) for _ in range (draw_times)]
    s = np.sum(x,axis=0)
    print(s)
    plt.hist(s, bins=50, density=True)
    plt.show()

def simple_heuristics_to_create_fat_tail():
    b = 2
    n = 1000
    c = 1
    x = np.random.rand(n)
    Y = 2 * x ** b
    plt.hist(Y, bins=50)
    plt.show()

def log_normal_plot():
    # Set the mean and standard deviation of the distribution
    mu, sigma = -0.69, 0.1

    # Generate a log-normal distribution using NumPy's lognormal function
    ln_dist = np.random.lognormal(mean=mu, sigma=sigma, size=1000)

    # Plot the distribution using Matplotlib
    plt.hist(ln_dist, bins=50)
    plt.title("Log-Normal Distribution")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.show()

if __name__ == '__main__':
    #clt_simulation_from_uniform()
    #simple_heuristics_to_create_fat_tail()
    log_normal_plot()