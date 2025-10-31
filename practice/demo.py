import sys
import bisect

def get_line():
    return sys.stdin.readline().strip()

def get_ints():
    return list(map(int, get_line().split()))

def write_output(s):
    sys.stdout.write(str(s)+'\n')

def countOccurences(nums: list[int], target: int) -> int:
    n=len(nums)
    if n==0:
        return 0
    
    l=bisect.bisect_left(nums, target)
    r=bisect.bisect(nums, target)

    if l>=n:
        return 0
    
    return r-l


nums=get_ints()
target = int(get_line())
result = countOccurences(nums, target)
write_output(result)