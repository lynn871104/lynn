# Merge sort與Heap sort

## Merge sort與Heap sort比較
### Merge sort
高效率、穩定  
分為"遞迴"與"迴圈"  
->皆須用到額外空間
### Heap sort
分為插入與刪除方法  
刪除又分為max heap與min heap  
/  
從時間複雜度上來看，兩者皆是nlog(n)，但在空間的使用上，heap sort比較佔上風(不用用到額外空間)，  
當數量越多，heap sort較吃香。而merge sort是在穩定度勝出。  

### 流程圖

![流程圖](https://github.com/lynn871104/lynn/blob/master/week5/mergesort%E6%B5%81%E7%A8%8B%E5%9C%96.jpg "流程圖")  

![流程圖](https://github.com/lynn871104/lynn/blob/master/week5/heapsort%E6%B5%81%E7%A8%8B%E5%9C%96.jpg"流程圖")
