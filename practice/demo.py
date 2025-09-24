import sys

def get_line():
    return sys.stdin.readline().strip()

def get_ints():
    return list(map(int, get_line().split()))

def write_output(s):
    sys.stdout.write(str(s)+'\n')

def majorityElement(nums: list[int]) -> int:
    candidate, count = None, 0
    for ele in nums:
        if count==0:
            candidate=ele
        count=+1 if ele==candidate else -1

    return candidate

nums=get_ints()
result = majorityElement(nums)
write_output(result)