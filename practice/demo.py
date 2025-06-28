import sys

def get_line():
    return sys.stdin.readline().strip()

def get_ints():
    return list(map(int, get_line().split()))

def write_output(s):
    sys.stdout.write(str(s)+'\n')

def check(nums: list[int]) -> bool:
    n=len(nums)
    if n <= 1:
        return True
    
    inversion_count=0
    for i in range(1,n):
        if nums[i] < nums[i-1]:
            inversion_count+=1

        if inversion_count > 1:
            return False
        
    if nums[0] < nums[n-1]:
        inversion_count+=1

    return inversion_count <= 1

nums = get_ints()
write_output(check(nums))