import random
import numpy as np
def Cnk(A, k): # 從 A 陣列中取出 m 個的所有可能性
	chooses = []
	Cnkfuction(A, len(A), k, chooses,k)

def Cnkfuction(A, n, k, chooses, k2): # 從 A[0..n] 中選取 k 個補進 chooses，如果滿 m 個就印出
	if len(chooses)==k2:
		print(chooses)
		return
	if n <= 0: return
	Cnkfuction(A,n-1,k,chooses,k2) # C(n-1,k)

	chooses.append(A[n-1])
	Cnkfuction(A,n-1,k-1,chooses,k2) # C(n-1,k-1)
	chooses.pop()

randomnum=random.randint(1,15)
arr = np.arange(1,randomnum+1,1)
take=random.randint(1,arr[-1])

print("這次是C",randomnum,"取",take)

Cnk(arr,take)
