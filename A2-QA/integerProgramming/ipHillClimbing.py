from msilib import sequence
from ipData import *
# 這是習題，請完成以下程式碼！
import random
import time
time1 = time.time()
ans = 0

def check(n):
    temp = 0
    k=0
    
  
    for i in range(len(coefs)):
        for j in range(len(coefs[i])):
            temp += coefs[i][j] * n[j]    
        if temp > maxs[i]:
            k -= 778844
        temp=0
    for l in range(len(n)):
        k += n[l] * cost_fn[l]    
    return k 

def tryip():
    counter = 0
    data = [0.0, 0.0, 0.0, 0.0, 0.0]
    h = 1
    while counter < 50000:

        counter+=1
        dx0 = random.randint(-h, h)
        dx1 = random.randint(-h, h)
        dx2 = random.randint(-h, h)
        dx3 = random.randint(-h, h)
        dx4 = random.randint(-h, h)
      

        data_temp = [data[0]+dx0, data[1]+dx1, data[2]+dx2, data[3]+dx3, data[4]+dx4]
      
        for i in range(len(data_temp)):
            if data_temp[i] < 0:
                data_temp[i] = 0
        
        if check(data) < check(data_temp):
            data = data_temp
    return data


t = tryip()
for i in range(len(t)):
    print(unknowns[i],"=", int(t[i]))
for i in range(len(t)):
    ans += t[i] * cost_fn[i]
time2 =time.time()    
print(ans,"花費了:",time2-time1,"秒")



