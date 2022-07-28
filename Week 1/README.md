# Introduction to QC and Linear Algebra
## What is a Quantum Bit?
_Quantum Bit_ (or _qubit_ in short) is analogous to the classical bit, which is the fundamental unit of information used in most computers today - but the important distinction between them comes in how the information is _stored_ not _measured_. While a classical bit can only store a _0_ or a _1_ the quantum bit is stored as a linear combination of _computational basis states_. ( $|0\rangle$ and $|1\rangle$  )

$$|\psi\rangle = \alpha |0\rangle + \beta |1\rangle$$

The linear combination may be written in terms of parameters as given below:

$$|\psi\rangle = e^{i\gamma} \left(\cos\frac{\theta}{2}|0\rangle + e^{i\phi} sin\frac{\theta}{2}|1\rangle\right)$$

and can be represented on a sphere as shown (Bloch Sphere):

<img src="https://user-images.githubusercontent.com/95964330/164911401-18eaa4fc-23b2-4623-a6f0-2630dfee2f4b.png" width=20% height=20%>

## Multiple Qubits
Let us consider the case of two Qubits. The system can be expressed as a superposition (linear combination) of 4 _computational basis states_ (in simple words 4 different possibilities that the system can "collapse" into) - $|00\rangle, |01\rangle, |10\rangle, |11\rangle$ ). An important two-qubit state is a Bell State or EPR state:

$$ \frac{|00\rangle + |11\rangle}{\sqrt2}$$

It has the property that upon measuring the value of the first qubit (which can be either 0 or 1 with the probability $\frac{1}{2}$ for each outcome), the outcome of the second qubit is already determined. A strong correlation exists in a Bell state than could ever exist in a classical system.

## Quantum Computation
### Single Qubit Gates
The only single bit gate one can think of in a classical system is the NOT gate - which convert _0_ state to _1_ state and vice-versa. An analogous quantum NOT gate also exists ( named the X gate) - along with an infinite number of other one qubit gates!!!
One property of the single qubit gates, that I find worth mentioning is that they act _linearly_ (meaning, $|\psi\rangle = \alpha |0\rangle + \beta |1\rangle$  will change to $|\psi\rangle = \alpha |1\rangle + \beta |0\rangle$ ) - non-linear behavious of operators can lead to paradoxes such as - time travel, faster-than-light-communication etc; and that they are _Unitary_ ($U^{\dagger}U = I$)

Quantum Operators can be thought of as matrices acting on the vector $[\alpha, \beta]^{T}$. For example, the NOT operator can be thought of as the  matrix:

$$\begin{equation}
 \begin{bmatrix}
     0 & 1 \\ 
     1 & 0
 \end{bmatrix}
\end{equation}$$

The operation of which can be seen as: ![image](https://user-images.githubusercontent.com/95964330/164912741-f88a8066-09cb-4ca6-8a89-b787ed49870a.png)


Other similar qubit operators are:

![image](https://user-images.githubusercontent.com/95964330/164912658-67ff1906-9302-4fd0-ad4c-58e36efc1059.png) - the Z gate

![image](https://user-images.githubusercontent.com/95964330/164912666-d40c7ca7-e7fb-4559-aff2-acf71fea4742.png) - the _Hadamard gate_

The following image summarises the action of some single-qubit operators:

<img src="https://user-images.githubusercontent.com/95964330/164912718-87d63d1e-2115-46ff-a5f8-9ea860a76961.png" width=50% height=50%>

Interestingly, _any_ set of single-quibit gates can be constructed out of a _finite- set of qantum gates - not always exactly, but to an _arbitrarily_ good precision; using the decomposition: <img src="https://user-images.githubusercontent.com/95964330/164959380-c167ae2f-2cee-4b39-8015-1c7001f01f0d.png" width=50% height=50%>

### Multiple Qubit Gates
The prototypical multi-qubit logic gate is the _controlled_-NOT or _CNOT_ gate - the first quibt decides whether the second qubit will be flipped or not. the second qubit will be flipped only if the first qubit (_control qubit_) is set to 1. The action of the gate can be summarised as: $|A, B\rangle \implies |A, B \oplus A\rangle$ and can be represented by the matrix:

<img src="https://user-images.githubusercontent.com/95964330/164959626-410d1480-5b14-4615-8e48-73e5d12a72ed.png" width=15% height=15%>

Just like in the glassical gates, the _NAND_ gate can be used to build _every_ other classical gate, in qubit-gates, a combination of the _CNOT_ gate and _single - qubit_ gates can represent _any_ multiple-qubit gate.

One important distinction between classical gates and qubit gates is that there is an irreversible loss of information when classical gates are used. For example - an output _0_ of the _AND_ gate can come from either of the following combinations - (0,1), (1,0), (0,0) - meaning, we cannot retrieve back the input by looking at the output. Surprisingly, qubit-gates, by their representation using _Unitary matrices_ (which are invertible), are also invertible - i.e. the input can be uniquely determined by looking at the output.

### Measurments in bases other than the computational bases
Note that the states $|0\rangle$ and $|1\rangle$ are one of many possible choice of basis states.  It is possible to express a state as a linear comination of an arbitrary basis set ( say, $|+\rangle$ and $|-\rangle$). It would help if the  new basis set was orthonormal. In that case the square of the modulus of the coeffecient of each basis would be the probability of that set of outcomes of the set of qubits on measurement.

### Quantum circuits
A number of features of the quantum circuits, which differentiates it from the conventional circuits are:
<ol>
  <li> Quantum circuits do not allow loops/ feedback.</li>
  <li> They do not allow FANIN - several wires being joined together and an bitwise OR of the inputs being shown as output.</li>
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
Heuristically, and at the risk of over-simplifying, quantum parallelism allows quantum computers to evaluate a function $f(x)$ for many different values of x simultaneously. Suppose $f(x): \{ 0, 1 \} \rightarrow \{ 0, 1 \}$ is a function with a one-bit domain and range. With an appropriate sequence of logic gates it is possible to transform this state into $|x, y \oplus f(x)\rangle$. Let $|x\rangle$ be $\frac{|0\rangle + |1\rangle}{\sqrt2}$ and y be $|0\rangle$, the state in the second qubit will be:

$$ \frac{|0,f(0)\rangle + |1,f(1)\rangle}{\sqrt2}$$

Which means, we have information about $f(0) and f(1) $ in a single circuit, unlike in the case of classical circuit, where multiple circuits each built to compute $f(x)$ are executed simultaneously.

### Deutsch's Algorithm
<img src = "https://user-images.githubusercontent.com/95964330/181414495-0d7f1974-3069-478a-9000-0fd3968802ee.png" width = 400>

$$ |\psi_1\rangle = \[ \frac{|0\rangle + |1\rangle}{\sqrt2} \] \[ \frac{|0\rangle - |1\rangle}{\sqrt2} \]$$

$$ |\psi_2\rangle = \pm \[ \frac{|0\rangle + |1\rangle}{\sqrt2} \] \[ \frac{|0\rangle - |1\rangle}{\sqrt2} \]$$

if $f(0) = f(1)$

$$ |\psi_2\rangle = \pm \[ \frac{|0\rangle - |1\rangle}{\sqrt2} \] \[ \frac{|0\rangle - |1\rangle}{\sqrt2} \]$$

if $f(0) = f(1)$

On applying Hadamard gate to first qubit,

$$ |\psi_3\rangle = |f(0) \oplus f(1)\rangle \[ \frac{|0\rangle - |1\rangle}{\sqrt2} \]$$

On measuring, we get the value of $f(0) \oplus f(1)$ with unity probability.

> This is very interesting indeed: the quantum circuit has given us the ability to determine a global property of f(x), namely , using only one evaluation of f(x)! This is faster than is possible with a classical apparatus, which would require at least two evaluations.


### The Deutsch-Jozsa Algorithm 

It is used to determine whether f(x) is constant for all values of x, or else f(x) is balanced, that is, equal to 1 for exactly half of all the possible x, and 0
for the other half.

<img src = "https://user-images.githubusercontent.com/95964330/181415965-b8360430-4509-4c46-91d0-a667ab48aa01.png" width = 400>

On applying the Hadamard gate:

$$ |\psi_1\rangle = \sum_{x} \frac{|x\rangle}{\sqrt{2^n}} \[ \frac{|0\rangle - |1\rangle}{\sqrt2} \]$$

On applying the $U_f$ gate:

$$ |\psi_2\rangle = \sum_{x} \frac{(-1)^{f(x)}|x\rangle}{\sqrt{2^n}} \[ \frac{|0\rangle - |1\rangle}{\sqrt2} \]$$

On applying the Hadamard gate:

$$ |\psi_3\rangle = \sum_{x} \frac{(-1)^{x \cdot z + f(x)}|x\rangle}{\sqrt{2^n}} \[ \frac{|0\rangle - |1\rangle}{\sqrt2} \]$$

On measuring:

> 1. If all query registers read 0, then f(x) is constant.
> 2. If none of the query registers read 0, then f(x) is balanced.

## The postulates of quantum mechanics

### State space

Associated to any isolated physical system is a complex vector space with inner product (that is, a Hilbert space) known as the state space of the system. The system is completely described by its state vector, which is a unit vector in the system’s state space.

### Evolution

The evolution of a closed quantum system is described by a unitary transformation. That is, the state $|\psi\rangle$ of the system at time $t_1$ is related to the
state $|\psi'\rangle$ of the system at time $t_2$ by a unitary operator U which depends only on the times $t_1$ and $t_2$.

$$ |\psi'\rangle =  U|\psi\rangle$$

### Quantum measurement

Quantum measurements are described by a collection {$M_m$} of measurement operators. These are operators acting on the state space of the system being measured. The index m refers to the measurement outcomes that may occur in the experiment. If the state of the quantum system is $|\psi\rangle$ immediately before the measurement then the probability that result m occurs is:

$$ p(m) = \langle \psi|M_m\dagger M_m|\psi \rangle$$

# Implementation

No programs were given for the $1^{st}$ week.




































