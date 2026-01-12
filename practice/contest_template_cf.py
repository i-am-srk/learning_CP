import sys

def get_line():
    return sys.stdin.readline().strip()

def get_list_input():
    return list(map(int, get_line().split()))

def output(s):
    return sys.stdout.write(str(s)+"\n")

MAX_D=32
C= [[0]*MAX_D for _ in range (MAX_D)]
for i in range (MAX_D):
    C[i][0]=1
    for j in range (1,i+1):
        C[i][j]=C[i-1][j-1]+C[i-1][j]

def solve(n, k):
    d=n.bit_length()-1
    ans=0

    if d+1>k:
        ans+=1

    for p in range(d):
        target_c= k-p

        for c in range(max(0, target_c), p+1):
            ans+=C[p][c]

    return ans

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