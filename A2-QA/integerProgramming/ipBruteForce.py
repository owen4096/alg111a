#7a + 8b + 2c + 9d + 6e

#5a	+	7b	+	9c	+	2d	+	e      ≤250
#18a+	4b	–	9c	+	10d	+	12e	   ≤285
#4a	+	7b	+	3c	+	8d	+	5e	   ≤211
#5a	+	13b	+	16c	+	3d	– 7e       ≤315


# 這是習題，請完成以下程式碼！

#根據上述式子 可得知a最大為50 b最大為30 c最大為70 d最大為26 e最大為42
#因為c用71真的太久了 所以改用20就好
import time
time1 = time.time()
answer=0
a=0
b=0
c=0
d=0
e=0
for a_num in range (0,51):
    for b_num in range (0,31):
        for c_num in range (0,20):
            for d_num in range (0,27):
                for e_num in range (0,43):
                        if(5*a+7*b_num+9*c_num+2*d_num+e_num<=250):
                            if(18*a_num+4*b_num-9*c_num+10*d_num+12*e_num <= 285):
                                if(4*a_num+7*b_num+3*c_num+8*d_num+5*e_num <= 211):
                                    if(5*a_num+13*b_num+16*c_num+3*d_num-7*e_num <=315):
                                        temp=7*a_num+8*b_num+2*c_num+9*d_num+6*e_num
                                        if(temp>answer):
                                            answer=temp
                                            a=a_num
                                            b=b_num
                                            c=c_num
                                            d=d_num
                                            e=e_num
time2=  time.time()                                          
print(answer,a,b,c,d,e,"花費了:",time2-time1,"秒")                    
                    
                                            
                                        


