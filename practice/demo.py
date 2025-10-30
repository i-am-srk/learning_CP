import sys

def get_line():
    return sys.stdin.readline().strip()

def get_ints():
    return list(map(int, get_line().split()))

def write_output(s):
    sys.stdout.write(str(s)+'\n')

def iterativeBS(nums: list[int], target: int) -> int:
    n=len(nums)
    x=0
    b=n//2
    while b>=1:
        while (x+b)<n and nums[x+b]<=target:
            x+=b
        b//=2
    
    if nums[x]==target:
        return x
    
    return -1


nums=get_ints()
target = int(get_line())
result = iterativeBS(nums, target)
write_output(result)