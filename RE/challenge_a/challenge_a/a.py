from z3 import *

s = Solver()
a = [Int(f"a{i}") for i in range(4)]

for i in a:
    s.add(i >= 0, i < 9)

s.add(sum(a) == 18)
s.add(a[0] * a[1] == 24)
s.add(a[2] - a[3] == 2)
s.add(a[0] >= a[1])
s.add(a[0] > a[3])

if s.check() == sat:
    m = s.model()
    for x in a:
        print(m[x], end="")