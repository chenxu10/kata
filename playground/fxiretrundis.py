# define a function to download FXI historical data from Yahoo Finance
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import lognorm

def download_fxi_historical_data():
    fxi = pd.read_csv('FXI.csv')
    return fxi

# define a function to calculate the daily return of FXI
def calculate_daily_return(fxi):
    fxi['daily_return'] = fxi['Adj Close'].pct_change()
    fxi['daily_return'].fillna(0, inplace=True)
    return fxi


def plot_daily_return(fxi):
    x = fxi['daily_return']
    # sample = x
    # mean = np.mean(sample)
    # std = np.std(sample)
    # y = 1 - lognorm.cdf(0.05, mean, std)
    # print(y)
    # plt.loglog(x,y)
    # plt.show()

    # fit = lognorm.fit(x)
    # # Use the fitted distribution to compute the survival function
    # y = []
    # for i in x:
    #     prob = 1 - lognorm.cdf(i, *fit)
    #     y.append(prob)
    y = 2*x + 10
    plt.loglog(x,y)
    plt.show()

if __name__ == '__main__':
    fxi = calculate_daily_return(download_fxi_historical_data())
    #print(fxi)
    plot_daily_return(fxi)

