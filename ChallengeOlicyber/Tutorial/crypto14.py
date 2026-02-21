from pwn import remote
from Crypto.Hash import SHA256, SHA3_384, SHA224, HMAC 
from Crypto.PublicKey import DSA
from Crypto.Util.number import getPrime,isPrime
p = remote("cr14.challs.olicyber.it", 30007)
p.recvuntil(b'libreria.')
p.recvline()
p.recv(1)
def answer_dsa(p, aura):
    question = p.recvuntil("= ?").strip()
    print(question)
    if "q" in question.decode():
        r = aura.q
    elif "y" in question.decode():
        r = aura.y
    elif "p" in question.decode():
        r = aura.p
    elif "g" in question.decode():
        r = aura.g
    elif "x" in question.decode():
        r = aura.x
    p.sendline(str(r).encode())
try:
    msg = p.recvline().strip()
    question = p.recv(30).strip()
    msg = msg.split(b"=")[1].strip().replace(b"'", b"").replace(b'"', b"")
    h = SHA3_384.new()
    result = h.update(msg).hexdigest()
    p.sendline(result.encode())
    p.recvuntil(b'hex() = ')
    key = bytes.fromhex(p.recvline().strip().replace(b"'", b"").decode())
    print("Sha3-384 sent")
    p.recvuntil(b' = ')
    msg = p.recvline().strip().replace(b"'", b"")
    HMAC = HMAC.new(key, msg, SHA224)
    p.sendline(HMAC.hexdigest().encode())
    print("HMAC sent")
    p.recvuntil(b'DSA.')
    p.recvuntil(b'hex() = \'', timeout=2)
    key = bytes.fromhex(p.recvuntil(b"'", drop=True, timeout=2).strip().decode())
    print(key)
    aura = DSA.import_key(key)
    print(aura)
    p.recv(1)
    answer_dsa(p, aura)
    answer_dsa(p, aura)
    answer_dsa(p, aura)
    p.recvuntil(b'esattamente ')
    bits = int(p.recvuntil(b'bit', drop=True).strip())
    res = getPrime(bits)
    p.sendlineafter(b': ',str(res).encode())
    p.recvuntil(b'= ')
    n_primo = int(p.recvuntil(b"p",drop=True).strip())
    print(n_primo)
    r = "si" if isPrime(n_primo) else "no"
    print(r)
    p.sendlineafter(b'? ', r.encode())
    p.recvuntil(b'Grande! ')
    p.interactive()
except Exception as e:
    print("Error :" + str(e))
    p.interactive()
    exit()