import sys
import bisect

def get_line():
    return sys.stdin.readline().strip()

def get_ints():
    return list(map(int, get_line().split()))

def write_output(s):
    sys.stdout.write(str(s)+'\n')

def hasDuplicate(nums: list[int]) -> bool:
    n=len(nums)
    freq_map = {}
    for num in nums:
        if num in freq_map:
            return True
        freq_map[num]=1

    return False


nums=get_ints()
# target = int(get_line())
result = hasDuplicate(nums)
write_output(result)