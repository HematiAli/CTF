import angr
import claripy

proj = angr.Project('./registers')
state = proj.factory.blank_state(
    addr = 0x80488c7, # after call input because user input destroy bti vectors
    add_options = {
        angr.options.SYMBOL_FILL_UNCONSTRAINED_MEMORY,
        angr.options.SYMBOL_FILL_UNCONSTRAINED_REGISTERS,
    }
)
pass0 = claripy.BVS("pass0", 32)
pass1 = claripy.BVS("pass1", 32)
pass2 = claripy.BVS("pass2", 32)

state.regs.eax = pass0
state.regs.ebx = pass1
state.regs.edx = pass2

simulation = proj.factory.simgr(state)

def is_successful(state):
    return b"Good Job." in state.posix.dumps(1)

def noo(state):
    return b"Try again." in state.posix.dumps(1)

simulation.explore(find=is_successful, avoid=noo)

if simulation.found:
    state = simulation.found[0]
    sol0 = state.solver.eval(pass0)
    sol1 = state.solver.eval(pass1)
    sol2 = state.solver.eval(pass2)
    s = " ".join(map("{:x}".format, [sol0, sol1, sol2]))
    print(s)
else:
    print("HIHIHIHIHH")
