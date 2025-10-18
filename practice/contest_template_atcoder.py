import sys
from collections import defaultdict

n, k = list(map(int, sys.stdin.readline().strip().split()))

s = sys.stdin.readline().strip()

# generate and count all substrings
counts: dict[str, int] = defaultdict(int)
for i in range(n-k+1):
    substring = s[i:i+k]
    counts[substring]+=1

# find max occurence
max_occurence: int = 0
if counts:
    max_occurence = max(counts.values())

# filter and output
max_strings: list[str] = []
for sub, count in counts.items():
    if count == max_occurence:
        max_strings.append(sub)

max_strings.sort()

sys.stdout.write(str(max_occurence)+'\n')
sys.stdout.write(' '.join(max_strings)+'\n')