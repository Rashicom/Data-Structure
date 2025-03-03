"""
2161. Partitio
n Array According to Given Pivot
You are given a 0-indexed integer array nums and an integer pivot. Rearrange nums such that the following conditions are satisfied:

Every element less than pivot appears before every element greater than pivot.
Every element equal to pivot appears in between the elements less than and greater than pivot.
The relative order of the elements less than pivot and the elements greater than pivot is maintained.
More formally, consider every pi, pj where pi is the new position of the ith element and pj is the new position of the jth element. If i < j and both elements are smaller (or larger) than pivot, then pi < pj.
Return nums after the rearrangement.

Input: nums = [9,12,5,10,14,3,10], pivot = 10
Output: [9,5,3,10,10,12,14]
"""

# time complexity o(n)
# space complexity o(2n)
def pivot_array1(nums, pivot):
    left = []
    right = []
    pivot_count = 0
    for num in nums:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            pivot_count += 1
    left.extend([pivot]*pivot_count)
    left.extend(right)
    return left

try:
    assert pivot_array1([9,12,5,10,14,3,10],10)
    print("TEST PASS")
except AssertionError:
    print("TEST FILURE")


# space complexity o(n)
# time complextiy o(n)
def pivot_array2(nums, pivot):
    pass