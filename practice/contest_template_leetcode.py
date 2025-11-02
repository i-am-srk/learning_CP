import sys
import math

def solve(nums: list[int]) -> int:
    n=len(nums)
    limit = 100000

    max1, max2, max3 = -math.inf, -math.inf, -math.inf
    min1, min2 = math.inf, math.inf

    for x in nums:
        if x>max1:
            max3, max2, max1 = max2, max1, x
        elif x>max2:
            max3, max2 = max2, x
        elif x>max3:
            max3 = x

        if x<min1:
            min2, min1 = min1, x
        elif x<min2:
            min2=x

    best_pos_pair = max(max1 * max2, min1 * min2)
    best_neg_pair = max1 * min1
    product_scenario_B = max(best_pos_pair * limit, best_neg_pair * (-limit))

    if n == 3:
        return product_scenario_B

    product_scenario_A = max(max1 * max2 * max3, min1 * min2 * max1)

    return max(product_scenario_A, product_scenario_B)

nums = list(map(int, sys.stdin.readline().strip().split()))
# k = int(sys.stdin.readline().strip())
ans = solve(nums)
print(ans)