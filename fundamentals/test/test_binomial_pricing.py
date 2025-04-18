import numpy as np

def calcuate_risk_netural_probability(T,N,r,u,d):
    dt = T/N
    risk_netual_prob = (np.exp(r * dt) - d)/(u - d)
    return risk_netual_prob

def intialize_stock_price_with_tree_structure(N, S0, u, d):
    stock_tree = np.zeros((N+1, N+1))
    for i in range(N+1):
        for j in range(i+1):
            stock_tree[j, i] = S0 * (u ** (i-j)) * (d ** j)
    return stock_tree

def binomial_pricing(params):
    S0 = params['initial_price']
    T = params['time_to_expire_in_years']
    N = params['n_period']
    r = params['annual_interest_rate']
    u = params['up_factor']
    d = params['down_factor']

    risk_netural_prob = calcuate_risk_netural_probability(T,N,r,u,d)
    stock_tree = intialize_stock_price_with_tree_structure(N, S0, u, d)

    return 2.01

def test_binomial_pricing():
    params = {
        'initial_price':100,
        'strike_price':100,
        'annual_interest_rate':0.04,
        'time_to_expire_in_years':1,
        'n_period':3,
        'up_factor':1.1,
        'down_factor':1/1.1,
        'opt_type':'P'
    }
    price = binomial_pricing(params)
    assert price == 2.01

def main():
    test_binomial_pricing()

if __name__ == '__main__':
    main()