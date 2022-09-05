# 參考 -- https://courses.cs.washington.edu/courses/cse467/03wi/FPGA.pdf
# FPGA = CLBs + routes
# CLB = LUT*2 + FullAdder + Flip-Flop
# 於是只要指定 route + 每個 CLB 的 LUT 內容，就能完成 FPGA 的燒錄。
# Clock 呢? 就用 一次 clock() 函數呼叫當成一個 Clock 吧！
class FPGA:
    def __init__(self, nrow, ncol, nLutIn):
        self.blocks = []
        for _ in range(nrow):
            row = []
            for _ in range(ncol):
                row.append(LogicBlock(nLutIn))
            self.blocks.append(row)
        self.route = [[[0]*nLutIn for _ in range(ncol)] for _ in range(nrow)]

and3   = [0,0,0,0,0,0,0,1]
or3    = [0,1,1,1,1,1,1,1]
xor3   = [0,1,1,0,1,0,0,1]
carry3 = [0,0,0,1,0,1,1,1]
mux2-1(s,a,b) = [0,0,1,1,0,1,0,1] # mux(s, a, b)

def idx3(a,b,c):
    return a<<2+b<<1+c

class CLB3:
    def __init__(self, n): # clk, out, cin, cout, row, add
        self.lut1 = [-1]*8
        self.lut2 = [-1]*8
        self.reg  = -1

    def run(i,cin,add,write,regOut):
        a = self.lut1[i]
        b = self.lut2[i]
        i = idx3(cin, a, b)
        sum = xor3[i]
        cout = carry3[i]
        regIn = 0 if add==0 else sum  # op:'0:a 1:add'
        if write: self.reg = regIn
        return {'cout':cout, 'out':reg if regOut else regIn }



'''
class LUT:
    def __init__(self, outs):
        self.outs = outs
    def lookup(i):
        return self.outs[i]

class RAM: # 在此 FPGA不包含RAM 的功能，所以外加一個 RAM 才能形成 computer
'''
