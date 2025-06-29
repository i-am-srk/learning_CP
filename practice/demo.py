import sys

def get_line():
    return sys.stdin.readline().strip()

def get_ints():
    return list(map(int, get_line().split()))

def write_output(s):
    sys.stdout.write(str(s)+'\n')

def removeDuplicates(nums: list[int]) -> int:
    n = len(nums)
    if n<=1:
        return 1
    l = 0
    for r in range(1, n):
        if nums[r]==nums[l]:
            if l-1>=0 and nums[r]==nums[l-1]:
                r+=1
            else:
                l+=1
                r+=1
        else:
            if l-1>=0 and nums[r]==nums[l-1]:
                r+=1
            elif l-1>=0 and nums[r]!=nums[l-1]:
                nums[r], nums[l] = nums[l], nums[r]
                l+=1
                r+=1
            else:
                l+=2
                r+=2

    return l


nums=get_ints()
write_output(removeDuplicates(nums))
write_output(nums)