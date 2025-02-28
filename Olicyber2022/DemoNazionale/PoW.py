import hashlib
import os
from pwn import *
p = remote("pow.challs.olicyber.it", 12209)
while True:
    try:
        p.recvuntil(b"with ")
        def find_x_faster(target_prefix):
         while True:
            # Genera direttamente i byte casuali
            random_bytes = os.urandom(16)
            hash_value = hashlib.sha256(random_bytes).hexdigest()
            if hash_value.startswith(target_prefix):
                return random_bytes.hex()


        # Target prefix
        target_prefix = p.recvline().decode().strip()
        

        # Find x
        x = find_x_faster(target_prefix)
        p.sendline(x)
        print(f"x = {x}")
        # print(f"SHA-256 = {hash_value}")
    except Exception as e:
        p.interactive()
        break