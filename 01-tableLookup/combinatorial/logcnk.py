import math

#將數字先轉成log,因此相乘變成相加,加完再把他推回去原本的數字
def logFactorial(n):
    logsum=0
    for i in range(1,n+1):
        logsum += math.log(i)
    return logsum        

def factorial(n):
    logf=logFactorial(n)
    return int(round(math.exp(logf),1))


print(factorial(10))