


class CurrencyConverter:
    def get_direct_rate(x,y):
        pass

def test_get_direct_rate():
    """

    """
    rates_string = "USD:AUD:1.4,CAD:USD:0.8,USD:JPY:110"
    converter = CurrencyConverter(rates_string)   
    print(converter.get_direct_rate("USD", "AUD"))  # 1.4
