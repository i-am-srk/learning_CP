import sys

inputs = list(map(int, sys.stdin.readline().strip().split()))

s, a, b, x = inputs

total_distance = 0

total_distance += ((x//(a+b))*(s*a)) + (((x%(a+b))*s) if (x%(a+b)) < a else (s*a))

print(total_distance)