'''
PROBLEM NO.4 DATE: MAY 03 2019

STATEMENT: This problem was asked by Stripe.
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
You can modify the input array in-place.

APPROACH: It is simple. Find min and max such that min is the smallest positive integer. Now within a range from min to max check if each element in this range
is in the original arr. If not then return the missing element. It will be the smallest positive integer that is missing. If all elements from the min to max range are found in arr, then, 
you should look at min and max. If min is 1 or 0 then return maxx+1 as the smallest possible integer that is missing from the original (given) arr. If the min is neither 1 nor 0, then, 
return min-1 as the smallest element that is missing from the original (given) array.
Also, you didn't think of sorting the array. That was given as the hint. Think about it once.
'''

arr = [-2,-3,0,2,4,1,5,-6]
def small_pos(arr): # You are doing for unsorted array. Think about sorting the array once and see if any change in time complexity. 
    minn=1 
    maxx=1   
    for i in range(len(arr)):
        if arr[i] >= 0 and arr[i] < minn:
            minn = arr[i]
        elif arr[i] >= 0 and arr[i] > maxx:
            maxx = arr[i]
    print('maxx: ', maxx)
    print('minn: ', minn)
    '''
        Approach No.1. For Approach No.2, Try it: Don't use 'not in' operator (Python). Use a helper function instead just for the not in operator. Find an alternative and avoid O(n^2) time complexity due to nested for loops.
        But it is complex and doesn't help us much. 
    '''
    for i in range(minn, maxx+1):
        if i not in arr:
            return i

    if minn==1 or minn==0:
        return maxx+1
    return minn-1

print(small_pos(arr))
    