
dic=[None]*50
count2=0

def cnk(n,k): # 主函數
	p = [] # p 代表已經排下去的，一開始還沒排，所以是空的
	y=1
	
	return permNext(n,k,p,y) # 呼叫 permNext 遞迴下去排出所有可能

def permNext(n,k,p,y): 
	count=0
	global count2
	global dic

	i = len(p)
	if i == k:
		if not p in dic:  #確認是否在字典裡 否則放入並印出 是則do nothing
			dic[count2]=p
			print(dic)
			count2=count2+1		
		return
				
	for x in range(y,n+1):  		 #因為組合沒有順序性 因此我的想法為只找由小到大 則為全部組合
		permNext(n,k,p,y+1) 		 #每個數字都可以選擇不放或放 此行為不放
		if x not in p:
			for j in range(len(p)):  #判斷x是否大於p中所有的數字 是則放入
				if x > p[j]:		 #判斷x是否大於p中所有的數字 是則放入
					count=count+1	 #判斷x是否大於p中所有的數字 是則放入
			if count == len(p):
				p.append(x)    
				permNext(n,k,p,y+1) 
				p.pop()       					        
		
cnk(6,3) 

