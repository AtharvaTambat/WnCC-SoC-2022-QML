# Quantum Circuits. Introduction to Qiskit
This portion summarizes how _any_ quantum gate can be built (exactly or to a good approximation) out of the Hadamard gate, phase, CNOT and the π/8 gate.

## Pauli matrices and rotations
The Pauli matrices give rise to three useful classes of unitary matrices when they are exponentiated, the rotation operators about the x, y, and z axes, deﬁned by the equations:

<img src="https://user-images.githubusercontent.com/95964330/168089904-6daf598e-789b-4c68-8dd3-eada894cc927.png" width=40% height=40%>

## Decomposition for a single qubit 
1. Suppose U is a unitary operation on a single qubit. Then there exist real numbers α, β, γ and δ such that
<img src="https://user-images.githubusercontent.com/95964330/168090687-ebd36686-c3d8-43fa-ae30-5b87a791c982.png" width=23% height=23%>

2. Suppose U is a unitary gate on a single qubit. Then there exist unitary operators A, B, C on a single qubit such that ABC = I and 
<img src="https://user-images.githubusercontent.com/95964330/168091337-4c154f70-6539-482c-985e-71a7db28b839.png" width=17% height=17%>
where α is some overall phase factor.

## Controlled operations
'If A is true, then do B'. This type of controlled operation is one of the most useful in computing, both classical and quantum. A controlled-U operation is a two qubit operation, again with a control and a target qubit. If the control qubit is set then U is applied to the target qubit, otherwise the target qubit is left alone. 

<img src="https://user-images.githubusercontent.com/95964330/168092291-f44fe741-8790-47f5-8006-9c175c9a5178.png" width=20% height=320%>
