data = open("program", "rb").read()

p = 0
flag = bytearray()

for i in range(40):
    base = 3 + i * 27

    A = data[base + 8]
    B = data[base + 17]
    target = (-B) % 256
    current = target ^ A
    char = (current - p) % 256
    flag.append(char)
    p = target

print(flag.decode())
