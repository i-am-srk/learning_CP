import sys

def get_line():
    return sys.stdin.readline().strip()

def get_ints():
    return list(map(int, get_line().split()))

def write_output(s):
    sys.stdout.write(str(s)+'\n')

def twoSum(nums: list[int], target: int) -> list[int]:
    indices_to_numbers={}
    ans=[]
    for index, num in enumerate(nums):
        compliment=target-num
        if compliment in indices_to_numbers:
            ans.append(indices_to_numbers[compliment])
            ans.append(index)
            break
        indices_to_numbers[num]=index

    return ans

nums=get_ints()
target = int(get_line())
result = twoSum(nums, target)
write_output(result)