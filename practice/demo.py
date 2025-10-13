import sys

def get_line():
    return sys.stdin.readline().strip()

def get_ints():
    return list(map(int, get_line().split()))

def write_output(s):
    sys.stdout.write(str(s)+'\n')

def longestConsequetive(nums: list[int]):
    if not nums:
        return 0
    
    nums_set = set(nums)
    longest_sequence = 0

    for num in nums:
        if (num-1) not in nums_set:
            current_sequence=1
            current_num = num
            while (current_num+1) in nums_set:
                current_sequence+=1
                current_num+=1
            longest_sequence = max(longest_sequence, current_sequence)

    return longest_sequence


nums=get_ints()
result = longestConsequetive(nums)
write_output(result)