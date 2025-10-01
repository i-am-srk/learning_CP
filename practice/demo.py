import sys

def get_line():
    return sys.stdin.readline().strip()

def get_ints():
    return list(map(int, get_line().split()))

def write_output(s):
    sys.stdout.write(str(s)+'\n')

def maxProfit(prices: list[int]) -> int:
    if not prices:
        return 0
    
    min_price = prices[0]
    max_profit = 0
    for price in prices[1:]:
        current_profit = price - min_price
        max_profit = max(max_profit, current_profit)
        min_price = min(min_price, price)

    return max_profit


nums=get_ints()
result = maxProfit(nums)
write_output(result)