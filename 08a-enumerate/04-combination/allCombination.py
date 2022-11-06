import random
import numpy as np
def Cnk(A, k): #A為要取的array 也就是cnk的n k則是取的數 為cnk之k
	chooses = []
	Cnkfuction(A, A[-1], k, chooses,k) #相比起用len(A) 我個人認為用A之最後一個數字比較淺顯 進到遞迴中也可以很清楚了解N-1是指從後面到前面

def Cnkfuction(A, n, k, chooses, k2): # 
	if len(chooses)==k2:
		print(chooses)
		return
	if n <= 0: return
	Cnkfuction(A,n-1,k,chooses,k2) # 先做不取在做取 因為遞迴後進先出 所以會先看到最小的數字組合 反之最大的則最後

	chooses.append(A[n-1])
	Cnkfuction(A,n-1,k-1,chooses,k2) # 取了後放入 記得要pop掉才能回到這一層 當下面都做完才能回收回去
	chooses.pop()

randomnum=random.randint(1,15)  # 看懂了老師的程式碼 但實在想不到哪裡可以改 於是改成cnk中的nk都隨機
arr = np.arange(1,randomnum+1,1)
take=random.randint(1,arr[-1])

print("這次是C",randomnum,"取",take)

Cnk(arr,take)
