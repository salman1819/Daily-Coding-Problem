#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
PROBLEM NO.4 DATE: JUL 17 2019

STATEMENT: This problem was asked by Facebook.
Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.
For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make the array non-decreasing.
Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-decreasing array.

APPROACH: The approach that I took for this problem was simple and easy solution, the one which comes to the mind first -- remove each element and immediately check if the new array is same as the sorted new array. If so, then return True else, add
back that element which you removed and then continue the same process for the next element in the array.
'''


# In[9]:


def func(arr):
    if arr == sorted(arr):
        return True
    for i in range(len(arr)):
        tmp = arr[i]
        del arr[i]
        if arr == sorted(arr):
            return True
        else:
            arr.insert(i, tmp)
            print(arr); # line in fork
    return False

print(func([1,2,500,270,100,8900]))


# In[ ]:




