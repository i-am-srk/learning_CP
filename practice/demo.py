import sys
import bisect

def get_line():
    return sys.stdin.readline().strip()

def get_ints():
    return list(map(int, get_line().split()))

def write_output(s):
    sys.stdout.write(str(s)+'\n')

def getFloorAndCeil(nums: list[int], target: int) -> int:
    n=len(nums)
    floor, ceil = -1, -1

    ceil_index = bisect.bisect_left(nums, target)
    if ceil_index<n:
        ceil = nums[ceil_index]

    floor_index = bisect.bisect_right(nums, target)-1
    if floor_index>=0:
        floor = nums[floor_index]

    return (floor, ceil)


nums=get_ints()
target = int(get_line())
result = getFloorAndCeil(nums, target)
write_output(result)