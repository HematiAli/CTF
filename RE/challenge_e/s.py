from z3 import *
s = Solver()
data = bytes.fromhex("7c153a474b6a2d3f7d3f7328703e6c2d243a083e2e773c45547748667c1511333f4f745e")
flag = [Int("flag_"+str(i)) for i in range(len(data) - 15)]
key = [Int("key_" + str(i)) for i in range(13)]
pipe = Int("pipe")

s.add(pipe == ord("|"))

for i, c in enumerate("TWCTF"):
    s.add(flag[i] == ord(c))

for f in flag:
    s.add(f >= 0, f < 128)
for k in key:
    s.add(k >= 0, k < 128)

message = flag + [pipe] + key

for i in range(1, len(data)):
    idx = i - 1
    byte = data[i]
    s.add((message[idx] + key[idx % 13] + data[idx]) % 128 == byte)

if s.check() == sat:
    m = s.model()
    print(bytes([m[x].as_long() for x in message]))


