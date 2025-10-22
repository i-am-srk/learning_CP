import sys

def get_line():
    return sys.stdin.readline().strip()

def get_ints():
    return list(map(int, get_line().split()))

def write_output(s):
    sys.stdout.write(str(s)+'\n')

def upperBound(nums: list[int], x: int) -> int:
    n = len(nums)
    low, high = 0, n
    ans = n

    while low < high:
        mid = low + (high-low)//2
        if nums[mid] > x:
            ans = mid
            high = mid
        else:
            low = mid+1

    return ans

nums=get_ints()
k = int(get_line())
result = upperBound(nums, k)
write_output(result)