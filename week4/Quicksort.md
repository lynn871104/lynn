# 演算法第一次作業:Quick sort  
## 想法:  
創三個list  
放 大於基準點、等於基準點、小於基準點  
使用append加入  
用for迴圈包住  
**要記得幫迴圈設停止條件!!!**
```
array = [5,7,3,-3,4,6]

def quick_sort(array):
    small = []
    center = []
    big = []
    # 創建三個list
    if len(array) > 1: #原本沒設停止條件
        mark = array[0] #抓第一個當基準
        for a in array:
            if a < mark:
                small.append(a) 
            elif a == mark:
                center.append(a)
            elif a > mark:
                big.append(a)
        return sort(small)+sort(center)+sort(big) #排好再合併起來 
    else: 
        return array #最後返回array
quick_sort(array)
```
儲存空間會太多、時間要很久->參考網路上class的用法
```
#10/15第一次思考但還是不太懂
#arr = [4,2,-7,3,2]
# class Quicksort:
#     def __init__(self,array, start, end):
#        self.ar = array
#        self.quick_sort(array,start, end)
#        print (array)
#    def quick_sort(self, array, start, end):
#        if start < end:
#            mark = quick_sort(array,start,end)
#            self.quick_sort(array,start,mark-1)
#            self.quick_sort(array,mark+1,end)
            
#    def partition(self,array,start,end):
#        x = array[end]
#        i = start-1
#        for a in range(start,end+1,1):
#            print (array)
#            if array[a] <= x:
#                i = i+1
#                if i < a:
#                    z = array[i]
#                    array[i] = array[a] #自己能想到這裡的交換
#                    array[j] = z
#        return i
```
