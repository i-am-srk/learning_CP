import sys
import bisect

def get_line():
    return sys.stdin.readline().strip()

def get_ints():
    return list(map(int, get_line().split()))

def write_output(s):
    sys.stdout.write(str(s)+'\n')

def singleNonDuplicate(nums: list[int]) -> int:
    n=len(nums)
    if n==1:
        return nums[0]
    
    low, high=0,n-1
    while low < high:
        mid = low+(high-low)//2

        if mid%2==1:
            mid-=1
        
        if nums[mid]==nums[mid+1]:
            low=mid+2
        else:
            high=mid
    
    return nums[low]



nums=get_ints()
# target = int(get_line())
result = singleNonDuplicate(nums)
write_output(result)