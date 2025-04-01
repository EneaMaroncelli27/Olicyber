from pwn import remote,process

# p = process('choose_your_otp.py')
p = remote('chooseyourotp.challs.olicyber.it', 38302)

flag_bin = ''
for i in range(350):
    print(i)
    payload = str(2**i)
    print("payload " + payload)
    p.sendlineafter(b'> ', payload)
    # p.interactive()

    
    risp = p.recvline().strip()
        
    tmp = str(int(risp) >> i)
    print(f"{tmp=}")
    
    flag_bin = tmp[0] + flag_bin
    print(f"{flag_bin=}")
    # input()
    
        
print("Final flag---> ", flag_bin)
    