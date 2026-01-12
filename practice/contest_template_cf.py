import sys

def get_line():
    return sys.stdin.readline().strip()

def get_list_input():
    return list(map(int, get_line().split()))

def output(s):
    return sys.stdout.write(str(s)+"\n")

def solve(n, p):
    if n<2:
        return 0
    
    d = [abs(p[i] - p[i+1]) for i in range(n-1)]
    m = n - 1
    
    left = [-1] * m
    right = [m] * m
    stack = []
    
    for i in range(m):
        while stack and d[stack[-1]] >= d[i]:
            stack.pop()
        if stack:
            left[i] = stack[-1]
        stack.append(i)
        
    stack = []
    for i in range(m-1, -1, -1):
        while stack and d[stack[-1]] > d[i]:
            stack.pop()
        if stack:
            right[i] = stack[-1]
        stack.append(i)

    freq = [0] * (n + 1)
    for i in range(m):
        count = (i - left[i]) * (right[i] - i)
        freq[d[i]] += count

    ans = [0] * (n + 1)
    current_sum = 0
    for k in range(n - 1, 0, -1):
        current_sum += freq[k]
        ans[k] = current_sum

    return " ".join(map(str, ans[1:n]))


def cf():
    # n, k = get_list_input()
    # answer = solve(n, k)
    # output(answer)


    t = int(get_line())

    while t:
        n = int(get_line())
        p = get_list_input()
        answer = solve(n, p)
        output(answer)

        t-=1

if __name__ == "__main__":
    cf()