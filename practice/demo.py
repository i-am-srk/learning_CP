import sys
import bisect

def get_line():
    return sys.stdin.readline().strip()

def get_ints():
    return list(map(int, get_line().split()))

def write_output(s):
    sys.stdout.write(str(s)+'\n')

def findMin(nums: list[int]) -> int:
    n = len(nums)
    low, high = 0, n-1

    if nums[low]<=nums[high]:
        return nums[low]
    
    while low<high:
        mid =low+(high-low)//2

        if nums[mid]>nums[high]:
            low=mid+1
        else:
            high=mid

    return nums[low]


# str_1 = get_line()
# str_2 = get_line()
nums=get_ints()
# k=int(get_line())
result = findMin(nums)
write_output(result)