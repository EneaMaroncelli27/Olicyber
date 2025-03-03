import angr
proj = angr.Project("./justonekey", 
    load_options={"auto_load_libs":False},
    main_opts={"base_addr":0})
init = proj.factory.entry_state()
sim = proj.factory.simulation_manager(init)
s = sim.explore(find=0x150C, avoid=[0x15A7, 0x1466])
print(s.found[0].posix.dumps(0), end="")

#stampa la key 

from pwn import *
p = remote('ustonekey.challs.olicyber.it', 38064)
p.sendlineafter(b': ',s.found[0].posix.dumps(0))
p.interactive()