import sys

def get_line():
    return sys.stdin.readline().strip()

def get_list_input():
    return list(map(int, get_line().split()))

def output(s):
    return sys.stdout.write(str(s)+"\n")

def solve(n):
    if n==2:
        return 2
    elif n==3:
        return 3
    else:
        return n%2

def cf():
    # n, k = get_list_input()
    # answer = solve(n, k)
    # output(answer)


    t = int(get_line())

    while t:
        people = int(get_line())
        answer = solve(people)
        output(answer)

        t-=1

if __name__ == "__main__":
    cf()