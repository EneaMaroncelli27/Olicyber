from z3 import *

sistema = Solver()

vars = [Int(f'a1[{i}]') for i in range(0, 20)]

print(vars)
sistema.add(vars[0] * vars[0] - 204 * vars[0] == -10404)
sistema.add(vars[1] * vars[1] - 216 * vars[1] == -11664)
sistema.add(vars[2] * vars[2] - 194 * vars[2] == -9409)
sistema.add(vars[3] * vars[3] - 206 * vars[3] == -10609)
sistema.add(vars[4] * vars[4] - 246 * vars[4] == -15129)
sistema.add(vars[5] * vars[5] - 200 * vars[5] == -10000)
sistema.add( vars[6] * vars[6] - 102 * vars[6] == -2601 )
sistema.add( vars[7] * vars[7] - 232 * vars[7] == -13456)
sistema.add(vars[8] * vars[8] - 202 * vars[8] == -10201)
sistema.add(vars[9] * vars[9] - 228 * vars[9] == -12996 )
sistema.add(vars[10] * vars[10] - 218 * vars[10] == -11881)
sistema.add( vars[11] * vars[11] - 210 * vars[11] == -11025)
sistema.add( vars[12] * vars[12] - 220 * vars[12] == -12100 )
sistema.add( vars[13] * vars[13] - 194 * vars[13] == -9409 )
sistema.add( vars[14] * vars[14] - 220 * vars[14] == -12100)
sistema.add(vars[15] * vars[15] - 232 * vars[15] == -13456)
sistema.add( vars[16] * vars[16] - 202 * vars[16] == -10201 )
sistema.add(vars[17] * vars[17] - 190 * vars[17] == -9025)
sistema.add( vars[18] * vars[18] - 96 * vars[18] == -2304)
sistema.add(vars[19] * vars[19] - 250 * vars[19] == -15625)
sistema.check()

flag = [0]*20
for v in sistema.model():
  idx = int(str(v).split('[')[1][:-1])
  flag[int(str(v).split('[')[1][:-1])] = sistema.model()[v].as_long()
print(''.join([chr(c) for c in flag]))