import sys

def get_line():
    return sys.stdin.readline().strip()

def get_ints():
    return list(map(int, get_line().split()))

def write_output(s):
    sys.stdout.write(str(s)+'\n')

def maxSubarrayLen(nums: list[int], target: int) -> int:
    sum_to_index = {0:-1}
    max_length, cumulative_sum = 0, 0
    for index, num in enumerate(nums):
        cumulative_sum+=num

        if (cumulative_sum-target) in sum_to_index:
            max_length = max(max_length, index-sum_to_index[cumulative_sum-target])

        if cumulative_sum not in sum_to_index:
            sum_to_index[cumulative_sum] = index
    
    return max_length

nums=get_ints()
target = int(get_line())
result = maxSubarrayLen(nums, target)
write_output(result)