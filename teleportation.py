import pyquil.quil as pq
from pyquil.gates import *
import pyquil.api as api

qvm = api.QVMConnection()
ins = pq.Program()

ins.inst(H(1), CNOT(1, 2))
ins.inst(H(0), Z(0), CNOT(0, 1), H(0))

ins.measure(0, 0).measure(1, 1).if_then(1, X(2)).if_then(0, Z(2))

wvf = qvm.wavefunction(ins, [0, 1])

print wvf
