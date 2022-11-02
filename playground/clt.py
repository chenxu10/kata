import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sts
from math import sqrt

# generates 'number_of_samples' samples of size 'samples_size' and returns an array of their means
def samples(random_value, sample_size, number_of_samples):
    result = np.asarray([])
    for i in range(number_of_samples):
        result = np.append(result, np.mean(random_value.rvs(sample_size)))
    return result

n = 10
b = 3.0
random_value = sts.pareto(b)
mean = random_value.mean()
variance = random_value.var()
print(mean)
print(variance)

plt.hist(samples(random_value, n, 1000), bins=20, normed=True)

x = np.linspace(0, 6, 100)
pdf = sts.norm(mean, sqrt(variance / n)).pdf(x)
plt.plot(x, pdf, color='r', label='theoretical PDF')

# **Example 1 ***
#Suppose we have a fair coin and we flip it 400 times. What is the probability you will see 210 heads or more?
#***Example 2:***
#Suppose you use Monte Carlo simulation to estimate the numerical value of .
#How would you implement it?
#If we require an error of 0.001, how many trials do you need?