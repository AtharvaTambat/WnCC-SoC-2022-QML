# Import all the libraries
from qiskit import *

# To visualise the circuit
%matplotlib inline
from qiskit.tools.visualization import plot_histogram

# The number to be guessed by the quantum circuit
secretnumber = '1010100101'

# To create the circuit for Bernstein-Vazirani Algorithm
circuit = QuantumCircuit(len(secretnumber)+1,len(secretnumber))

circuit.h(range(len(secretnumber)))
circuit.x(len(secretnumber))
circuit.h(len(secretnumber))

circuit.barrier()

for i, decide in enumerate(reversed(secretnumber)):
    if decide == '1':
        circuit.cx(i,len(secretnumber))
        
circuit.barrier()
circuit.h(range(len(secretnumber)))
circuit.barrier()

# To measure the output of the circuit
circuit.measure(range(len(secretnumber)),range(len(secretnumber)))

# To draw the circuit in mat plot lib
circuit.draw(output = 'mpl')

# To run the quantum simulator for the circuit 
backend = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend = backend, shots = 1).result()
counts = result.get_counts()
print(counts)
