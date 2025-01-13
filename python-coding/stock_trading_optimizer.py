"""
Stock Trading Profit Optimizer

Time: 30-40 minutes
Difficulty: Medium

Problem:
Design a stock trading system that helps users maximize their profits. Implement a StockTrader class that manages
buying and selling stocks while tracking profits/losses.

Requirements:
1. Implement a StockTrader class with following methods:
   - record_price(timestamp: int, price: float) -> None  # Records stock price at given timestamp
   - buy(timestamp: int, quantity: int) -> bool  # Attempts to buy stocks at given timestamp
   - sell(timestamp: int, quantity: int) -> bool  # Attempts to sell stocks at given timestamp
   - get_profit() -> float  # Returns total profit/loss
   
2. Business Rules:
   - Can't sell stocks you don't own (need to buy first)
   - Can't buy/sell at timestamps where price isn't recorded
   - All transactions should maintain FIFO order
   - Each transaction should calculate profit/loss based on buy/sell price difference

3. Example Usage:
trader = StockTrader()
trader.record_price(1, 10.0)  # Stock price $10 at timestamp 1
trader.record_price(2, 15.0)  # Stock price $15 at timestamp 2
trader.buy(1, 10)            # Buy 10 stocks at timestamp 1 ($10 each)
trader.sell(2, 5)            # Sell 5 stocks at timestamp 2 ($15 each) -> Profit: $25

Expected Solution Structure:
- Use OOP principles
- Handle edge cases and invalid inputs
- Optimize for time/space complexity
- Include basic error handling
"""

class StockTrader:
    def __init__(self):
        # Initialize your data structures here
        pass

    def record_price(self, timestamp: int, price: float) -> None:
        # Implement price recording logic
        pass

    def buy(self, timestamp: int, quantity: int) -> bool:
        # Implement buy logic
        pass

    def sell(self, timestamp: int, quantity: int) -> bool:
        # Implement sell logic
        pass

    def get_profit(self) -> float:
        # Implement profit calculation
        pass

# Optional Test Cases
def test_stock_trader():
    trader = StockTrader()
    trader.record_price(1, 10.0)
    trader.record_price(2, 15.0)
    trader.record_price(3, 8.0)
    
    assert trader.buy(1, 10) == True
    assert trader.sell(2, 5) == True
    assert trader.sell(3, 5) == True
    assert trader.get_profit() == 25.0  # (15-10)*5 + (8-10)*5

    print("All test cases passed!")

"""
This problem tests:

- OOP implementation
- Data structure selection
- Transaction handling
- Error cases
- Time/price tracking
- Profit calculation
- FIFO order maintenance

The candidate should:

1. Implement proper data structures for price/transaction storage
2. Handle edge cases (invalid timestamps, quantities)
3. Maintain transaction order
4. Calculate profits correctly
5. Consider time/space complexity

"""
