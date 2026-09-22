#!/usr/bin/env python
# coding: utf-8

# (sec-numbers)=
# # Encoding numbers
# 
# If a quantum computation involves numbers, first we need to encode them.The situation is not much different from classical computing.  First, we have only finite number of qubits, we cannot encode all numbers.  Secondly, strictly speaking continuous numbers cannot be expressed in digital computers.  In this section, we study how to encode integer numbers and real numbers.

# ## Integers
# 
# Suppose that we encode integers in $n$ qubits. We just use the same encoding scheme as classical encoding.   That is to express intgers in binary and map them to bit string. Recall the inter indexing of the computational basis introduced in {numref}`ssec-notations` which also uses the binary string. Hence, integers from $0$ to $2^n-1$ can be expressed by the computational basis
# 
# $$
# j \quad \Rightarrow \quad |j\rangle_n
# $$
# 
# For example, $151 \Rightarrow |151\rangle_8 = |10010111\rangle$.  You can also encode the same number with more qubits. Using $16$ qubits, $151 \Rightarrow |151\rangle_{16} = |0000000010010111\rangle$.  The lower half of the binary string matches to the 8-qubit expression.
# 
# The following Qiskit example encode 151 in eight qubits.

# In[1]:


from qiskit import *

qr=QuantumRegister(8,'q')
qc=QuantumCircuit(qr)

# create integer 151
qc.x([0,1,2,4,7])

from qiskit.quantum_info import Statevector

Statevector(qc).draw('latex')


# ## Real numbers with floating point arithmetic
# 
# Real numbers are continuous and thus there are uncountable many numbers even upper and lower bounds are limited.  The situation is same in classical computation.  THerefore, we express real numbers approximately using the [*floating-point arithmetic*](https://en.wikipedia.org/wiki/Floating-point_arithmetic) method.  Suppose that we write a real number in a scientific notation *mantissa* $\times$ *scale*, for example in base 10 $0.3452 \times 10^7$.  We can always make the mantissa less than 1 by adjusting the scaling.  We can also make the mantissa integer as $3452 \times 10^3$. 
# Therefore, the scientific notation can be written as integer times scaling.
# Now, we use the similar expression in binary.  Consider a binary fractional number $0.10011 \times 2^{10}$.  The mantissa can be written as 
# 
# $$
# 0.10011 = \frac{1}{2} + \frac{1}{2^4} + \frac{1}{2^5} = \frac{1}{2^5} \left (2^4 \times 1 + 2 \times 1  + 1 \right) =  \frac{1}{2^5} \times 10011
# $$
# 
# Hence, $0.10011 \times 2^{10} = 10011 \times 2^5$.
# 
# In general binary fractional number expressed with $n$ qubits  is written as
# 
# $$
# 0.j_{n-1}\,j_{n-2}\,...\,j_1\,j_0 =  \frac{1}{2^n} \left ( 2^{n-1} j_{n-1} + 2^{n-2} j_{n-2} + \cdots + 2 j_1 + j_0 \right)  = \frac{1}{2^n} \sum_{k=0}^{n-1} 2^k j_k
# $$
# 
# which indicate that the mantissa can be written as an integer divided by $2^n$.
# Real numbers smaller than 1 can be approximately encoded with $n$ qubit as integer devided by $2^n$.  In practice, $0<x<1$ is encoded as $|2^n x\rangle = |j\rangle_n$.  At the end of computation, we can find $x$ by computing $j/2^n$ on a classical computer. 
# 
# Using 3 qubits, we can encode eight real numbers, 
# $\frac{0}{8} = 0$, $\frac{1}{8} = 0.125$, $\frac{2}{8} = 0.25$, $\frac{3}{8} = 0.375$,
# $\frac{4}{8} = 0.5$, $\frac{5}{8}=0.625$, $\frac{6}{8}=0.75$, $\frac{7}{8}= 0.875$. The gap between two adjacent values is $0.125$, too big as approximated real number.  However, for some applications, this is good enough. See for examples, {numref}`sec-qft` and {numref}`sec-qpe`. If $64$ qubits are available, we can encode $2^{64} = 18446744073709551616$ different real numbers between 0 and 1.  That means the gap is approximately $5.42101086 \times 10^{-20}$, which is small enough for most of applications.  Unfortunately, the currently available quantum computer do not have enough qubits to use floating point arithmetic.
# 

# In[2]:


from qiskit import *

qr=QuantumRegister(3,'q')
qc=QuantumCircuit(qr)

# create |101>
qc.x([0,2])

# find corresponding real number
# extract output
psi=Statevector(qc).to_dict()
psi=list(psi.keys())[0]
x = int(psi[2])/2. + int(psi[1])/2**2.+ int(psi[0])/2**3.

print("|{0:s}> corresponds to x={1:5.3f}".format(psi,x))


# ## Real numbers encoded in coefficients
# 
# Unlike classical bits, quantum states naturally contains continuous numbers in superposition states.  Consider general qubit state
# 
# $$
# |\psi\rangle = \cos\left(\frac{\pi x}{2}\right) |0\rangle + \sin\left(\frac{\pi x}{2}\right) e^{2\pi y} |1\rangle
# $$
# 
# where $0<x<1$ and $0<y<1$.  We can store two real numbers $x$ and $y$ in a single qubit. Their value can be determined by the method discussed in {numref}`sec-state-tomography`.  It is relatively easy to encode and decode the data.  However, it is not trivial to use $x$ and $y$ in actual calculation.  However, this method works in certain application nicely, especially the real numbers represent angles.

# let us calculate $\cos(A)\cos(B)\cos(C),\, \cos(A)\cos(B)\sin(C),\, \cdots\, \sin(A)\sin(B)\sin(C)$ all at once where $0<A, B, C<\pi/2$. Using three qubits, we construct a state
# 
# $$
# \begin{align}
# |\psi\rangle &=\left(\cos(A)|0\rangle + \sin(A)|1\rangle\right) \otimes \left(\cos(B)|0\rangle + \sin(B)|1\rangle\right) \otimes \left(\cos(C)|0\rangle + \sin(C)|1\rangle\right) \\
# &= \cos(A)\cos(B)\cos(C)|000\rangle + \cos(A)\cos(B)\sin(C)|001\rangle + \cdots + \sin(A)\sin(B)\sin(C)|111\rangle
# \end{align}
# $$
# 
# By measuring all qubits, we obtain probabilities $p_{000}, \cdots, p_{111}$.  Then,
# $\cos(A)\cos(B)\cos(C) = \sqrt{p_{000}}, \cdots $.  Now we calculated all combination of three trig functions simultaneously.

# In[3]:


import numpy as np
from qiskit import *

cr=ClassicalRegister(3,'c')
qr=QuantumRegister(3,'q')
qc=QuantumCircuit(qr,cr)

A=np.pi/3
B=np.pi/4
C=np.pi/6

qc.ry(2*A,0)
qc.ry(2*B,1)
qc.ry(2*C,2)

qc.measure([0,1,2],[0,1,2])

# Chose a general quantum simulator without noise.
# The simulator behaves as an ideal quantum computer.
backend = Aer.get_backend('qasm_simulator')

# set number of tries
nshots=8192

# execute the quantum circuit and store the outcome
job = backend.run(qc,shots=nshots)

# extract the result
result = job.result()

# count the outcome
counts = result.get_counts()

for k in counts.keys():
    sqrtp = np.sqrt(counts[k]/nshots)
    term=(k.replace('0',' cos')).replace('1',' sin')
    print("{0:s}  = {1:3.3f}".format(term,sqrtp))


# In[ ]:




