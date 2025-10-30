import sys

def get_line():
    return sys.stdin.readline().strip()

def get_ints():
    return list(map(int, get_line().split()))

def write_output(s):
    sys.stdout.write(str(s)+'\n')

def insertSearch(nums: list[int], target: int) -> int:
    n=len(nums)
    low,high=0,n

    while low<high:
        mid=low+(high-low)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            high-=1
        else:
            low+=1

    return low


nums=get_ints()
k = int(get_line())
result = insertSearch(nums, k)
write_output(result)