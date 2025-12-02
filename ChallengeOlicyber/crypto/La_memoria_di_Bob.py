from pwn import remote,log
from Crypto.Util.Padding import pad
from base64 import b64decode
import string

p = remote('bob.challs.olicyber.it', 10602)
alph = string.ascii_letters + string.digits + string.punctuation + ' '
f = b'pensi? Bob: Ok. Allora mi puoi dare la flag? Alice: Nah, ma ti pare? Sono studiata io... Bob: Ma seriamente, ti immagini se qualcuno riuscisse ad ottenere i nostri messaggi?'
print(len(f))
for j in range(len(f)+1,224):
    p = remote('bob.challs.olicyber.it', 10602)
    log.info(f'Leaking byte so far: {f.decode()}')
    if j%16 == 6:
        found = False
        for s in alph:
            p = remote('bob.challs.olicyber.it', 10602)

            for z in alph:
                c = s.encode() + z.encode()
                tmp = c +f
                
                payload =b'a'*11 + pad(tmp,16) + b'a'*(j+1)
                
                # print(f'Trying byte: {c}')
                try:
                
                    p.sendlineafter(b'Bob: ', payload)
                    
                    p.recvuntil(b'!')
                    
                    enc = b64decode(p.recvuntil(b'non ', drop=True).decode().strip())
                    

                    blocks = []
                    for i in range(len(enc.hex())//32):
                        block = enc.hex()[i*32:(i+1)*32]
                        # print(block)
                        blocks.append(block)    
                    # input()
                    
                    if blocks[1] == blocks[-1-j//16]:
                        log.success(f'Found byte: {c.decode()}')
                        f = c + f
                        p.sendlineafter(b'1\n',b'1')
                        p.close()
                        found = True
                        break
                    
                    p.sendlineafter(b'1\n',b'1')
                except Exception as e:
                    print(e)
                    print(blocks)
                    p.interactive()

            if found:
                break
            p.close()
                
    elif j%16 == 7:
        continue
    else:

        for i in alph:
            c = i.encode()
            tmp = c +f
            
            payload =b'a'*11 + pad(tmp,16) + b'a'*j
            
            # print(f'Trying byte: {c}')
            try:
            
                p.sendlineafter(b'Bob: ', payload)
                
                p.recvuntil(b'!')
                
                enc = b64decode(p.recvuntil(b'non', drop=True).decode().strip())
                

                blocks = []
                for i in range(len(enc.hex())//32):
                    block = enc.hex()[i*32:(i+1)*32]
                    # print(block)
                    blocks.append(block)    
                # input()
                if len(tmp) % 16 == 0:
                    if blocks[1] == blocks[-2-(j-1)//16]:
                        
                        log.success(f'Found byte mod 16: {c.decode()}')
                        f = c + f
                        p.sendlineafter(b'1\n',b'1')
                        p.close()

                        break

                else:
                    if blocks[1] == blocks[-1-j//16]:
                       
                        log.success(f'Found byte position {j}: {c.decode()}')
                        f = c + f
                        p.sendlineafter(b'1\n',b'1')
                        p.close()

                        break
                
                p.sendlineafter(b'1\n',b'1')
            except:
                p.interactive()


p.interactive()
