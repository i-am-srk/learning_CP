import sys

def get_line():
    return sys.stdin.readline().strip()

def get_ints():
    return list(map(int, get_line().split()))

def write_output(s):
    sys.stdout.write(str(s)+'\n')

def maximumMedianSum(nums: list[int]) -> int:
    n = len(nums)
    nums.sort()
    l, r = 0, n-1
    median_sum=0
    while(l<r and l<r-1):
        median_sum += nums[r-1]
        l+=1
        r-=2
    return median_sum

nums=get_ints()
result = maximumMedianSum(nums)
write_output(result)