import sys
import bisect

def get_line():
    return sys.stdin.readline().strip()

def get_ints():
    return list(map(int, get_line().split()))

def write_output(s):
    sys.stdout.write(str(s)+'\n')

def isAnagram(s: str, t:str) -> bool:
    if len(s)!=len(t):
        return False
    
    s_freq = {}
    t_freq = {}

    for c in s:
        if c in s_freq:
            s_freq[c]+=1
        else:
            s_freq[c]=1

    for c in t:
        if c in t_freq:
            t_freq[c]+=1
        else:
            t_freq[c]=1

    for key, value in s_freq.items():
        if key not in t_freq or t_freq[key]!=value:
            return False
        
    return True


str_1 = get_line()
str_2 = get_line()
# nums=get_ints()
# k=int(get_line())
result = isAnagram(str_1, str_2)
write_output(result)