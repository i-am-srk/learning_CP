import sys

def get_line():
    return sys.stdin.readline().strip()

def get_ints():
    return list(map(int, get_line().split()))

def write_output(s):
    sys.stdout.write(str(s)+'\n')

def rotateArray(nums: list[int], start: int, end: int):
    n = end-start
    k = n-1
    nums[start:end] = reversed(nums[start:end])
    nums[start:start+k] = reversed(nums[start:start+k])
    nums[start+k:end] = reversed(nums[start+k:end])

def moveZeros(nums: list[int]):
    n = len(nums)
    zeros_count = 0
    for i in range(n-1, -1, -1):
        if nums[i]!=0:
            continue
        else:
            start = i
            end = n-zeros_count
            rotateArray(nums, start, end)
            zeros_count+=1


nums=get_ints()
moveZeros(nums)
write_output(nums)