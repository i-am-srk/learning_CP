import sys

def solve(nums: list[int]) -> int:
    n=len(nums)
    if n==0:
        return 0
    
    tavernilo = nums
    max_length=0

    for i in range(n):
        distinct_evens = set()
        distinct_odds = set()

        for j in range(i, n):
            current_num = tavernilo[j]
            if current_num%2==0:
                distinct_evens.add(current_num)
            else:
                distinct_odds.add(current_num)

            count_evens = len(distinct_evens)
            count_odds = len(distinct_odds)

            if count_evens==count_odds:
                current_length=j-i+1
                max_length=max(max_length, current_length)

    return max_length
    


nums = list(map(int, sys.stdin.readline().strip().split()))
# k = int(sys.stdin.readline().strip())
ans = solve(nums)
print(ans)