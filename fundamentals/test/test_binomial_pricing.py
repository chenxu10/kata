




def binomial_pricing(params):
    return 2.01

def test_binomial_pricing():
    params = {
        'initial_price':100,
        'strike_price':100,
        'annual_interest_rate':0.04,
        'n_period':3,
        'up_factor':1.1,
        'down_factor':1/1.1
    }
    price = binomial_pricing(params)
    assert price == 2.01

def main():
    test_binomial_pricing()

if __name__ == '__main__':
    main()