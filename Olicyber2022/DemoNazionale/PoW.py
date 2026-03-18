from pwn import remote
from hashlib import sha256
from tqdm import trange
import json
def precompute():
    mappa = {}
    for i in trange(100_000_000):
        _hash = sha256(str(i).encode()).hexdigest()[:6]
        mappa[_hash] = str(i).encode().hex()
    with open('logs.json','w') as f:
        f.write(json.dumps(mappa))


# precompute()
p = remote("pow.challs.olicyber.it", 12209)
with open('logs.json','r') as f:
    prefixes = json.loads(f.read())
while True:
    try:
        p.recvuntil(b'with ')
        prefix = p.recvline().strip().decode()
        assert prefix in prefixes
        print(prefix in prefixes)
        p.sendline(prefixes[prefix])
    except Exception as e:
        print(f"An error occurred {e}")
        p.interactive()
        exit()
        