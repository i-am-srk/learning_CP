import sys

def get_line():
    return sys.stdin.readline().strip()

def get_ints():
    return list(map(int, get_line().split()))

def write_output(s):
    sys.stdout.write(str(s)+'\n')

def leaders(nums: list[int]) -> list[int]:
    ans = [nums[-1]]

    for i in range(len(nums)-1, -1, -1):
        if nums[i]>ans[-1]:
            ans.append(nums[i])

    ans.reverse()
    return ans

nums=get_ints()
result = leaders(nums)
write_output(result)