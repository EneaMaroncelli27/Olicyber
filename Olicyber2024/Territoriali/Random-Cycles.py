from pwn import remote,process
import string

def spin(w, k):
    k = k % len(w)
    return w[-k:] + w[:-k]

def unspin(w,k):
    k = k % len(w)
    return  w[k:] + w[:k]


def craft_alph(key : dict):
    alph = ""
    for c in (string.ascii_letters + string.digits):
        if len(alph) == 50:
            return alph
        if c not in key.keys():
            alph += c
    else:
        sorted_keys = sorted(key, key=key.get, reverse=False)
        for c in sorted_keys:
            if len(alph) == 50:
                return alph
            if c not in alph:
                alph += c


for x in range(100):
    # p = process(['python3',"random-cycles.py"])
    p = remote("random-cycles.challs.olicyber.it", 38102)
    key = {}
    for i in range(10):
        alph_cut = craft_alph(key)
        if alph_cut == None:
            p.sendlineafter(b'text:', b'a'*50)
            p.recvuntil(b'text: ')
            cpt = p.recvline().strip().decode()
            continue
        lalph = alph_cut
        p.sendlineafter(b'text:', alph_cut)
        p.recvuntil(b'text: ')
        cpt = p.recvline().strip().decode()
        for i in range(15):
            if key.get(cpt[i]) != None:
                key[cpt[i]] = max(len(lalph[lalph.index(cpt[i+1]):]), key[cpt[i]])
            key[cpt[i]] = len(lalph[lalph.index(cpt[i+1]):])
            lalph = cpt[:i+1] + spin(lalph[i+1:],key[cpt[i]])
      
        order = string.ascii_lowercase + string.ascii_uppercase + string.digits
        key = dict(sorted(key.items(), key=lambda kv: order.index(kv[0])))

    for n in range(100):
        print("GUESS ",n)
        p.recvuntil(b'text: ')
        guess_enc = p.recvline().strip().decode()
        guess = ['']*50
        guess[0] = guess_enc[0]
        for i in reversed(range(1,len(guess_enc))):
            guess_enc = guess_enc[:i] + unspin(guess_enc[i:], key[guess_enc[i-1]])
        p.sendlineafter(b'text: ',guess_enc.encode())

        r = p.recv(1).decode().strip()
        # p.interactive()
        if r == "N":
            p.close()
            break
    else:
        break
    
p.interactive()
