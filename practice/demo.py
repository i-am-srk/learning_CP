import sys

def get_line():
    return sys.stdin.readline().strip()

def get_ints():
    return list(map(int, get_line().split()))

def write_output(s):
    sys.stdout.write(str(s)+'\n')

def bSearch(nums: list[int], target: int) -> int:
    n = len(nums)
    low, high = 0, n-1
    idx = -1

    while low<=high:
        mid = (low+high)//2
        if nums[mid]==target:
            idx = mid
            break
        elif nums[mid]>target:
            high = mid-1
        else:
            low = mid+1

    return idx

nums=get_ints()
k = int(get_line())
result = bSearch(nums, k)
write_output(result)