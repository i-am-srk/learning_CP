import sys

def get_line():
    return sys.stdin.readline().strip()

def get_ints():
    return list(map(int, get_line().split()))

def write_output(s):
    sys.stdout.write(str(s)+'\n')

class Solution:
    def selectionSort(nums: list[int]) -> list[int]:
        n=len(nums)
        for i in range(n-1):
            mini = i
            for j in range(i+1, n):
                if nums[j]<nums[mini]:
                    mini=j
            if nums[mini]<nums[i]:
                nums[i],nums[mini]=nums[mini],nums[i]
        return nums
    
    def bubbleSort(nums: list[int]) -> list[int]:
        n=len(nums)
        didSwap=0
        for i in range(n-1,0,-1):
            for j in range(i):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
                    didSwap+=1
            if didSwap==0:
                break
        return nums
    
    def insertionSort(nums: list[int]) -> list[int]:
        n=len(nums)
        for i in range(n):
            for j in range(i,0,-1):
                if j>0 and nums[j-1]>nums[j]:
                    nums[j-1],nums[j]=nums[j],nums[j-1]
                else:
                    break
        return nums
    
arr = get_ints()
result = Solution.insertionSort(arr)
write_output(result)