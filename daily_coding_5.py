'''
PROBLEM NO.5 DATE: JUN 1 2019
--Jan-19-2023

STATEMENT: This problem was asked by Microsoft.
Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element. Recall that the median of an even-numbered list is the average of the two middle numbers.
For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:
2
1.5
2
3.5
2
2
2

APPROACH: Sort the temporary list as you take a slice of the original list, element by element keep adding to the temporary list and then implement the definition of median. 
'''

def func(arr):
    for i in range(1, len(arr)+1):
        tmp_arr = sorted(arr[:i])
        zz = len(tmp_arr)
        if zz%2 != 0:
            yy = int((zz-1)/2)
            print(tmp_arr[yy])
        else:
            xx = int(zz/2)
            ly = (tmp_arr[xx] + tmp_arr[xx-1])/2
            if ly%int(ly) == 0.0:
                print(int(ly))
            else:
                print(ly)

func([2,1,5,7,2,0,5])