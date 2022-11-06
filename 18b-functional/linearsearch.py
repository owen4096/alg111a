def linearserach(d,x):
    n=len(d)
    for i in range(n):
        if d[i]==x:
            print("在第",i,"個")
            return
    print("沒找到欸")        
    

a=[1,3,7,13,19,20]
linearserach(a,20)