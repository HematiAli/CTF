import sys
import random

key = sys.argv[1]
flag = '**CENSORED**'

assert len(key) == 13
assert max([ord(char) for char in key]) < 128
assert max([ord(char) for char in flag]) < 128

message = flag + "|" + key

encrypted = chr(random.randint(0, 128))

for i in range(0, len(message)):
  encrypted += chr((ord(message[i]) + ord(key[i % len(key)]) + ord(encrypted[i])) % 128)

print(encrypted.encode('hex'))
# 7c153a474b6a2d3f7d3f7328703e6c2d243a083e2e773c45547748667c1511333f4f745e
