import sys

def get_line():
    return sys.stdin.readline().strip()

def get_list_input():
    return list(map(int, get_line().split()))

def output(s):
    return sys.stdout.write(str(s)+"\n")

def solve(n, k):
    if k>n:
        return -1
    
    found=False
    for d in range(32):
        low=n//(1<<d)
        high=(n+(1<<d)-1)//(1<<d)

        if low==k or high==k:
            found=True
            return d
        
        if high<k:
            break
    
    if not found:
        return -1

def cf():
    # n, k = get_list_input()
    # answer = solve(n, k)
    # output(answer)


    t = int(get_line())

    while t:
        n, k = get_list_input()
        answer = solve(n, k)
        output(answer)

        t-=1

if __name__ == "__main__":
    cf()