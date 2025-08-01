import sys

def get_line():
    return sys.stdin.readline().strip()

def get_ints():
    return list(map(int, get_line().split()))

def write_output(s):
    sys.stdout.write(str(s)+'\n')

# k=3, p=1
def singleNumber(nums: list[int]) -> int:
    x1, x2, mask = 0, 0, 0
    for num in nums:
        x2^=x1&num
        x1^=num
        mask=~(x1&x2)
        x2&=mask
        x1&=mask
    
    return x1|x2

nums=get_ints()
result = singleNumber(nums)
write_output(result)