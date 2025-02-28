from pwn import *
if args.REMOTE:
    p = remote('flagsforkeys.challs.olicyber.it', 38060)
else:
    p=process('./flagsforkeys')

p.recvline()
key_1 = 'JIiEv3'
key_2 = 'Kg9FRj'
key_3 = 'xe8zh2'
map = [5,1,0,2,3,4]
payload1 =''
for c in key_1:
    payload1 += chr(ord(c) - 4)
print(payload1)
payload2 = ''
for c in key_2:
    payload2 += chr(ord(c) ^ 6)
print(payload2)
part3 = [0,0,0,0,0,0]
for i in range(len(key_3)):
    part3[map[i]] = key_3[i]
print(part3)
payload3 = ''
for c in part3:
    payload3 += c

last_payload = payload1.encode() + b'-' + payload2.encode() + b'-' + payload3.encode()
print(last_payload)
p.sendline(last_payload)
p.interactive()