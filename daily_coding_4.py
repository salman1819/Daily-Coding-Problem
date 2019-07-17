#!/usr/bin/env python
# coding: utf-8

# In[1]:


def func(arr):
  for i in range(len(arr)):
    tmp = arr[i]
    del arr[i]
    if arr == sorted(arr):
      return True
    else:
      arr.insert(i, tmp)
      continue
  return False

print(func([10,5,1]))


# In[ ]:




