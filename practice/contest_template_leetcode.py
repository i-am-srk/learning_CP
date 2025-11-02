import sys

def solve(nums: list[int]) -> list[int]:
    n=len(nums)
    nums.sort()

    l, r = nums[0], nums[n-1]
    ans = []
    i = 0

    while l<=r and i<n:
        if nums[i]==l:
            i+=1
            l+=1
            continue
        ans.append(l)
        l+=1

    return ans
    
nums = list(map(int, sys.stdin.readline().strip().split()))
# k = int(sys.stdin.readline().strip())
ans = solve(nums)
print(ans)