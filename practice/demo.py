import sys

def get_line():
    return sys.stdin.readline().strip()

def get_ints():
    return list(map(int, get_line().split()))

def write_output(s):
    sys.stdout.write(str(s)+'\n')

def missingNumber(nums: list[int]) -> int:
    n=len(nums)
    visited=[False]*(n+1)
    
    for num in nums:
        visited[num]=True

    ans=-1
    for i in range(len(visited)):
        if visited[i]:
            continue
        ans = i
        break

    return ans

nums=get_ints()
result = missingNumber(nums)
write_output(result)