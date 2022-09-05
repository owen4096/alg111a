class Gate:
    def __init__(self, name, params):
        self.name = name
        self.params = params
    def normalForm(self):
        plist = []
        for param in self.params:
            if isinstance(param, Gate):
                plist.append(param.normalForm())
            else:
                plist.append("_")
        return f"{self.name}({','.join(plist)})"

def Not(a):
    return Gate("not", [a])

def Nand(a,b):
    return Gate("nand", [a,b])

def dumpGateLib(gateLib):
    for name, array in gateLib.items():
        print(name, ' ', array[0], end =" ")
        for g in array[1:]:
            print(g.normalForm(), end=" ")
        print()

def mapMin(goal, boolLib):
    pass

if __name__ == '__main__':
    a = "_"; b= "_"; c="_"; d="_"; e="_"; f="_"; g="_"; h="_"
    gateLib = {
    "NOT"    :[2, Not(a)],
    "NAND"   :[3, Nand(a,b)],
    "NAND3"  :[4, Nand(Not(Nand(a,b)),c)],
    "NAND4"  :[5, Nand(Nand(Not(Nand(a,b)),c),d),
                Nand(Not(Nand(a,b)),Not(Nand(c,d)))],
    "AOI21"  :[4, Not(Nand(Nand(a,b),Not(c)))],
    "AOI22"  :[5, Not(Nand(Nand(a,b),Nand(c,d)))]
    }
    dumpGateLib(gateLib)
    print('Nand(a,b)=', Nand(a,b).normalForm())
    goal = \
    Nand(
        Not(
            Nand(
                Not(
                    Nand(
                        Nand(Nand(a,b),
                             Not(c)
                            ),
                        Not(d)
                        )
                    ),
                Nand(
                    Not(Nand(e,f)),
                    g)
                )
            )
        ,h)
    print(goal.normalForm())
