import sys

def get_line():
    return sys.stdin.readline().strip()

def get_ints():
    return list(map(int, get_line().split()))

def write_output(s):
    sys.stdout.write(str(s)+'\n')

def findMaxConsecutiveOnes(nums: list[int]) -> int:
    max_ones = 0
    curr = 0
    for num in nums:
        if num==1:
            curr+=1
        else:
            max_ones = max(curr, max_ones)
            curr=0    
    max_ones = max(curr, max_ones)

    return max_ones

nums=get_ints()
result = findMaxConsecutiveOnes(nums)
write_output(result)