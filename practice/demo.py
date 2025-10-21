import sys

def get_line():
    return sys.stdin.readline().strip()

def get_ints():
    return list(map(int, get_line().split()))

def write_output(s):
    sys.stdout.write(str(s)+'\n')

def subarraySum(nums: list[int], k: int) -> int:
    count = 0
    current_sum = 0
    prefix_sum = {}
    prefix_sum[0]=1

    for num in nums:
        current_sum+=num
        if current_sum-k in prefix_sum:
            count+=prefix_sum[current_sum-k]
        prefix_sum[current_sum]=prefix_sum.get(current_sum, 0)+1

    return count


nums=get_ints()
k=int(get_line())
result = subarraySum(nums, k)
write_output(result)