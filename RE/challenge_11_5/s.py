import angr
import claripy

proj = angr.Project('./memory')
state = proj.factory.blank_state(
    addr = 0x8048618, # after call input because user input destroy bti vectors
    add_options = {
        angr.options.SYMBOL_FILL_UNCONSTRAINED_MEMORY,
        angr.options.SYMBOL_FILL_UNCONSTRAINED_REGISTERS,
    }
)
pass0 = claripy.BVS("pass0", 8 * 8)
pass1 = claripy.BVS("pass1", 8 * 8)
pass2 = claripy.BVS("pass2", 8 * 8)
pass3 = claripy.BVS("pass2", 8 * 8)

state.memory.store(0x0AB232C0, pass0)
state.memory.store(0x0AB232C8, pass1)
state.memory.store(0x0AB232D0, pass2)
state.memory.store(0x0AB232D8, pass3)

simulation = proj.factory.simgr(state)

def is_successful(state):
    return b"Good Job." in state.posix.dumps(1)

def noo(state):
    return b"Try again." in state.posix.dumps(1)

simulation.explore(find=is_successful, avoid=noo)

if simulation.found:
    state = simulation.found[0]
    sol0 = state.solver.eval(pass0, cast_to=bytes).decode()
    sol1 = state.solver.eval(pass1, cast_to=bytes).decode()
    sol2 = state.solver.eval(pass2, cast_to=bytes).decode()
    sol3 = state.solver.eval(pass3, cast_to=bytes).decode()
    s = " ".join([sol0, sol1, sol2, sol3])
    print(s)
else:
    print("HIHIHIHIHH")
