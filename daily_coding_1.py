'''
PROBLEM NO.1 DATE: APR 30 2019

STATEMENT: This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass? // This means that you have to pass through the array just once. Hence Time & Space complexity is O(n). 

APPROACH: Calculate the difference between target and elements in the list. Check if this difference is in list. Time and Space complexity is O(n), as
you only have to traverse through the list just once.
'''

arr = [1,2,-10,58,20,43]
k = 57
def sum_to_target(arr, k):           # arr is list of all int assume (4*n bytes) k is also int and 4 bytes (assume)
    for i in arr:                    # i is int assume here so it's 4 bytes (assume)
        if k-i in arr:
            # return (i, k-i)        # Total space required here for this program is: 4n+4+4? So, the space complexity is 'linear'
            return True
        return False
print(sum_to_target(arr, k))

