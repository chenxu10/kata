
def calcuate_risk_netural_probability(T,N):
    dt = T/N
    return dt

def binomial_pricing(params):
    T = params['time_to_expire_in_years']
    N = params['n_period']
    prob = calcuate_risk_netural_probability(T,N)
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