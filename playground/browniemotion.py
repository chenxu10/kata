import random
import numpy as np
import matplotlib.pyplot as plt
# generate 248 random numbers with mean=0 standard deviation=1 from normal distribution

def normal_distribution():
    mu, sigma = 0, 1 # mean and standard deviation
    s = np.random.normal(mu, sigma, 248)
    count, bins, ignored = plt.hist(s, 30, density=True)
    plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
    np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
    linewidth=2, color='r')
    plt.show()

def generate_oneasset_rw(startingprice=100, timesteps=251):
    s = [startingprice]
    sigma = 0.157

    for i in range(timesteps):
        snext = s[-1] * np.exp(-0.5 * sigma**2 * (1/248) + sigma * (1/15.7) * random.choice([-1,1]))
        s.append(snext)
    
    plt.plot(s)
    return s

# Given annual standard deviation, calculate daily standard deviation
def daily_stddev(annual_stddev):
    return annual_stddev / np.sqrt(248)

if __name__ == "__main__":
    #normal_distribution()
    #print(daily_stddev(0.157))
    generate_oneasset_rw(startingprice=100,timesteps=251)

