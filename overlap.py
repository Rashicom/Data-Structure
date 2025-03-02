"""
Given a list of time intervals (start, end) Group the overlapping intervals and return an array of arrays.
bundle overlaping sets

 
Example 1
 
Input: [(1, 3), (2, 5), (8, 10), (9, 11), (15, 21)]
"""

def find_overlapping_pairs(intervals):
    lenn = len(intervals)-1
    result = []
    temp_list = []
    for interval in intervals:
        if len(temp_list) == 0:
            temp_list.append(interval)
        elif temp_list[-1][1] > interval[0]:
            temp_list.append(interval)
        else:
            result.append(temp_list)
            temp_list = [interval]
    
    result.append(temp_list)
    return result
        

try:
    assert find_overlapping_pairs([(1, 3), (2, 5), (8, 10), (9, 11), (15, 21)]) == [[(1, 3), (2, 5)],[(8, 10), (9, 11)],[(15, 21)]]
    print("TEST PASS")
except AssertionError:
    print("Test Filure")



"""
same problem , but unsorted intervals
"""

