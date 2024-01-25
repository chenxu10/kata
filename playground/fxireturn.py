import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def main():
    # Download the data
    data = yf.download("FXI", start="2005-01-01", end="2021-12-31")
    # Calculate the daily returns
    returns = data['Adj Close'].pct_change()
    mu = returns.mean()
    sigma = returns.std()

    # Plot the histogram
    plt.hist(returns, bins=50)
    plt.xlabel('Daily Returns')
    plt.ylabel('Frequency')
    plt.title('Histogram of Daily Returns for FXI')

    # Add the vertical lines
    plt.axvline(x=mu - sigma, c='r', linestyle='--')
    plt.axvline(x=mu + sigma, c='r', linestyle='--')
    plt.axvline(x=mu - 2*sigma, c='g', linestyle='--')
    plt.axvline(x=mu + 2*sigma, c='g', linestyle='--')
    plt.axvline(x=mu - 3*sigma, c='b', linestyle='--')
    plt.axvline(x=mu + 3*sigma, c='b', linestyle='--')

    # Add labels to the vertical lines
    plt.text(mu - sigma, plt.ylim()[1]*0.7, '{:.2%}'.format(mu - sigma))
    plt.text(mu + sigma, plt.ylim()[1]*0.7, '{:.2%}'.format(mu + sigma))
    plt.text(mu - 2*sigma, plt.ylim()[1]*0.7, '{:.2%}'.format(mu - 2*sigma))
    plt.text(mu + 2*sigma, plt.ylim()[1]*0.7, '{:.2%}'.format(mu + 2*sigma))
    plt.text(mu - 3*sigma, plt.ylim()[1]*0.7, '{:.2%}'.format(mu - 3*sigma))
    plt.text(mu + 3*sigma, plt.ylim()[1]*0.7, '{:.2%}'.format(mu + 3*sigma))

    plt.show()
    plt.close()

if __name__ == '__main__':
    main()

