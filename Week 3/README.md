# The Last Dance with QCQI

## Quantum Fourier Transform
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

If x = $j_1j_2j_3...j_n$ as represented in binary, $\frac{x}{2^k} = j_1j_2...j_{n-k}.j_{n-k+1}...j_n$ in binary (by shifting the bits), and, $e^{i2\pi\frac{x}{2^k}}$ =  $e^{i2\pi j_1j_2...j_{n-k}.j_{n-k+1}...j_n}$ = $e^{i2\pi 0.j_{n-k+1}...j_n}$ (as $e^{i2\pi j_1j_2...j_{n-k}.j_{n-k+1}...j_n}$ = $e^{i2\pi j_1j_2...j_{n-k} + 0.j_{n-k+1}...j_n}$ = $(1)e^{i2\pi 0.j_{n-k+1}...j_n}$)

## Quantum Phase Estimation 


## Implementation
The following programs have been implemented for this week.

1. Quantum Fourier Transform
2. Quantum Phase Estimation
3. Shor's Algorithm
4. Grover's Algorithm
