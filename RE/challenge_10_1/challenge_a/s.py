from z3 import *

s = Solver()

a, b, c, d = Ints('a b c d')

s.add(a >= 0, a < 9)
s.add(b >= 0, b < 9)
s.add(c >= 0, c < 9)
s.add(d >= 0, d < 9)
s.add(a+b+c+d == 18)
s.add(a*b == 24)
s.add(c-d == 2)
s.add(a >= b)
s.add(a > d)

if s.check() == sat:
    m = s.model()
    print(m)