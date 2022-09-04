# from bmDelegate import *
from eda0 import *
from truthTable import *

table = [
#abco1A0CPfR
"00001000001",
"00101001111",
"01001000110",
"01111001011",
"10001100100",
"10111101000",
"11011100001",
"11111101101"
]

table = TruthTable(table, 3, ["a", "b", "c", "o", "one", "A", "zero", "C", "parity", "f", "Removable"])
rules = boolMinimize(table)
print(rules)
