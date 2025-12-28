import sys
import bisect

def get_line():
    return sys.stdin.readline().strip()

def get_ints():
    return list(map(int, get_line().split()))

def write_output(s):
    sys.stdout.write(str(s)+'\n')

def count_apartments(applicants: list, apartments: list, k: int) -> int:
    applicants.sort()
    apartments.sort()

    i,j,matches=0,0,0
    while i<len(applicants) and j<len(apartments):
        if abs(apartments[j]-applicants[i])<=k:
            matches+=1
            i+=1
            j+=1
        elif apartments[j]<applicants[i]-k:
            j+=1
        else:
            i+=1

    return matches




# str_1 = get_line()
# str_2 = get_line()
# k=int(get_line())
# nums=get_ints()
n, m, k = get_ints()
applicants = get_ints()
apartments = get_ints()
result = count_apartments(applicants, apartments, k)
write_output(result)