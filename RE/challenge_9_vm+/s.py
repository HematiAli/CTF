"""
every where that use MOD_OPCODE use 02 => this main program check (i % 2 == 0)
"""
flag = b"\x56\x4c\x75\x5c\x38\x6d\x39\x58\x6c\x28\x3e\x57\x7b\x5f\x3f\x54\x44\x5b\x71\x20\x82\x1b\x8b\x50\x80\x46\x7e\x15\x8a\x57\x7d\x5a\x50\x54\x81\x51\x8c\x0c\x94\x44"
i = 0
res = []
while i < len(flag):
    if i % 2 == 0:
        res.append(flag[i] - i)
    else:
        res.append(flag[i] + i)
    i += 1

print(bytes(res).decode())