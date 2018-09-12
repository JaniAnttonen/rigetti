from pyquil.quil import Program
from pyquil.api import QVMConnection, QPUConnection
from pyquil.gates import H, CNOT, MEASURE

qp = QPUConnection()
qvm = QVMConnection()
p = Program(H(0), CNOT(0, 1), MEASURE(0, 0), MEASURE(1, 1))
results = qp.run(p, classical_addresses=[0, 1], trials=10)

print("Entangled qubits galore:")
print(results)
