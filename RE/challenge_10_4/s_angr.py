import angr
import claripy

flag_length = 34
flag_format = "VishwaCTF{" # leave it empty if you don't know the flag format

proj = angr.Project("./chal")

flag_chars = [claripy.BVS(f"flag{i}", 8) for i in range(flag_length)] # like Bitvec in z3
flag = claripy.Concat(*flag_chars)

state = proj.factory.full_init_state(
    args = ['./chal', flag],
)
for i in range(len(flag_format)):
    state.solver.add(flag_chars[i] == ord(flag_format[i]))

for i in range(len(flag_format), flag_length):
    state.solver.add(flag_chars[i] >= ord('!'))
    state.solver.add(flag_chars[i] <= ord("~"))
# because we can't find address in IDA use correct and wrong in functions and explore
def is_successful(state):
    return b'CORRECT :)' in state.posix.dumps(1)
def should_abort(state):
    return b'INCORRECT :(' in state.posix.dumps(1)

simgr = proj.factory.simulation_manager(state)
simgr.explore(find=is_successful, avoid=should_abort)

if simgr.found:
    f = simgr.found[0]
    res = f.solver.eval(flag, cast_to=bytes)
    print(res.decode())

