import sys

def get_line():
    return sys.stdin.readline().strip()

def get_ints():
    return list(map(int, get_line().split()))

def write_output(s):
    sys.stdout.write(str(s)+'\n')

def linear_search(nums, target):
    target_idx = -1
    for i in range(len(nums)):
        if nums[i]==target:
            target_idx = i
            break
    return target_idx

nums=get_ints()
target = int(get_line())
result = linear_search(nums, target)
write_output(result)