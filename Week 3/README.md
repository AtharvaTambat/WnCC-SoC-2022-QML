# The Last Dance with QCQI :dancer:

## Quantum Fourier Transform :atom:
The discrete Fourier transform is usually described as transforming a set $x_0,...,x_{N−1}$ of N complex numbers into a set of complex numbers $y_0,...,y_{N−1}$ defined by:

$$y_k \equiv \frac{1}{\sqrt{N}}\sum ^{j = N-1} _{j=0} e^\frac{2\pi ijk}{N} x_j$$

Similarly, the Quantum Fourier Transform transforms the state

$$ |k\rangle \rightarrow \frac{1}{\sqrt{2^n}}\sum ^{j = 2^n-1} _{j=0} e^\frac{2\pi ijk}{2^n} |k\rangle $$

One can think of Quantum Fourier Transform as change of basis. In the computational basis, we store numbers in binary using the states $|0\rangle$ and $|1\rangle$. In the Fourier basis, we store numbers using different rotations around the Z-axis. Counting in computational basis will be represented by bit flips of consequent qubits, while counting in Fourier basis is denoted by rotation of vector in the X-Y plane on the Bloch Sphere.

Classically, the fast Fourier transform takes roughly $N log(N) = n2^n$ steps to Fourier transform N = 2n numbers. On a quantum computer, the Fourier transform can be accomplished using about $log^2(N) = n^2$ steps, an exponential saving! But, the catch here is that the operations are performed on a "hidden" superposition and the the results of such a calculation are not available to us if we go about it in a straightforward manner.

Nevertheless, problems like the Deutsch’s problem, and Shor’s algorithms for discrete logarithm and factoring, can be solved effeciently using QFT.

With a little algebra the quantum Fourier transform can be given the following useful product representation:

$$ \begin{aligned}
QFT_{2^n}\vert x \rangle = 
& \frac{1}{\sqrt{2^n}}
\left(\vert0\rangle + e^{\frac{2\pi i}{2}x} \vert1\rangle\right) 
\otimes
\left(\vert0\rangle + e^{\frac{2\pi i}{2^2}x} \vert1\rangle\right) 
\otimes  
\ldots
\otimes
\left(\vert0\rangle + e^{\frac{2\pi i}{2^{n-1}}x} \vert1\rangle\right) 
\otimes
\left(\vert0\rangle + e^{\frac{2\pi i}{2^n}x} \vert1\rangle\right) 
\end{aligned} $$

If x = $j_1j_2j_3...j_n$ as represented in binary, $\frac{x}{2^k} = j_1j_2...j_{n-k}.j_{n-k+1}...j_n$ in binary (by shifting the bits), and, $e^{i2\pi\frac{x}{2^k}}$ =  $e^{i2\pi j_1j_2...j_{n-k}.j_{n-k+1}...j_n}$ = $e^{i2\pi 0.j_{n-k+1}...j_n}$ (as $e^{i2\pi j_1j_2...j_{n-k}.j_{n-k+1}...j_n}$ = $e^{i2\pi( j_1j_2...j_{n-k} + 0.j_{n-k+1}...j_n)}$ = $(1)e^{i2\pi 0.j_{n-k+1}...j_n}$)

Therefore, the circuit for the same is:

![image](https://user-images.githubusercontent.com/95964330/180614388-fb9f8262-df01-41be-8831-7d32f12e6e61.png)

where,

$$R_k \equiv \begin{bmatrix}
1&0 \\
0&e^\frac{2\pi i}{2^k} \\
\end{bmatrix}$$

## Quantum Phase Estimation :electron:

The Quantum Phase Estimation is one of the uses of the QFT to guess the global phase ($\alpha$) that a Unitary matrix U adds to its eigenvector $|\psi\rangle$

$$ U|\psi\rangle = e^{i\alpha}|\psi\rangle $$

The circuit for phase estimation, is as follows:
![image](https://user-images.githubusercontent.com/95964330/180615245-8eb67782-461e-41d1-af71-ccfd2596ab79.png)

1. **Setup:** first register has qubits $|\psi_0\rangle = \lvert 0 \rangle^{\otimes n} \lvert \psi \rangle$
2. **Superposition:** After application of Hadamard gates to all the qubits of the first register,
 
 $$ |\psi_1\rangle = {\frac {1}{\sqrt{2^{n}}}}\left(|0\rangle +|1\rangle \right)^{\otimes n} \lvert \psi \rangle $$
 
3. **Controlled Uoperations:** 
If 

$$ U|\psi\rangle = e^{2\pi i \phi}|\psi\rangle $$ 

if the controller qubit = $|1\rangle$

then, the state in the quantum circuit becomes:

$$\begin{aligned}
|\psi_{2}\rangle & =\frac {1}{2^{\frac {n}{2}}} \left(|0\rangle+{e^{\boldsymbol{2\pi i} \phi 2^{n-1}}}|1\rangle \right) \otimes \cdots \otimes \left(|0\rangle+{e^{\boldsymbol{2\pi i} \phi 2^{1}}}\vert1\rangle \right) \otimes \left(|0\rangle+{e^{\boldsymbol{2\pi i} \phi 2^{0}}}\vert1\rangle \right) \otimes |\psi\rangle\\\\
& = \frac{1}{2^{\frac {n}{2}}}\sum _{k=0}^{2^{n}-1}e^{\boldsymbol{2\pi i} \phi k}|k\rangle \otimes \vert\psi\rangle
\end{aligned}$$

4. **Inverse Quantum Fourier Transform:** The above expression looks similar to the one obtained after QFT of $|x\rangle$, so the logical thing would be to apply inverse QFT, and on doing so, we find that $x = 2^n \phi$. So, we get the binary value of $2^n \phi$ in the first register, with high probability, while the state in second register is unaffected.

$$ |\psi_4\rangle = | 2^n \phi \rangle \otimes | \psi \rangle $$

## Grover's Search Algorithm :eyeglasses:

The Grover's search is used to carry out an unstructured search. Say, there is a function $f(x)$ which is equal to 1 for a binary input $x_0$, and 0 for all other binary inputs (given the number of bits is fixed), Grover search can look for $x_0$ with $O(\sqrt{N})$ instead of the classical algorithm, which takes $O(N)$ time - having to go through each element one-by-one.

The following is the circuit for implementing Grover's search:

![image](https://user-images.githubusercontent.com/95964330/180616162-08083c2a-b538-43c5-a108-226d44b74224.png)
![image](https://user-images.githubusercontent.com/95964330/180616183-fa9050eb-35b2-4bd2-9a0a-623f89a5f8c4.png)

1. **Superposition:** After application of Hadamard gates to all the qubits of the first register,
 
 $$ |\psi_1\rangle = {\frac {1}{\sqrt{2^{n}}}}\left(|0\rangle +|1\rangle \right)^{\otimes n} \lvert \psi \rangle $$
 
2. **Oracle:** We, now have to somehow implement such a gate, which inverts the phase of that computational basis, in the superposition, for which f(x) = 1

$$U_\omega|x\rangle = (-1)^{f(x)}|x\rangle$$

3. **Diffuser:** The "Diffuser" is the gate $U_s = \left(2|s\rangle\langle s| - 1\right) = H^{\otimes n}(2|0\rangle \langle0| - I)H^{\otimes n}$, where $|s\rangle$ is the uniform superposition of all possible computational basis with the given number of bits.

What the repeating the above steps does is that, it brings the uniform superposition closer and closer to the requires state $x_0$ with each iteration i.e. it increase the coeffecient of the correct computational basis ($x_0) while decreasing the coeffecients of the rest in the superposition - increasing the probability of getting the right answer at the end.

## Shor's Algorithm

Shor's Algorithm solves the problem of period finding. It basically finds the period of $f(x) = a^x(modN)$. 
![image](https://user-images.githubusercontent.com/95964330/180619599-bc574da8-42f3-4f00-8ce3-045ad77f6b0b.png)

1. **Superposition:** After application of Hadamard gates to all the qubits of the first register,
 
 $$ |\psi_1\rangle = {\frac {1}{\sqrt{2^{n}}}}\left(|0\rangle +|1\rangle \right)^{\otimes n} \lvert 1 \rangle $$
 
2. The lower register has the value $|1\rangle$. $|1\rangle$ is a superposition of $|u_s\rangle$'s, which is defined as follows:

$$\begin{aligned}
|u_s\rangle &= \tfrac{1}{\sqrt{r}}\sum_{k=0}^{r-1}{e^{-\tfrac{2\pi i s k}{r}}|a^k \bmod N\rangle}\\ 
\end{aligned}$$

We also notice, that the sum of all such $|u_s\rangle$'s is $|1\rangle$:

$$\tfrac{1}{\sqrt{r}}\sum_{s=0}^{r-1} |u_s\rangle = |1\rangle $$

Also notice, that $U$, such that $U|y\rangle \equiv |ay \bmod N \rangle$, $|u_s\rangle$ is the eigenvector of U:

$$U|u_s\rangle = e^{\tfrac{2\pi i s}{r}}|u_s\rangle  $$

3. **Application of U gates:** Application of controlled U's in such a fashion actually implements $U^j|\phi\rangle$, where $j$ is the number whose binary equivalent is the computational basis in the first register and $|\phi\rangle$ is the state of the second register.So the state of qubits in the first register after application of gates is $|\psi\rangle$

$$\begin{equation}
	|\psi\rangle = \frac{1}{\sqrt{2^n}}\sum_{j=0} ^{2^n - 1} |j\rangle U^j|1\rangle = \frac{1}{\sqrt{2^n}}\sum_{j=0} ^{2^n - 1} |j\rangle |x^jmodN\rangle
\end{equation} $$

It can be proved that

$$\frac{1}{\sqrt{r}}\sum_{s=0} ^{r-1} e^\frac{2 \pi isk}{r} |u_s\rangle = |x^k modN\rangle $$

Putting the previous two equations together, the state after application of U gates:

$$	|\psi\rangle = \frac{1}{\sqrt{r2^n}} \sum_{j=0} ^{2^n - 1}  \sum_{s=0} ^{r-1} |j\rangle e^\frac{2 \pi isj}{r} |u_s\rangle  $$

4. **Inverse Fourier Transform:** The previous equation looks very similar to the QFT of *some* state. On applying inverse Fourier Transform, we get:

$$\frac{1}{\sqrt{r}} \sum_{s = 0} ^{r-1} |\frac{s}{r}\rangle |u_s\rangle $$

5. **Measurement:** On measuring the first register, we will measure the binary value of $\frac{s}{r}$ for some $s \in [0, r) $. By applying continued fractions algorithm, we can guess the denominator of the fraction, which is the required period of the function $f(x) = a^x(mod N)$

Applying classical algorithm for finding the factors once the period is obtained.

## Implementation
The following programs have been implemented for this week.

1. [Quantum Fourier Transform](https://github.com/AtharvaTambat/WnCC-SoC-2022-QML/blob/main/Week%203/Quantum_Fourier_Transform.ipynb)
2. [Quantum Phase Estimation](https://github.com/AtharvaTambat/WnCC-SoC-2022-QML/blob/main/Week%203/Quantum_Phase_Estimation.ipynb)
3. [Shor's Algorithm](https://github.com/AtharvaTambat/WnCC-SoC-2022-QML/blob/main/Week%203/Shor's_Algorithm.ipynb)
4. [Grover's Algorithm](https://github.com/AtharvaTambat/WnCC-SoC-2022-QML/blob/main/Week%203/Grover's_Search_Algorithm.ipynb)

