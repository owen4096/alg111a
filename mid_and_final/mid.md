### 期中project_0-1 knapsack

所謂背包問題分為兩種 普通背包問題以及0-1，背包問題，其中0-1背包為NP-complete problem

### 定義
有一個背包承重為w，每個物品的價值為Ｖ(i)，每個物品的重量為Ｗ(i)，for all i=1~n，看能取多少價值的物品</br>
普通背包又稱為Fractional Knapsack Problem，跟0-1背包的差別在於普通背包問題是可以取不到一個物品的，比如說0.8個 a + 2個b</br>
而0-1背包顧名思義 只有0 or 1 不取或是全拿</br>


### 以下為程式碼區段 由chatGPT產上

<pre><code>

def knapsack(n, C, w, v):
    # 初始化 dp 數組
    dp = [[0] * (C + 1) for _ in range(n + 1)]
 
    # 循環枚舉物品
    for i in range(1, n + 1):
        # 循環枚舉容量
        for j in range(1, C + 1):
            # 不放入物品
            dp[i][j] = dp[i - 1][j]
            # 放入物品
            if j >= w[i]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - w[i]] + v[i])
 
    return dp[n][C]
 
 
# 測試程序
if __name__ == '__main__':
    n = 4
    C = 5
    w = [0, 2, 1, 3, 2]
    v = [0, 12, 10, 20, 15]
    print(knapsack(n, C, w, v))

</code></pre>

以上為利用chatGPT生成的的0-1 Knapack ，概念是利用dp去做遞迴,遞迴去比較i-1 之最佳解以及拿了之後w-w(i)之最佳解兩者取大的</br>
相較於Fractional Knapsack Problem可以利用Greedy的方式,因為可以切割的關西,可以一步一步求出最佳解(local max = globol max)</br>
但0-1 Knapack 還得需要回頭看放入這個物品拿出那個物品結果會不會更好,所以cost time大幅度提升</br>
基本上程式碼算是可以完全看懂,但實在是沒辦法自己寫出來,能做到的只有把整個概念的presudo code寫下來而已</br>

<img src="https://github.com/owen4096/alg111a/blob/main/mid_and_final/01knap.jpg" width="500" height="400"  align=center /> 

以上為我自己嘗試寫出並trace的結果,算是一種自學筆記吧,概念上都是沒問題,就是程式寫不太出來就是了,在遞迴這方面還是得在加強</br>





### 參考資料
* [0-1 Knapsack wiki](https://zh.wikipedia.org/zh-hk/%E8%83%8C%E5%8C%85%E9%97%AE%E9%A2%98)
* [A lot of knapsack problem](https://web.ntnu.edu.tw/~algo/KnapsackProblem.html)

