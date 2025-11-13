from pwn import remote
import json,base64



p = remote('based.challs.olicyber.it', 10600)

p.recvuntil(b'la tua risposta\n\n')

while True:
    question = p.recvuntil(b': "').strip()
    
    message = p.recvuntil(b'"}',drop=True).strip()
    answer = ''
    
    if b'questo a binario' in question:
        answer = {"answer": bin(int.from_bytes(message))[2:]} 
    elif b'questo da binario' in question:
        message = message.zfill((len(message)+7)//8*8)
        answer = {"answer": int(message,2).to_bytes(len(message)//8,byteorder='big').decode()}         
    elif b'questo da base64' in question:
        answer = {"answer": base64.b64decode(message).decode()}
    elif b'questo da esadecimale' in question:
        answer = {"answer": bytes.fromhex(message.decode()).decode()}
    elif b'questo a esadecimale' in question:
        answer ={"answer": message.hex()}
    elif b'questo a base64' in question:
        answer = {"answer": base64.b64encode(message).decode()}
    else:
        print(question)
        p.interactive()
    

    p.sendlineafter(b'!\n',json.dumps(answer).encode())
    try:
        p.recvuntil(b'Converti')
    except:
        p.recvuntil(b'te!')
        p.recvline()
        flag = p.recvline().strip()
        print(''.join(chr(int(c,8)) for c in flag.decode().split()))

        p.interactive()
