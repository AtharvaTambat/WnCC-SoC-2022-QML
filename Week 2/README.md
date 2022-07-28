# Quantum Circuits. Introduction to Qiskit
This portion summarizes how _any_ quantum gate can be built (exactly or to a good approximation) out of the Hadamard gate, phase, CNOT and the $\frac{\pi}{8}$ gate.

## Pauli matrices and rotations
The Pauli matrices give rise to three useful classes of unitary matrices when they are exponentiated, the rotation operators about the x, y, and z axes, deﬁned by the equations:

<img src="https://user-images.githubusercontent.com/95964330/168089904-6daf598e-789b-4c68-8dd3-eada894cc927.png" width=40% height=40%>

## Decomposition for a single qubit 
1. Suppose U is a unitary operation on a single qubit. Then there exist real numbers α, β, γ and δ such that
<img src="https://user-images.githubusercontent.com/95964330/168090687-ebd36686-c3d8-43fa-ae30-5b87a791c982.png" width=23% height=23%>

2. Suppose U is a unitary gate on a single qubit. Then there exist unitary operators A, B, C on a single qubit such that ABC = I and 
<img src="https://user-images.githubusercontent.com/95964330/168091337-4c154f70-6539-482c-985e-71a7db28b839.png" width=17% height=17%>
where $\alpha$ is some overall phase factor.

## Controlled operations
'If A is true, then do B'. This type of controlled operation is one of the most useful in computing, both classical and quantum. A controlled-U operation is a two qubit operation, again with a control and a target qubit. If the control qubit is set then U is applied to the target qubit, otherwise the target qubit is left alone. 

<img src="https://user-images.githubusercontent.com/95964330/168092291-f44fe741-8790-47f5-8006-9c175c9a5178.png" width=20% height=20%>

### Phase shift on qubit

Our ﬁrst step will be to apply the phase shift $e^{i\alpha}$ on the target qubit, controlled by the control qubit. The circuit for the same is represented as follows:

<img src="https://user-images.githubusercontent.com/95964330/168101910-0c4d3b41-dfca-4342-bd06-c96477db623c.png" width=30% height=30%>

We may now complete the construction of the controlled-U operation, as shown in the figure below:

<img src="https://user-images.githubusercontent.com/95964330/168102460-1f1b22fc-6bcb-4582-90ee-f1eeab5af874.png" width=35% height=35%>

### Multi-Qubit conditioning and Controlling Target Qubit When Control Bit Is Not $|1\rangle$

Now that we know how to condition on a single qubit being set, what about conditioning on multiple qubits? More generally, suppose we have n + k qubits, and U is a k qubit unitary operator. Then we deﬁne the controlled operation $C^n(U)$ by the equation:

<img src="https://user-images.githubusercontent.com/95964330/168104142-e1b8fe9d-6c59-4f77-aa74-f9058813d089.png" width=50% height=50%>

That is, the operator U is applied to the last k qubits if the ﬁrst n qubits are all equal to one, and otherwise, nothing is done. How do we implement this with our existing repertoire of gates, where U is an arbitrary single qubit unitary operation? The steps for the same are:

1. Suppose the control qubits are in the computational basis state $|c_1, c_2, . . . , c_n\rangle$. The ﬁrst stage of the circuit is to reversibly all the control bits $c_1, . . . , c_n$ together to produce the product $c_1 · c_2 . . . c_n$ - by continuously applying Toffoli gates to sebsequent qubits.
2. Next, a U operation on the target qubit is performed, conditional on the ﬁnal work qubit being set to one. That is, U is applied if and only if all of $c_1$ through $c_n$ are set.
3. Finally, the last part of the circuit just reverses the steps of the ﬁrst stage, returning all the work qubits to their initial state, $|0\rangle$. The combined result, therefore, is to apply the unitary operator U to the target qubit, if and only if all the control bits $c_1$ through $c_n$ are set, as desired.

The following figure summarizes the process:

<img src="https://user-images.githubusercontent.com/95964330/168136833-282bac31-b5f2-4e8c-bf41-bb3d62bb3b54.png" width=30% height=30%>

What is special with using $|1\rangle$ for deciding whether a _Unitary_ operation will be performed?......NOTHING!!! In the following section we shall consider how to change the circuit a little bit (by insertion of X gates) so that the U-gate responds to $|0\rangle$ instead of $|1\rangle$. (We shall use the open circle notation to indicate conditioning on the qubit being set to zero, while a closed circle indicates conditioning on the qubit being set to one.)

<img src="https://user-images.githubusercontent.com/95964330/168137717-dded19af-45da-4bfd-b932-0fb1487d7220.png" width=30% height=30%>


## Measurement
It is the ﬁnal element used in quantum circuits - a projective measurement in the computational basis is denoted using a ‘meter’ symbol. It follows the following two principles:

1. Prinicple of deferred measurement: Measurements can always be moved from an intermediate stage of a quantum circuit to the end of the circuit; if the measurement results are used at any stage of the circuit then the classically controlled operations can be replaced by conditional quantum operations.

2. Principle of implicit measurement: Without loss of generality, any unterminated quantum wires (qubits which are not measured) at the end of a quantum circuit may be assumed to be measured.

## Universal quantum gates
1. An arbitrary unitary operator may be expressed exactly as a product of unitary operators that each acts non-trivially only on a subspace spanned by two computational basis states.
2. An arbitrary unitary operator may be expressed exactly using single qubit and gates.
3. Single qubit operation may be approximated to arbitrary accuracy using the Hadamard, phase, and $\frac{\pi}{8}$ gates.

> This in turn implies that any unitary operation can be approximated to arbitrary accuracy using Hadamard, phase, CNOT , and $\frac{\pi}{8}$ gates.









