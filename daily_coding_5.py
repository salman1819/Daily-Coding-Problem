#!/usr/bin/env python
# coding: utf-8

# In[39]:


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


# In[40]:


func([2,1,5,7,2,0,5])


# In[ ]:




