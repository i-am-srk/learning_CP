import sys
import bisect

def get_line():
    return sys.stdin.readline().strip()

def get_ints():
    return list(map(int, get_line().split()))

def write_output(s):
    sys.stdout.write(str(s)+'\n')

def searchRange(nums: list[int], target: int) -> list[int]:
    if len(nums)==0 or nums[-1]<target:
        return [-1,-1]
    
    l = bisect.bisect_left(nums, target)
    r = bisect.bisect_right(nums, target)-1

    if nums[l]==target and nums[r]==target:
        return [l,r]

    return [-1,-1]

nums=get_ints()
target = int(get_line())
result = searchRange(nums, target)
write_output(result)