import sys

def get_line():
    return sys.stdin.readline().strip()

def get_ints():
    return list(map(int, get_line().split()))

def write_output(s):
    sys.stdout.write(str(s)+'\n')

def unionArray(nums1: list[int], nums2: list[int]) -> list[int]:
    i, j = 0, 0
    union_array = []

    while i<len(nums1) and j<len(nums2):
        if nums1[i]<nums2[j]:
            num=nums1[i]
            i+=1
        elif nums1[i]>nums2[j]:
            num=nums2[j]
            j+=1
        else:
            num=nums1[i]
            i+=1
            j+=1

        if len(union_array)>0 and union_array[-1]==num:
            continue
        else:
            union_array.append(num)

    while i<len(nums1):
        num=nums1[i]
        i+=1
        if len(union_array)>0 and union_array[-1]==num:
            continue
        else:
            union_array.append(num)

    while j<len(nums2):
        num=nums2[j]
        j+=1
        if len(union_array)>0 and union_array[-1]==num:
            continue
        else:
            union_array.append(num)

    return union_array

nums1=get_ints()
nums2=get_ints()
result = unionArray(nums1, nums2)
write_output(result)