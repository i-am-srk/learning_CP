import sys

def get_line():
    return sys.stdin.readline().strip()

def get_list_input():
    return list(map(int, get_line().split()))

def output(s):
    return sys.stdout.write(str(s)+"\n")

def check_square(nums: list[int]) -> bool:
    side_length = nums[0]
    is_valid = True
    for num in nums:
        if num != side_length:
            is_valid = False
            break

    return is_valid

def solve():
    t = int(get_line())

    while t:
        sticks = get_list_input()
        answer = "YES" if check_square(sticks) else "NO"
        output(answer)

        t-=1

if __name__ == "__main__":
    solve()