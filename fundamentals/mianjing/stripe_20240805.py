


class CurrencyConverter:
    def get_direct_rate(x,y):
        pass

def test_get_direct_rate():
    """

    """
    rates_string = "USD:AUD:1.4,CAD:USD:0.8,USD:JPY:110"
    converter = CurrencyConverter(rates_string)   
    print(converter.get_direct_rate("USD", "AUD"))  # 1.4


    # Part 2: 通過一次轉換計算轉換率
    print(converter.get_one_hop_rate("CAD", "AUD"))  # 1.12 (CAD -> USD -> AUD)

    # Part 3: 使用最佳轉換率
    print(converter.get_best_rate("USD", "AUD"))  # 1.4

    # Part 4: 返回所有可計算的轉換率對
    print(converter.get_all_possible_rates())