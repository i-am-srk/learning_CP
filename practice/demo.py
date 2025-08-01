import sys

def get_line():
    return sys.stdin.readline().strip()

def get_ints():
    return list(map(int, get_line().split()))

def write_output(s):
    sys.stdout.write(str(s)+'\n')

def singleNumber(nums: list[int]) -> int:
    res = 0
    for num in nums:
        res = res^num
    return res

nums=get_ints()
result = singleNumber(nums)
write_output(result)