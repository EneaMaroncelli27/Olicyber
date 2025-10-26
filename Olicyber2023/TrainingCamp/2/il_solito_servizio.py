from Crypto.Util.number import bytes_to_long
from pwn import remote

p = 290413720651760886054651502832804977189
int_command = bytes_to_long('get_flag'.encode())
admin_public_key = 285134739578759981423872071328979454683

## (admin_pubk * sign ) = int_command % p
## possiamo dividere entrambe le parti per la pubk --> questo perche pubk^-1 = inv(pubk,p)

inv = pow(admin_public_key,-1,p)

signature = (int_command*inv)%p

p = remote('il-solito-servizio.challs.olicyber.it', 34006)
p.sendlineafter(b'>',b'1')
p.sendlineafter(b': ',str(signature).encode())
p.interactive()
    