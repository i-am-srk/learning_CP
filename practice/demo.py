import sys

def get_line():
    return sys.stdin.readline().strip()

def get_ints():
    return list(map(int, get_line().split()))

def write_output(s):
    sys.stdout.write(str(s)+'\n')

def maxSubArray(nums: list[int]) -> int:
    global_max = float('-inf')
    current_max = 0
    for num in nums:
        current_max=max(num, current_max+num)
        global_max=max(global_max, current_max)
    
    return global_max

nums=get_ints()
result = maxSubArray(nums)
write_output(result)