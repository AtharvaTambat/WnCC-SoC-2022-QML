# Introduction to QC and Linear Algebra
## What is a Quantum Bit?
_Quantum Bit_ (or _qubit_ in short) is analogous to the classical bit, which is the fundamental unit of information used in most computers today - but the important distinction between them comes in how the information is _stored_ not _measured_. While a classical bit can only store a _0_ or a _1_ the quantum bit is stored as a linear combination of _computational basis states_. ( <img src="https://user-images.githubusercontent.com/95964330/164874781-7c8f5ff1-5a00-496c-8f3c-0c8a34f5fea6.png" width=2.2% height=2.2%> and <img src="https://user-images.githubusercontent.com/95964330/164912039-69f001dd-55f6-45e6-9c87-9f276af6081b.png" width=2.2% height=2.2%> )

<img src="https://user-images.githubusercontent.com/95964330/164874629-662d2bef-87f2-4040-998a-5c9d68ef021c.png" width=20% height=50%>

The linear combination may be written in terms of parameters as given below:

![Linear combination](https://user-images.githubusercontent.com/95964330/164911312-21d86906-97e0-4f2c-af14-f1f528ef83e5.png)

and can be represented on a sphere as shown (Bloch Sphere):

<img src="https://user-images.githubusercontent.com/95964330/164911401-18eaa4fc-23b2-4623-a6f0-2630dfee2f4b.png" width=20% height=20%>

## Multiple Qubits
Let us consider the case of two Qubits. The system can be expressed as a superposition (linear combination) of 4 _computational basis states_ (in simple words 4 different possibilities that the system can "collapse" into) - <img src="https://user-images.githubusercontent.com/95964330/164911803-8a1d0b81-915b-4169-8777-876bcc9f42c2.png" width=10% height=10%> ). An important two-qubit state is a Bell State or EPR state:

<img src="https://user-images.githubusercontent.com/95964330/164911760-a353c3dd-6938-45c4-bf37-53ed46193dc2.png" width=10% height=10%>

It has the property that upon measuring the value of the first qubit (which can be either 0 or 1 with the probability 1/2 for each outcome), the outcome of the second qubit is already determined. A strong correlation exists in a Bell state than could ever exist in a classical system.

## Quantum Computation
### Single Qubit Gates
The only single bit gate one can think of in a classical system is the NOT gate - which convert _0_ state to _1_ state and vice-versa. An analogous quantum NOT gate also exists ( named the X gate) - along with an infinite number of other one qubit gates!!!
One property of the single qubit gates, that I find worth mentioning is that they act _linearly_ (meaning, <img src="https://user-images.githubusercontent.com/95964330/164912453-df63f10d-4dec-4215-94f3-3732b38edf19.png" width=7% height=7%> will change to <img src="https://user-images.githubusercontent.com/95964330/164912455-e4c0c738-c414-4059-bbf2-531b29ce0a85.png" width=8% height=8%>) - non-linear behavious of operators can lead to paradoxes such as - time travel, faster-than-light-communication etc; and that they are _Unitary_ (<img src="https://user-images.githubusercontent.com/95964330/164912784-9d16218c-aaba-4080-b2e3-3e5038379c94.png" width=5% height=5%>)

Quantum Operators can be thought of as matrices acting on the vector ![image](https://user-images.githubusercontent.com/95964330/164912587-aabbca59-b3e1-4e88-8398-bf39489420c0.png). For example, the NOT operator can be thought of as the  matrix:

![image](https://user-images.githubusercontent.com/95964330/164912638-f70b94a5-414b-4187-96b6-d88363e70f34.png). The operation of which can be seen as: ![image](https://user-images.githubusercontent.com/95964330/164912741-f88a8066-09cb-4ca6-8a89-b787ed49870a.png)


Other similar qubit operators are:

![image](https://user-images.githubusercontent.com/95964330/164912658-67ff1906-9302-4fd0-ad4c-58e36efc1059.png) - the Z gate

![image](https://user-images.githubusercontent.com/95964330/164912666-d40c7ca7-e7fb-4559-aff2-acf71fea4742.png) - the _Hadamard gate_

The following image summarises the action of some single-qubit operators:

<img src="https://user-images.githubusercontent.com/95964330/164912718-87d63d1e-2115-46ff-a5f8-9ea860a76961.png" width=50% height=50%>

Interestingly, _any_ set of single-quibit gates can be constructed out of a _finite- set of qantum gates - not always exactly, but to an _arbitrarily_ good precision; using the decomposition: <img src="https://user-images.githubusercontent.com/95964330/164959380-c167ae2f-2cee-4b39-8015-1c7001f01f0d.png" width=50% height=50%>

### Multiple Qubit Gates
The prototypical multi-qubit logic gate is the _controlled_-NOT or _CNOT_ gate - the first quibt decides whether the second qubit will be flipped or not. the second qubit will be flipped only if the first qubit (_control qubit_) is set to 1. The action of the gate can be summarised as: <img src="https://user-images.githubusercontent.com/95964330/164959586-e00f0c75-dce5-424c-9b68-d32a7f76a524.png" width=15% height=15%> and can be represented by the matrix:

<img src="https://user-images.githubusercontent.com/95964330/164959626-410d1480-5b14-4615-8e48-73e5d12a72ed.png" width=15% height=15%>

Just like in the glassical gates, the _NAND_ gate can be used to build _every_ other classical gate, in qubit-gates, a combination of the _CNOT_ gate and _single - qubit_ gates can represent _any_ multiple-qubit gate.

One important distinction between classical gates and qubit gates is that there is an irreversible loss of information when classical gates are used. For example - an output _0_ of the _AND_ gate can come from either of the following combinations - (0,1), (1,0), (0,0) - meaning, we cannot retrieve back the input by looking at the output. Surprisingly, qubit-gates, by their representation using _Unitary matrices_ (which are invertible), are also invertible - i.e. the input ca be uniquely determined by looking at the output.

### Measurments in bases other than the computational bases
Note that the states <img src="https://user-images.githubusercontent.com/95964330/164874781-7c8f5ff1-5a00-496c-8f3c-0c8a34f5fea6.png" width=2.2% height=2.2%> and <img src="https://user-images.githubusercontent.com/95964330/164912039-69f001dd-55f6-45e6-9c87-9f276af6081b.png" width=2.2% height=2.2%> are one of many possible choice of basis states.  It is possible to express a state as a linear comination of an arbitrary basis set ( say, <img src="https://user-images.githubusercontent.com/95964330/164992819-a5b7cf69-a5a1-4077-b1dc-1c10b1f423e9.png" width=2.2% height=2.2%> and <img src="https://user-images.githubusercontent.com/95964330/164992852-c824a9b3-a7a0-45f7-9060-91cbca562a1d.png" width=2.2% height=2.2%>). It would help if the  new basis set was orthonormal. In that case the square of the modulus of the coeffecient of each basis would be the probability of that set of outcomes of the set of qubits on measurement.

### Quantum circuits
A number of features of the quantum circuits, which differentiates it from the conventional circuits are:
<ol>
  <li> Quantum circuits do not allow loops/ feedback.</li>
  <li> They do not allow FANIN - several wires being joined together and an bitwise _OR_ of the inputs being shown as output.</li>
  <li> They do not allow FANOUT - several copies of a qubit being produced.</li>
</ol>

Two important elements of a quantum circuit are: 

1. Controlled Gates - with one control bit (similar to that in CNOT gate) and n target qubits - represented by a Unitary matrix U. </li> ![image](https://user-images.githubusercontent.com/95964330/164993180-7653680e-7c97-4d86-aac4-7ac4bb871858.png)
1. "Meter" for measurment of the quantum bit. </li> ![image](https://user-images.githubusercontent.com/95964330/164993191-713ae328-4c33-45ce-8788-6b28ec4c8963.png)

### Qubit Copying - NOT ALLOWED!!!
The _no-cloning_ theorem states that the qubits cannot be copied. A simple way of seeing this is that when a qubits is measured, _no information_ about the probability of the _other_ outcome (the extra hidden information in the qubit regarding the _other_ possibility than the one which is obtained) cannot be obtained. If somehow we _can_ copy the qubit.......there remains a possibility to retrieve the _"extra, hidden information"_, indicating that the qubit cannot have been copied in the first place. 

## Quantum Teleportation
To give an overview of the problem at hand - Alice and Bob generated an EPR Pair together, they both get seperated, and Alice has to deliver a qubit to Bob with two conditions on how she can do that - she cannot view the qubit and can only send _classical_ information to Bob.

<img src="https://user-images.githubusercontent.com/95964330/167312994-c528ff60-0ba9-4331-bf52-91f373f8b6d2.png" width=40% height=40%>

As summarized in the figure, the steps she follows are:
1. Alice sends her qubits through a CNOT gate.
2. She sends her first qubit through a Hadamard gate 
3. She performs a measurment of on bot the qubits.
4. Voila!! She knows what operation Bob needs to perform on the third and the last qubit (which can be shown mathematically), so that the qubit returns to its original state, and therefore Alice has successfully transferred the qubit Bob without Bob "seeing" the qubit.

So.....can information be transmitted faster than light??? N..n..not really. The fact that Alice has to send Bob the information of which gate to apply to the last qubit, restricts 'faster than light' communication. Without the classical channel the teleportation does not convey any information at all.

## Quantum Algorithms
How does that class compare with the computations which can be performed using classical logical circuits? The quantum computer _does_ have an upper hand over a classical computer in some class of problems....which are elaborated below.

### Toffoli Gates
Classical gates (made of NAND and NOT) are irreversible, but can be replaced by an equivalent quantum _reversible_ gate known as the Toffoli gate. The Toffoli gate
has three input bits and three output bits - two bits are _control_ bits and one is the _output_ bit, as illustrated below:

<img src="https://user-images.githubusercontent.com/95964330/167313676-adf4aafe-49c2-43c3-a2e3-36e4832b5646.png" width=40% height=40%>

The rule for the Toffoli gate is: The third bit is a target bit that is ﬂipped if both control bits are set to 1, and otherwise is left alone. The toffoli gate can be used to simulate both the NAND gate and the NOT gate - and therefore, all the classical gates. 

### Quantum Parallelism 
Heuristically, and at the risk of over-simplifying, quantum parallelism allows quantum computers to evaluate a function f(x) for many different values of x simultaneously. 
### Deutsch's Algorithm

### The Deutsch-Jozsa Algorithm 

# Linear Algebra 
Since a good understanding of quantum mechanics is based upon a solid understanding of Linear Algebra, here is some basic review of the important concepts in Linear Algebra.

## Vectors and Basic Notations
1. A vectors in Quantum Mechanics is denoted by - <img src="https://user-images.githubusercontent.com/95964330/166400275-267c42c0-960c-439e-8396-9872eb6eeccb.png" width=2.2% height=2.2%>. The zero vector is denoted as **0** (not <img src="https://user-images.githubusercontent.com/95964330/166400403-5da0886d-32a3-4493-915d-de5bcdf0d510.png" width=2.2% height=2.2%>).
2. A vector subspace of a vector space _V_ is a subset _W_ of _V_ such that _W_ is also a vector space, that is, _W_ must be closed under scalar multiplication and addition.
3. Here are some basic notations: 


<img src="https://user-images.githubusercontent.com/95964330/166400521-0ab48ac5-7b8b-4f3d-9d68-0abf13c9f9df.png" width=35% height=35%>

## Bases, Linear Independence and Linear Operators

1. A _spanning set_ is a set of vectors, such that any vector in the subspace can be written as a linear combination of those vectors.
2. A set of _non-zero_ vectors is called _linearly dependent_, if there exists complex numbers such that a non-trivial linear combination of vectors is equal to the _0_ vector. If not, the set of vectors is called _linearly independent_.
3. 






























