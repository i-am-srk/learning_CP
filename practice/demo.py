import sys
import bisect

def get_line():
    return sys.stdin.readline().strip()

def get_ints():
    return list(map(int, get_line().split()))

def write_output(s):
    sys.stdout.write(str(s)+'\n')

def floorSqrt(num: int) -> int:
    if num<2:
        return num
    
    l, r = 1, num//2
    ans=0
    while l<=r:
        mid = l+(r-l)//2
        square=mid*mid
        if square == num:
            return mid
        elif square<num:
            ans=mid
            l=mid+1
        else:
            r=mid-1

    return ans


# str_1 = get_line()
# str_2 = get_line()
# nums=get_ints()
k=int(get_line())
result = floorSqrt(k)
write_output(result)