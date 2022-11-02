# QQplot 
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

#create dataset with 100 values that follow a normal distribution
np.random.seed(0)
data = np.random.normal(0,1, 1000)
fig = sm.qqplot(data, line='45')
plt.show()

# qqplot for lognormal
data = np.random.lognormal(0,1, 1000)
fig = sm.qqplot(data, line='45')
plt.show()

# qqplot for exponential
data = np.random.exponential(scale=1, size=1000)
fig = sm.qqplot(data, line='45')
plt.show()