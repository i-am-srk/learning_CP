import sys

def get_line():
    return sys.stdin.readline().strip()

def get_list_input():
    return list(map(int, get_line().split()))

def output(s):
    return sys.stdout.write(str(s)+"\n")

def solve(n, k):
    solved = 0
    total_time = 240
    available_time = total_time-k
    for i in range(1, n+1):
        available_time -= 5*i
        if available_time >= 0:
            solved+=1

    return solved

def cf():
    n, k = get_list_input()
    answer = solve(n, k)
    output(answer)


    # t = int(get_line())

    # while t:
    #     sticks = get_list_input()
    #     answer = "YES" if check_square(sticks) else "NO"
    #     output(answer)

    #     t-=1

if __name__ == "__main__":
    cf()