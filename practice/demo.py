import sys

def get_line():
    return sys.stdin.readline().strip()

def get_ints():
    return list(map(int, get_line().split()))

def write_output(s):
    sys.stdout.write(str(s)+'\n')

# k=3, p=1
def singleNumber(nums: list[int]) -> list[int]:
    xor = 0
    for num in nums:
        xor^=num

    set_bit = xor & -xor
    
    a, b = 0, 0
    for num in nums:
        if num & set_bit:
            a^=num
        else:
            b^=num

    return [a,b]

nums=get_ints()
result = singleNumber(nums)
write_output(result)