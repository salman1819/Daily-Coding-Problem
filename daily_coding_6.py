'''
This problem was asked by Facebook.

Given an array of integers in which two elements appear exactly once and all other elements appear exactly twice, find the two elements that appear only once.

For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8. The order does not matter.

Follow-up: Can you do this in linear time and constant space?

'''

def func_only_once(lst):  
                                                    # implemented with linear time complexity O(n) and constant space complexity
    a = b = count = flag = 0                        # variables for work. They do not count for space complexity, unlike lists
    for i in range(len(lst)):                       # avoiding the logic to check if the list is empty. Assumption made here is that the list / array is not empty
        count=lst.count(lst[i])
        if count!=2 and flag == 0:
            a = lst[i]
            flag = 1
        elif count!=2 and flag == 1:
            b = lst[i]
            return a,b
        else:
            count = 0
    return -1                     # in case if there are no unique values in the given array

print(func_only_once([2, 4, 6, 8, 10, 2, 6, 10]))
''' checking for git commit'''

