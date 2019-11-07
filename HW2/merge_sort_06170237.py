#!/usr/bin/env python
# coding: utf-8

# In[71]:


array = [8,4,5,7,3,0,1,2,3]
class solution():
    def merge_sort(array):
        if len(array) < 1:
            return array #跟別人討論發現要這個條件才不會沒完沒了
        else:
            N = int(len(array))
            A1 = array[0:int(N/2)]
            A2 = array[int(N/2):]
            newA1 = merge_sort(A1)
            newA2 = merge_sort(A2)
        return sort(newA1,newA2)
    def sort(A1,A2):
        if A1[0] < A2[0]:
            return [A1[0]]
            return sort(A1[1:],A2)
        else:
            return [A2[0]]
            return sort(A1,A2[1:])
print(merge_sort(array))

