import sys

def get_line():
    return sys.stdin.readline().strip()

def get_ints():
    return list(map(int, get_line().split()))

def write_output(s):
    sys.stdout.write(str(s)+'\n')

def lowerBound(nums: list[int], x: int) -> int:
    n = len(nums)
    low, high = 0, n-1

    while low<high:
        mid=(low+high)//2
        if nums[mid]-x < 0:
            low=mid+1
        else:
            high = mid

    if nums[low] >= x:
        return low
    else:
        return n

nums=get_ints()
k = int(get_line())
result = lowerBound(nums, k)
write_output(result)