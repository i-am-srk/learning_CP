import sys

def check(nums: list[int], x: float) -> bool:
    
    n=len(nums)
    max_so_far=float('-inf')
    current_psum=0.0
    min_psum=0.0

    for num in nums:
        current_psum+=num-x
        max_so_far=max(max_so_far, current_psum-min_psum)
        min_psum=min(min_psum, current_psum)

    return max_so_far>=0

def findMaxAverage(nums: list[int]) -> int:
    
    if not nums:
        return 0
    
    # search range
    min_val=min(nums)
    max_val=max(nums)

    low=float(min_val)
    high=float(max_val)

    # required precision
    TOLERANCE=1e-6

    # binary search loop
    while (high-low) > TOLERANCE:
        mid=(low+high)/2

        # avg=mid is possible
        if check(nums, mid):
            low=mid
        else:
            high=mid

    return int(low+TOLERANCE)


# the number of test cases
t = int(sys.stdin.readline().strip())

while t:
    
    # length of the input array
    n = int(sys.stdin.readline().strip())

    #
    a = list(map(int, sys.stdin.readline().strip().split()))

    # driver code
    ans=findMaxAverage(a)

    # output the result
    sys.stdout.write(str(ans)+'\n')

    t-=1

