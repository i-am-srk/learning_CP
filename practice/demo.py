import sys
import bisect
from collections import defaultdict

def get_line():
    return sys.stdin.readline().strip()

def get_ints():
    return list(map(int, get_line().split()))

def write_output(s):
    sys.stdout.write(str(s)+'\n')

def safe_pow_check(base: int, exp: int, limit: int) -> int:
    if base==1: return 0 if limit<1 else -1
    result = 1
    for _ in range(exp):
        result *= base
        if result > limit:
            return 1
    return 0 if result == limit else -1

def nth_root(n: int, m: int) -> int:
    if m==0: return 0
    if m==1: return 1
    if n==1: return m
    
    lo, hi=1, m
    if n>=60 and m<=10**18: hi=2
    elif n>=2: hi=int(m**(1/n))+2

    ans = -1
    while lo<=hi:
        mid=lo+(hi-lo)//2
        val=pow(mid,n)
        
        if val==m:
            return mid
        elif val<m:
            lo=mid+1
        else:
            hi=mid-1

    return ans

# str_1 = get_line()
# str_2 = get_line()
# nums=get_ints()
# k=int(get_line())
n=int(get_line())
m=int(get_line())
result = nth_root(n,m)
write_output(result)