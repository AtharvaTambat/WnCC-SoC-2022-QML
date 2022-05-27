# Code for quantum teleportation

from qiskit import *

# Create a new quantum circuit
circuit = QuantumCircuit(3,3)

# For visualizing the circuit
%matplotlib inline
circuit.draw(output = 'mpl', cregbundle=False)

# Adding appropriate gates to the circuit
circuit.x(0)
circuit.barrier()
circuit.h(1)
circuit.cx(1,2)
circuit.cx(0,1)
circuit.h(0)
circuit.barrier()
circuit.measure([0,1],[0,1])circuit.barrier()
circuit.cx(1,2)
circuit.cz(0,2)

# For visualizing the Quantum teleportation circuit
circuit.draw(output = 'mpl')

#For measuring the output on a quantum simulator
circuit.measure(2,2)
backend = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend = backend, shots = 1024).result()
counts = result.get_counts()

# plotting the result on histogram
from qiskit.tools.visualization import plot_histogram
plot_histogram(counts)
