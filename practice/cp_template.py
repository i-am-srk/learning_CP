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
    for i in range(n-1,0,-1):
        for j in range(0,i):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return nums

# arr = get_ints()
# write_output(bubbleSort(arr))