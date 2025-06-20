
from hashlib import sha512

hash_tung = sha512(b"tung tung tung sahur VS cappuccino assassino").digest()


inp = bytearray(bytearray.fromhex("2ce4190bdf7c920301217b56b11f067fd361bb2f11b04e7b9a75912b16adb5af96e00ed7ecbcb1fc5cf80837ac4f40d181c0cdf9b8167ce2f982ac6a6f9035f2"))

for i in range(64):
    inp[i] ^= hash_tung[i]

for j in range(0,64,2):
    inp[j]^=32

print(inp.decode())