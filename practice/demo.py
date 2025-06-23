import sys

def get_line():
    return sys.stdin.readline().strip()

def get_ints():
    return list(map(int, get_line().split()))

def write_output(s):
    sys.stdout.write(str(s)+'\n')

def secondSmallest(nums: list[int]) -> int:
    if len(nums)<2:
        return -1
    small=float('inf')
    second_small=float('inf')
    for i in range(len(nums)):
        if nums[i]<small:
            second_small=small
            small=nums[i]
        elif nums[i]<second_small and nums[i]!=small:
            second_small=nums[i]

    return second_small

def secondLargest(nums: list[int]) -> int:
    if len(nums)<2:
        return -1
    large=float('-inf')
    second_large=float('-inf')
    for i in range(len(nums)):
        if nums[i]>large:
            second_large=large
            large=nums[i]
        elif nums[i]>second_large and nums[i]!=large:
            second_large=nums[i]

    return second_large

nums=get_ints()
write_output(secondSmallest(nums))
write_output(secondLargest(nums))