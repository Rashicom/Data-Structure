"""
Question:
    2570. Merge Two 2D Arrays by Summing Values

merge two lists , the nums[i][0] is the id and the nums[i][1] is the value
both list is accending order by id.
merge two list into one by accending order by id. add both values if same id present from list2 and list2

Input: nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]
Output: [[1,6],[2,3],[3,2],[4,6]]
"""

def merge_two_lists(nums1, nums2):
    num1_len, num2_len, i, j = len(nums1)-1, len(nums2)-1, 0, 0
    result = []

    while i <= num1_len and j <= num2_len:
        if nums1[i][0] == nums2[j][0]:
            result.append([nums2[j][0], nums1[i][1]+nums2[j][1]])
            i += 1
            j += 1
        elif nums1[i][0] < nums2[j][0]:
            result.append(nums1[i])
            i += 1
        elif nums2[j][0] < nums1[i][0]:
            result.append(nums2[j])
            j += 1
        
    if i <= num1_len:
        result.extend(nums1[i:])
    if j <= num2_len:
        result.extend(nums2[j:])
    return result


try:
    assert merge_two_lists([[1,2],[2,3],[4,5]], [[1,4],[3,2],[4,1]]) == [[1,6],[2,3],[3,2],[4,6]]
    print("TEST 1 PASS")
    assert merge_two_lists([[2,4],[3,6],[5,5]], [[1,3],[4,3]]) == [[1,3],[2,4],[3,6],[4,3],[5,5]]
    print("TEST 2 PASS")
except AssertionError:
    print("Test filure")




"""
Merge two normal sorted list
"""

# TODO
def merge_two_normal_list(nums1, nums2):
    pass


"""
Merge two unsorted list
"""

def merge_unsorted_list(nums1, nums2):
    pass