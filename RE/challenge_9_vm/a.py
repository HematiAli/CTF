program = open("program", "rb").read()

# ins = [(program[i:i+3]) for i in range(0, len(program), 3)]

# print(len(ins)//9)
p = 0
flag = b""
for i in range(40):
    base = 3 + i * 27
    A = program[base + 8] # xor
    B = program[base + 17] 
    target = (-B) % 256
    c =  target ^ A
    char = chr((c - p) % 256)
    p = target
    flag += char.encode()

print(flag)
