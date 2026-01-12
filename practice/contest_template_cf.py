import sys

def get_line():
    return sys.stdin.readline().strip()

def get_list_input():
    return list(map(int, get_line().split()))

def output(s):
    return sys.stdout.write(str(s)+"\n")

TABLE = [[0] * 8 for _ in range(8)]
for m1 in range(8):
    for m2 in range(8):
        res = 0
        for i in range(3):
            if (m1 >> i) & 1:
                for j in range(3):
                    if (m2 >> j) & 1:
                        res |= (1 << ((i + j) % 3))
        TABLE[m1][m2] = res

def solve(n, adj):
    parent = [0] * (n + 1)
    order = []
    has_child = [False] * (n + 1)
    visited = [False] * (n + 1)

    stack = [1]
    visited[1] = True
    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                has_child[u] = True
                stack.append(v)

    curr_sum = [1] * (n + 1)

    ans = ""
    for u in reversed(order):
        if not has_child[u]:
            dp_u = 2
        else:
            dp_u = 2 | curr_sum[u]
        
        if u == 1:
            if dp_u & 1:
                ans = "YES"
            else:
                ans = "NO"
        else:
            p = parent[u]
            curr_sum[p] = TABLE[curr_sum[p]][dp_u]

    return ans

def cf():
    # n, k = get_list_input()
    # answer = solve(n, k)
    # output(answer)


    t = int(get_line())

    while t:
        n = int(get_line())

        adj = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            u, v = get_list_input()
            adj[u].append(v)
            adj[v].append(u)

        answer = solve(n, adj)
        output(answer)

        t-=1

if __name__ == "__main__":
    cf()