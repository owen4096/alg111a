# https://en.wikipedia.org/wiki/Context-sensitive_language
# https://cs.stackexchange.com/questions/135633/context-sensitive-grammar-for-the-language-anbncn-mid-n%E2%89%A51
'''
S→aSXY|abc
cX→Xc
bX→bb
cY→cc
'''
from random import random

def S():
    if random()<0.7:
        return f'{a}{S()}{X()}{Y()}' if random()<0.5 else 'abc'

# cX→Xc ??


