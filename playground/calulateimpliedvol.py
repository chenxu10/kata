import scipy.optimize as optimize
import numpy as np
import scipy.stats

def implied_volatility(price, S, K, T, r, option_type):
    """
    Calculate the implied volatility of an option.
    
    Parameters:
    price: float
        The market price of the option
    S: float
        The spot price of the underlying asset
    K: float
        The strike price of the option
    T: float
        The time to expiration of the option in years
    r: float
        The risk-free interest rate
    option_type: str
        'call' or 'put'
    
    Returns:
    implied_vol: float
        The implied volatility of the option
    """
    
    # Define a function to calculate the option price
    # based on the Black-Scholes model
    def option_price(sigma, S, K, T, r, option_type):
        d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
        d2 = d1 - sigma * np.sqrt(T)
        if option_type == 'call':
            return S * scipy.stats.norm.cdf(d1) - K * np.exp(-r * T) * scipy.stats.norm.cdf(d2)
        elif option_type == 'put':
            return K * np.exp(-r * T) * scipy.stats.norm.cdf(-d2) - S * scipy.stats.norm.cdf(-d1)
    
    # Define a function to calculate the difference between the
    # market price and the option price calculated from the
    # Black-Scholes model
    def price_diff(sigma, *args):
        return option_price(sigma, *args) - price
    
    # Use fsolve to find the implied volatility that
    # makes the option price calculated from the
    # Black-Scholes model equal to the market price
    implied_vol = optimize.fsolve(price_diff, x0=1, args=(S, K, T, r, option_type))[0]
    
    return implied_vol

if __name__ == '__main__':
    print(implied_volatility(0.72,28,31,0.3,0.04,'call'))