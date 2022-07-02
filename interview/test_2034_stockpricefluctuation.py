"""
You are given a stream of records about a particular stock. Each record contains a timestamp and the corresponding price of the stock at that timestamp.

Unfortunately due to the volatile nature of the stock market, the records do not come in order. Even worse, some records may be incorrect. 
Another record with the same timestamp may appear later in the stream correcting the price of the previous wrong record.

Design an algorithm that:

Updates the price of the stock at a particular timestamp, correcting the price from any previous records at the timestamp.
Finds the latest price of the stock based on the current records. The latest price is the price at the latest timestamp recorded.
Finds the maximum price the stock has been based on the current records.
Finds the minimum price the stock has been based on the current records.
Implement the StockPrice class:

StockPrice() Initializes the object with no price records.
void update(int timestamp, int price) Updates the price of the stock at the given timestamp.
int current() Returns the latest price of the stock.
int maximum() Returns the maximum price of the stock.
int minimum() Returns the minimum price of the stock.

Input
["StockPrice", "update", "update", "current", "maximum", "update", "maximum", "update", "minimum"]
[[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]
Output
[null, null, null, 5, 10, null, 5, null, 2]
"""
from sortedcontainers import SortedDict

class StockPrice:

    def __init__(self):
        self.time_to_prices = SortedDict()
        self.prices_to_time = SortedDict()
   
    def update(self, timestamp: int, price: int) -> None:
        # update previous price with time stamp
          # non previouse price in reocrd
        # price not in record need to add a new dict
        # prices_to_time add timestamp
        # timestamp add prices_to_time pair

        if timestamp in self.time_to_prices:
            prev_price = self.time_to_prices[timestamp]
            self.prices_to_time[prev_price].remove(timestamp)
            if len(self.prices_to_time[prev_price]) == 0:
                self.prices_to_time.pop(prev_price)
        
        if not price in self.prices_to_time:
            self.prices_to_time[price] = set()
        
        self.prices_to_time[price].add(timestamp)
        self.time_to_prices[timestamp] = price

    def current(self) -> int:
        return self.time_to_prices.peekitem(-1)[1]

    def maximum(self) -> int:
        return self.prices_to_time.peekitem(-1)[0]

    def minimum(self) -> int:
        return self.prices_to_time.peekitem(0)[0]