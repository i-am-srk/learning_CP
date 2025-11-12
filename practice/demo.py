import sys
import bisect

def get_line():
    return sys.stdin.readline().strip()

def get_ints():
    return list(map(int, get_line().split()))

def write_output(s):
    sys.stdout.write(str(s)+'\n')

def search_II(nums: list[int], target: int) -> bool:
    n = len(nums)
    low, high = 0, n-1

    while low<=high:
        mid = low+(high-low)//2

        if nums[mid]==target:
            return True
        
        if nums[mid]==nums[low] and nums[mid]==nums[high]:
            low+=1
            high-=1
            continue 

        if nums[mid]>=nums[low]:
            if nums[low]<=target and target<nums[mid]:
                high = mid-1
            else:
                low = mid+1
        else:
            if nums[mid]<target and target<=nums[high]:
                low = mid+1
            else:
                high = mid-1
    
    return False

# str_1 = get_line()
# str_2 = get_line()
nums=get_ints()
k=int(get_line())
result = search_II(nums, k)
write_output(result)