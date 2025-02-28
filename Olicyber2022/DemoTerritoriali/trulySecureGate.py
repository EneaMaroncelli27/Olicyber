import angr
proj = angr.Project("./rincorro", 
    load_options={"auto_load_libs":False},
    main_opts={"base_addr":0})
init = proj.factory.entry_state()
sim = proj.factory.simulation_manager(init)
s = sim.explore(find=0x1465)
print(s.found[0].posix.dumps(0).decode(), end="")
