import sys
sys.set_int_max_str_digits(1000000000)

def get_line() -> str:
    return sys.stdin.readline().strip()

def get_ints() -> list[int]:
    return list(map(int, get_line().split()))

def write_output(s: str):
    sys.stdout.write(str(s)+'\n')


def findGCD(a: int, b: int) -> int:
    """
    find gcd
    """
    if b==0:
        return a
    return findGCD(b, a%b)

# a, b = get_ints()
# write_output(findGCD(a, b))

def isPrime(x: int) -> bool:
    """
    primarility test of x
    """
    d = 2
    while(d*d <= x):
        if x%d == 0:
            return False
        d += 1
    return x >= 2

# result_Prime = isPrime(int(get_line()))
# write_output(result_Prime)

def binpow(a: int, n: int) -> int:
    """
    compute binary exponentiation
    """
    res = 1
    while n>0:
        if n&1:
            res = res*a
        a = a*a
        n >>= 1
    return res

# a, n = get_ints()
# write_output(binpow(a, n))

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

# arr = get_ints()
# write_output(selectionSort(arr))

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

# arr = get_ints()
# write_output(bubbleSort(arr))

def insertionSort(nums: list[int]) -> list[int]:
    n=len(nums)
    for i in range(n):
        for j in range(i,0,-1):
            if j>0 and nums[j-1]>nums[j]:
                nums[j-1],nums[j]=nums[j],nums[j-1]
            else:
                break
    return nums

# arr = get_ints()
# write_output(insertionSort(arr))

def merge(nums,low,mid,high):
    temp=[]
    left,right=low,mid+1

    while left<=mid and right<=high:
        if nums[left]<=nums[right]:
            temp.append(nums[left])
            left+=1
        else:
            temp.append(nums[right])
            right+=1
    
    while left<=mid:
        temp.append(nums[left])
        left+=1

    while right<=high:
        temp.append(nums[right])
        right+=1

    for i in range(low,high+1):
        nums[i]=temp[i-low]

def mergeSort(nums,low,high):
    if low>=high:
        return
    mid=(low+high)//2
    mergeSort(nums,low,mid)
    mergeSort(nums,mid+1,high)
    merge(nums,low,mid,high)
    return nums

    
# arr = get_ints()
# result = mergeSort(arr,0,len(arr)-1)
# write_output(result)

def recursive_bubble_sort(nums: list[int], n: int):
    if n==0:
        return
    
    didSwap=0

    for i in range(n):
        if nums[i]>nums[i+1]:
            nums[i],nums[i+1]=nums[i+1],nums[i]
            didSwap+=1
    
    if didSwap==0:
        return
    
    return recursive_bubble_sort(nums,n-1)

# nums=get_ints()
# recursive_bubble_sort(nums,len(nums)-1)
# write_output(nums)

def recursive_insertion_sort(nums: list[int], n: int):
    if n==len(nums):
        return
    
    for i in range(n,0,-1):
        if i>0 and nums[i-1]>nums[i]:
            nums[i-1],nums[i]=nums[i],nums[i-1]
    
    return recursive_insertion_sort(nums,n+1)

# nums=get_ints()
# recursive_insertion_sort(nums,0)
# write_output(nums)

def partition(nums: list[int], low:int, high:int):
    pivot=nums[low]
    i,j=low,high
    while i<j:
        while nums[i]<=pivot and i<high:
            i+=1

        while nums[j]>pivot and j>low:
            j-=1
    
        if i<j:
            nums[i],nums[j]=nums[j],nums[i]

    nums[low],nums[j]=nums[j],nums[low]
    return j

def quickSort(nums: list[int], low:int, high: int):
    if low>=high:
        return
    partitionIndex=partition(nums,low,high)
    quickSort(nums,low,partitionIndex-1)
    quickSort(nums,partitionIndex+1,high) 

# nums=get_ints()
# quickSort(nums,0,len(nums)-1)
# write_output(nums) 

def bSearch(nums: list[int], target: int) -> int:
    n=len(nums)
    low,high=0,n-1
    idx=-1

    while low<=high:
        mid=low+(high-low)//2
        if nums[mid]==target:
            idx=mid
            break
        elif nums[mid]>target:
            high=mid-1
        else:
            low=mid+1

    return idx

# nums=get_ints()
# k=int(get_line())
# index=bSearch(nums,k)
# write_output(index)

def iterativeBS(nums: list[int], target: int) -> int:
    n=len(nums)
    x=0
    b=n//2
    while b>=1:
        while (x+b)<n and nums[x+b]<=target:
            x+=b
        b//=2
    
    if nums[x]==target:
        return x
    
    return -1


# nums=get_ints()
# target = int(get_line())
# result = iterativeBS(nums, target)
# write_output(result)