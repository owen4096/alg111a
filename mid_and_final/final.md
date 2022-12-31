### 期末project_0-1 subset sum problem



### 定義
所謂subset sum problem就是給定一個集合S及一個輸入k，檢查是否有一個子集合屬於S且每個元素的加總=k</br>
時間複雜度為Ｏ（2^n）</br>
舉例如下:</br>
{3, 34, 4, 12, 5, 2}, sum = 9  4+5=9 TRUE</br>
{3, 34, 4, 12, 5, 2}，sum = 30 FALSE</br>


### 以下為程式碼區段 由chatGPT產生

<pre><code>

def subset_sum(numbers: List[int], target: int) -> bool:

    # 確認input是否為0 因為空集合視為0
    if target == 0:
        return True

    # 如果list為空或是target< 0，return False
    if not numbers or target < 0:
        return False

    # 拿出最後一個數字 因為是python所以可以直接用-1
    last_number = numbers[-1]
    # 用前n-1個
    without_last = subset_sum(numbers[:-1], target)
    # 用所有
    all= subset_sum(numbers[:-1], target - last_number)

    return without_last or all


</code></pre>

以上為利用chatGPT生成的的subset sum problem ，概念跟期中的0-1 knapsack problem一樣，利用dp去做遞迴，嘗試以下兩種情況</br>
１：不利用最尾端之數字，用前ｎ－１個數字完成</br>
２：利用最尾端之數字，用全部數字完成，其中ｎ為｜Ｓ｜</br>
以上兩個只要有一個做得到　就會return True，否則則為False</br>
dp的好處就是可以一直利用前一次的最優解，去查看本次加入後的變化，而且相較於greedy，dp是可以回頭的演算法，可以做修正</br>

基本上程式碼算是可以完全看懂，基本上自己寫出來也沒有問題，但實在沒什麼地方好改，於是直接傳了</br>







### 參考資料
* [subset sum problem wiki](https://zh.m.wikipedia.org/zh-hant/%E5%AD%90%E9%9B%86%E5%92%8C%E5%95%8F%E9%A1%8C)
* [Subset Sum Problem](https://ithelp.ithome.com.tw/articles/10240370)
