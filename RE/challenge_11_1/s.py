import angr

p = angr.Project('./find')

state = p.factory.entry_state(
    add_options = {
        angr.options.SYMBOL_FILL_UNCONSTRAINED_MEMORY,
        angr.options.SYMBOL_FILL_UNCONSTRAINED_REGISTERS
    }
)

simgr = p.factory.simgr(state)

simgr.explore(find=0x8048694)

if simgr.found:
    f = simgr.found[0]
    print(f.posix.dumps(0))