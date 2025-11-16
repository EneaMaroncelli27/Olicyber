from pwn import remote,xor

p = remote("modes.challs.olicyber.it",10802)

ct = bytes.fromhex("866bb5802051d56f37b1073a501b4afe4324424336ba60d4efe9af817b27a95a0f3adec8b809088bbaaebbfa0629c079")
print(len(ct))
iv = ct[:16]
flag_enc = ct[16:]

p.sendlineafter(b': ', flag_enc[:16].hex().encode() )

res = p.recvline().strip()
flag_f = xor(bytes.fromhex(res.decode()), iv)

p.close()
p = remote("modes.challs.olicyber.it",10802)
p.sendlineafter(b': ', flag_enc[16:].hex().encode())

flag_s = xor(bytes.fromhex(p.recvline().strip().decode()), flag_enc[:16])
p.close()
print((flag_f +  flag_s).decode())