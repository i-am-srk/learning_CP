import sys
import bisect

def get_line():
    return sys.stdin.readline().strip()

def get_ints():
    return list(map(int, get_line().split()))

def write_output(s):
    sys.stdout.write(str(s)+'\n')

def distinct_nos(nums: list) -> int:
    n=len(nums)
    if n<2:
        return 1
    
    nums.sort() # n(logn)
    i,distincts=0,0
    while i<n: # k(logn): k is distinct numbers
        distincts+=1
        i = bisect.bisect_right(nums,nums[i],lo=i)

    return distincts


# str_1 = get_line()
# str_2 = get_line()
k=int(get_line())
nums=get_ints()
result = distinct_nos(nums)
write_output(result)