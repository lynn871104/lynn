# Linked List
## Linked List優點
* 不連續的儲存在記憶體位置  
* 依使用多寡分配空間  
* 方便頻繁新增、刪除資料 
* 查詢(走訪所有node)  
* BlockChain的應用

## Linked List定義
* Listed list(連接串列)是一種常見的資料結構、其使用node(節點)來記錄、表示、儲存資料，並利用每個node中的Pointer指向下一個node，藉此將多個node串接起來，並以NULL來代表Linked list的終點。  
*　一個node中至少會包含data和pointer。　　
*　Ｐointer記錄下一個node的記憶體位置，因此可以在Lnked list中「移動」、「新增節點」、「刪除節點」「印出Linked list」等資料處理。  
## Array和Linked list的比較
**Array優點:**  
* random acces:只要利用index即可在O(1)時間對Array的資料作存取。  
* 較Linked list為節省記憶體空間:因為Linked list需要多一個pointer來下一node的記憶體位置  
      * 假設data是1byte，Pointer項目卻是4bytes，結構上多花了4倍的記憶體空間卻與真正需處理的資料無關。  
**Array缺點:**  
* 新增/刪除資料麻煩(所有資料須同時移動)  
* 花費O(N)的時間在搬動資料  
**Array適用時機:**
* 能夠快速存取資料。  
* 已知欲處理的資料數量、便能確認矩陣的大小。  
* 要求記憶體空間的使用越少越好。  
**Linked list優點:**  
* 新增/刪除資料較簡單，只要對O(1)個節點調整pointer，無須搬動其餘元素  
* Linked list的資料數量可以是動態的，不像Array會有resize的問題
**Linked list缺點**
* Linked list沒有index，若要找到特定node，需要從頭```(ListNode*first)```開始找起，搜尋的時間複雜度為O(N)  
* 需要額外的記憶體空間來儲存pointer  
**Linked list適用時機**  
* 無法預期資料數量時  
* 需要頻繁地新增/刪除資料時  
* 不需要快速查詢資料
