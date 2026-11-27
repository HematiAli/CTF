import angr
import claripy

proj = angr.Project('./matrix')
state = proj.factory.entry_state()

sim = proj.factory.simgr()
sim.run()

if sim.deadended:
    for s in sim.deadended:
        tmp = s.posix.dumps(0)
        print(tmp)