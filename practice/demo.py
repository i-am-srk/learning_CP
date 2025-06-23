import sys

def get_line():
    return sys.stdin.readline().strip()

def get_ints():
    return list(map(int, get_line().split()))

def write_output(s):
    sys.stdout.write(str(s)+'\n')

def largestElement(nums: list[int]) -> int:
    maxi=nums[0]
    for i in range(len(nums)):
        if nums[i]>maxi:
            maxi=nums[i]
    return maxi

nums=get_ints()
write_output(largestElement(nums))