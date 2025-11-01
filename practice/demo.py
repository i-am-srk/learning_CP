import sys
import bisect

def get_line():
    return sys.stdin.readline().strip()

def get_ints():
    return list(map(int, get_line().split()))

def write_output(s):
    sys.stdout.write(str(s)+'\n')

def findRotation(nums: list[int]) -> int:
    n=len(nums)
    if n==0:
        return 0

    low, high = 0, n-1
    if nums[low] <= nums[high]:
        return low
    
    while low<high:
        mid = low+(high-low)//2
        if nums[mid]>nums[high]:
            low=mid+1
        else:
            high=mid

    return low


nums=get_ints()
# target = int(get_line())
result = findRotation(nums)
write_output(result)