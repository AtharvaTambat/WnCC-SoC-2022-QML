# Introduction to QC and Linear Algebra
## What is a Quantum Bit?
_Quantum Bit_ (or _qubit_ in short) is analogous to the classical bit, which is the fundamental unit of information used in most computers today - but the important distinction between them comes in how the information is _stored_ not _measured_. While a classical bit can only store a _0_ or a _1_ the quantum bit is stored as a linear combination of _computational basis states_. ( <img src="https://user-images.githubusercontent.com/95964330/164874781-7c8f5ff1-5a00-496c-8f3c-0c8a34f5fea6.png" width=2.2% height=2.2%> and <img src="https://user-images.githubusercontent.com/95964330/164912039-69f001dd-55f6-45e6-9c87-9f276af6081b.png" width=2.2% height=2.2%> )

<img src="https://user-images.githubusercontent.com/95964330/164874629-662d2bef-87f2-4040-998a-5c9d68ef021c.png" width=20% height=50%>

The linear combination may be written in terms of parameters as given below:

![Linear combination](https://user-images.githubusercontent.com/95964330/164911312-21d86906-97e0-4f2c-af14-f1f528ef83e5.png)

and can be represented on a sphere as shown (Bloch Sphere):

![Bloch Sphere](https://user-images.githubusercontent.com/95964330/164911401-18eaa4fc-23b2-4623-a6f0-2630dfee2f4b.png)

## Multiple Qubits
Let us consider the case of two Qubits. The system can be expressed as a superposition (linear combination) of 4 _computational basis states_ (in simple words 4 different possibilities that the system can "collapse" into) - <img src="https://user-images.githubusercontent.com/95964330/164911803-8a1d0b81-915b-4169-8777-876bcc9f42c2.png" width=10% height=10%> ). An important two-qubit state is a Bell State or EPR state:

<img src="https://user-images.githubusercontent.com/95964330/164911760-a353c3dd-6938-45c4-bf37-53ed46193dc2.png" width=10% height=10%>

It has the property that upon measuring the value of the first qubit (which can be either 0 or 1 with the probability 1/2 for each outcome), the outcome of the second qubit is already determined. A strong correlation exists in a Bell state than could ever exist in a classical system.

## Quantum Computation
### Single Qubit Gates
The only single bit gate one can think of in a classical system is the NOT gate - which convert _0_ state to _1_ state and vice-versa. An analogous quantum NOT gate also exists ( named the X gate) - along with an infinite number of other one qubit gates!!!
One property of the single qubit gates, that I find worth mentioning is that they act _linearly_ (meaning, <img src="https://user-images.githubusercontent.com/95964330/164912453-df63f10d-4dec-4215-94f3-3732b38edf19.png" width=7% height=7%> will change to <img src="https://user-images.githubusercontent.com/95964330/164912455-e4c0c738-c414-4059-bbf2-531b29ce0a85.png" width=8% height=8%>) - non-linear behavious of operators can lead to paradoxes such as - time travel, faster-than-light-communication etc.

Quantum Operators can be thought of as matrices acting on the vector ![image](https://user-images.githubusercontent.com/95964330/164912587-aabbca59-b3e1-4e88-8398-bf39489420c0.png). For example, the NOT operator can be thought of as the  matrix:

![image](https://user-images.githubusercontent.com/95964330/164912638-f70b94a5-414b-4187-96b6-d88363e70f34.png). The operation of which can be seen as: ![image](https://user-images.githubusercontent.com/95964330/164912741-f88a8066-09cb-4ca6-8a89-b787ed49870a.png)


Other similar qubit operators are:

![image](https://user-images.githubusercontent.com/95964330/164912658-67ff1906-9302-4fd0-ad4c-58e36efc1059.png) - the Z gate

![image](https://user-images.githubusercontent.com/95964330/164912666-d40c7ca7-e7fb-4559-aff2-acf71fea4742.png) - the _Hadamard gate_

The following image summarises the action of some single-qubit operators:

![image](https://user-images.githubusercontent.com/95964330/164912718-87d63d1e-2115-46ff-a5f8-9ea860a76961.png)



















