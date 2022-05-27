# Importing all necessary libraries
from qiskit import *


# Creating a quantum circuit
circuit = QuantumCircuit(2,2)

# For visualising the circuit
%matplotlib inline
circuit.draw(output = 'mpl', cregbundle=False)


# Adding appropriate gates to the circuit
circuit.x(0)
circuit.cx(0,1)
circuit.cx(1,0)
circuit.cx(0,1)

# To visualize the circuit
circuit.draw(output = 'mpl', cregbundle=False)

# To measure the swapped output and draw it in matplotlib
circuit.measure([0,1],[0,1])
circuit.draw(output = 'mpl')

# To run the quantum simulator
backend = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend = backend, shots = 1024).result()
counts = result.get_counts()

# plotting the result on histogram
from qiskit.tools.visualization import plot_histogram
plot_histogram(counts)
