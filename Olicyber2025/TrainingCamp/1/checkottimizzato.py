from pwn import *
import time
from tqdm import trange
context.log_level = 'critical'
flag = b''
list_byte = bytes(range(256))
tmp_max = 0
while True:
    for i in trange(256):
        p = process('./optimized')
        byte = list_byte[i]
        trying = flag + bytes([byte])
        p.recvline()
        start_time = time.time()
        p.sendline(trying)
        p.recvline()
        end_time = time.time()
        tot_time = end_time - start_time
        if tot_time > tmp_max:
            tmp_max = tot_time
            max_byte = bytes([byte])
        p.close()
    flag += max_byte
    if flag.endswith(b'}'):
        break
    print(f'Flag trovata finora {flag.decode()}')
print(f'Flag trovata --> {flag.decode()}')