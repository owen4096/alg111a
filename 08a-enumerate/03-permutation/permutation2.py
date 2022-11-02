
dic=[5000]
count2=0

def cnk(n,k): # 主函數
	p = [] # p 代表已經排下去的，一開始還沒排，所以是空的
	y=1
	return permNext(n,k,p,y) # 呼叫 permNext 遞迴下去排出所有可能

def permNext(n,k,p,y): # 已經排好 p[0..i-1], 繼續排下去 [i...n-1]
	count=0
	global count2
	global dic
	i = len(p)
	if i == k:
		if not p in dic:
			dic[count2]=p
			count2=count2+1
			
			print(p)
		
		return	
		
	for x in range(y,n+1):
		permNext(n,k,p,y+1)
		if x not in p:
			for j in range(len(p)):
				if x > p[j]:
					count=count+1
			if count == len(p):
				p.append(x)    # 把 x 放進盤面
				permNext(n,k,p,y+1) # 繼續遞迴尋找下一個排列
				p.pop()       
		

						        
		
cnk(6,3) 

