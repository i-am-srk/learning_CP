import sys

def get_line():
    return sys.stdin.readline().strip()

def get_list_input():
    return list(map(int, get_line().split()))

def output(s):
    return sys.stdout.write(str(s)+"\n")

def solve(s, k, m):
    num_flips = m//k
    time_left = m%k

    if num_flips==0:
        sand_left=s
    elif num_flips%2==1:
        sand_left=min(s,k)
    else:
        sand_left=s

    rem_sand = max(0, sand_left - time_left)
    return rem_sand

def cf():
    # n, k = get_list_input()
    # answer = solve(n, k)
    # output(answer)


    t = int(get_line())

    while t:
        s, k, m = get_list_input()
        answer = solve(s, k, m)
        output(answer)

        t-=1

if __name__ == "__main__":
    cf()