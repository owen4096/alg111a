def sqrtloop(n):
    low=1.0
    high=n
    mid=(low+high)/2.0
    while abs(mid*mid-n)>0.00001:
        mid=(low+high)/2.0        
        if mid*mid>n:
            high=mid
        elif mid*mid<n:
            low=mid
    return mid        
print(sqrtloop(3.0))    