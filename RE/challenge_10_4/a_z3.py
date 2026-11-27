from z3 import *

solver = Solver()

s = [BitVec(f"s{i}", 32) for i in range(34)]



solver.add(s[3] + s[4] + s[1] + s[7] - s[8] * s[2] * s[6] * s[5] - s[11] - s[9] - s[10] == 0xFCE1B58A)
solver.add(s[3] - s[4] - s[6] + s[9] + s[8] * s[11] * s[10] - s[2] + s[5] + s[7] * s[12] == 285707)
solver.add(s[11] + s[10] * s[4] + s[3] - s[12] * s[7] - s[13] - s[5] * s[9] * s[6] + s[8] == 0xFFF3D627)
solver.add(s[4] + s[12] - s[7] * s[11] - s[9] - s[5] * s[6] - s[14] - s[8] * s[13] * s[10] == 0xFFFB9605)
solver.add(s[13] + s[14] + s[7] + s[6] - s[12] - s[15] * s[11] - s[5] + s[8] * s[10] * s[9] == 666868)
solver.add(s[12] + s[15] * s[16] + s[11] + s[13] - s[10] + s[6] * s[8] - s[7] - s[9] + s[14] == 9837)
solver.add(s[7] + s[11] - s[8] + s[16] * s[13] - s[17] - s[14] - s[9] + s[10] * s[15] - s[12] == 9858)
solver.add(s[17] + s[12] + s[9] - s[18] - s[8] - s[15] + s[16] + s[11] * s[14] * s[13] - s[10] == 296504)
solver.add(s[11] * s[13] * s[18] * s[16] - s[17] - s[10] + s[9] + s[15] * s[12] - s[19] - s[14] == 10963387)
solver.add(s[17] + s[16] + s[20] + s[12] - s[14] * s[18] * s[15] * s[19] - s[13] - s[11] - s[10] == 0xFC129A84)
solver.add(s[16] - s[19] - s[15] + s[11] * s[13] + s[18] + s[21] * s[12] + s[14] + s[17] * s[20] == 13340)
solver.add(s[18] * s[16] + s[17] * s[15] - s[20] - s[12] - s[19] * s[14] + s[22] + s[13] * s[21] == 4641)
solver.add(s[15] + s[20] + s[18] + s[21] + s[13] * s[19] - s[22] - s[16] - s[14] + s[17] * s[23] == 6428)
solver.add(s[19] * s[24] + s[15] * s[20] + s[16] * s[14] + s[23] - s[18] * s[21] - s[22] * s[17] == 7851)
solver.add(s[19] + s[24] + s[22] + s[21] + s[25] + s[16] + s[18] + s[20] * s[23] - s[15] + s[17] == 2997)
solver.add(s[17] * s[23] + s[20] * s[25] - s[16] + s[26] * s[21] - s[24] + s[22] * s[19] * s[18] == 342425)
solver.add(s[20] + s[26] + s[24] * s[17] + s[27] * s[22] * s[25] - s[21] - s[19] * s[18] + s[23] == 243251)
solver.add(s[24] + s[22] + s[25] * s[21] - s[28] - s[19] - s[26] * s[27] * s[20] - s[23] + s[18] == 0xFFF95DAC)
solver.add(s[28] + s[19] + s[25] + s[29] - s[24] - s[21] - s[23] + s[27] - s[22] * s[26] + s[20] == 0xFFFFECA3)
solver.add(s[21] + s[30] + s[26] + s[22] * s[23] - s[29] + s[20] - s[24] * s[25] - s[27] - s[28] == 0xFFFFF9A7)
solver.add(s[22] + s[26] + s[25] + s[30] + s[23] - s[24] - s[29] - s[31] - s[21] - s[27] - s[28] == 0xFFFFFF70)
solver.add(s[29] + s[30] + s[31] - s[26] - s[25] - s[23] - s[28] - s[27] - s[22] - s[32] * s[24] == 0xFFFFE4A7)
solver.add(s[33] + s[25] - s[31] * s[23] + s[27] - s[26] * s[32] + s[30] - s[24] * s[29] - s[28] == 0xFFFFB6B5)

for i, ch in enumerate(b"VishwaCTF"):
    solver.add(s[i] == ch)

for i in s:
    solver.add(i >= 32, i <= 126)

if solver.check() == sat:
    m = solver.model()
    print(bytes([m[x].as_long() for x in s]))