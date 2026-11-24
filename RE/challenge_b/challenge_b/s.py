from z3 import *

s = Solver()
a,b,c,d,e,f,g, h = BitVecs('a b c d e f g h' , 8)

s.add(a ^ b == 0x69)
s.add((b ^ c) == 0x6c)

s.add((c ^ d) == 0x0d)
s.add((d ^ e) == 0x3d)
s.add((e ^ f) == 0x0c)
s.add((f ^ g) == 0x08)
s.add((g ^ h) == 0x18)
s.add((a & h) == 0x52)
s.add((c | f) == 0x7f)

s.add(a >= 30, a <= 126)
s.add(b >= 30, b <= 126)
s.add(c >= 30, c <= 126)
s.add(d >= 30, d <= 126)
s.add(e >= 30, e <= 126)
s.add(f >= 30, f <= 126)
s.add(g >= 30, g <= 126)
s.add(h >= 30, h <= 126)

if s.check() == sat:
    m = s.model()
    print(m)