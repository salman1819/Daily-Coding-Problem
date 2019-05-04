'''
PROBLEM NO.2 DATE: MAY 1 2019

STATEMENT: This problem was asked by Uber.
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?

APPROACH: I knew that this could be easily done without thinking much by two for loops, but that is not at all an optimal solution. The next approach I took was
if i is the index of interest then answer is product of arr[0:i] * product of arr[i+1:] is the new value that should be replaced at index i.
After looking at follow-up hint, I realized that this could have been done by division (// ---> quotient way). Anyways, the approach I thought of initially
was a good one and I looked online for quicker ways to calculate product(arr[0:i]) and product(arr[i+1:]). I stumbled upon reduce. But I was not totally in favour of importing any packages.
Then, I created a helper function that gives you the product of numbers in a list. This approach is efficient and makes overall code quite readable.
'''
# from functools import reduce
arr = [1,-2,3,9,0,-3]
def except_product(arr):
    ca = []
    for i in range(len(arr)):
        if i == 0:
            # ar = reduce(lambda x,y: x*y, arr[1:]) #no need to put list before reduce as reduce spits out a single number, which is product of numbers in that list
            ar = prodd_c(arr[1:])
            ca.append(ar)
            print('ar: ', ar) # check if it is correct
        elif i == (len(arr)-1):
            #az = reduce(lambda x,y: x*y, arr[0:i])
            az = prodd_c(arr[0:i])
            print('az: ', az)                                # do this without reduce but use this logic only
            ca.append(az)
        else:
            # product1 = reduce((lambda x, y: x * y), arr[0:i])
            product1 = prodd_c(arr[0:i])
            # product2 = reduce((lambda x, y: x * y), arr[i+1:])
            product2 = prodd_c(arr[i+1:])
            ax = product1*product2
            print('ax: ', ax) 
            ca.append(ax)
    return ca

def prodd_c(arr):
    prodf=1
    for i in arr:
        prodf*=i
    return prodf

print(except_product(arr))