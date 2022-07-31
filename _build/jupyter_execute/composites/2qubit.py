#!/usr/bin/env python
# coding: utf-8

# (sec-2qubits)=
# # Two qubits
# 

# ## Hilbert space and computational basis
# 
# First, let us recall that a single qubit is in a two-dimensional Hilbert space $\mathbb{C}^2$ and the computational basis vectors $0\rangle$ and $|1\rangle$ span the space. Now we consider two qubits $q_0$ and $q_1$. The composite system lives in a four-dimensional Hilbert space.  The dimension $4$ is not $2+2$ but $2 \times 2$.  We write it $\mathbb{C}^2 \otimes \mathbb{C}^2$ where $\otimes$ indicates *tensor product*.  This mathematical structure is very important. Using the computational basis of each $\mathbb{C}^2$, we can construct four *computational basis* vectors for the composite system as products $|q_1\rangle \otimes |q_0\rangle$:
# 
# $$
# |00\rangle \equiv |0\rangle \otimes |0\rangle, \quad |01\rangle \equiv |0\rangle \otimes |1\rangle, \quad |10\rangle \equiv |1\rangle \otimes |0\rangle, \quad |11\rangle \equiv |0\rangle \otimes |0\rangle.
# $$(computational-basis-q2)
# 
# The physical meaning of each basis vector is clear. For example, $|01\rangle$ means $q_0$ is in $\rangle$ and $q_1$ in $|0\rangle$.
# 
# Other basis sets are also used.  The $xx$ basis uses $|\pm\rangle$ for both qubits
# 
# $$
# |++\rangle \equiv |+\rangle \otimes |+\rangle, \quad |+-\rangle \equiv |+\rangle \otimes |-\rangle, \quad |-+\rangle \equiv |-\rangle \otimes |+\rangle, \quad |--\rangle \equiv |-\rangle \otimes |-\rangle
# $$
# 
# The mixed basis in which $q_0$ and $q_1$ use different basis kets is also allowed.
# 
# $$
# |0+\rangle \equiv |0\rangle \otimes |+\rangle, \quad |0-\rangle \equiv |0\rangle \otimes |-\rangle, \quad |1+\rangle \equiv |1\rangle \otimes |+\rangle, \quad |1-\rangle \equiv |1\rangle \otimes |-\rangle
# $$
# 

# **Exercise** {numref}`%s <sec-2qubits>`.1    Show that the above basis sets are all orthonormal.

# ## Superposition states
# 
# The state of two-qubit system is expressed as 
# 
# $$
# c_{00} |00\rangle + c_{01} |01\rangle + c_{10} |10\rangle + c_{11} |11\rangle.
# $$
# 
# What does this state physically means?  To see that, we assume that Alice has qubit $q_0$ and Bob has $q_1$.  They are separated by a large distance.  Even when they are far apart, the above state is still valid. Alice can measure her qubit but not Bob's qubit.  Similarly, Bob can measure his qubit but not Alice's.  This type of measurement is known as *local measurement*.  Now Alice measures her qubit $q_0$ before Bob measures $q_1$.  Suppose that the outcome is $|0\rangle$.  The state now collapses to 
# 
# $$
# \frac{1}{N} (c_{00} |00\rangle + c_{10} |10\rangle) = \left(c_0 |0\rangle + c_1|1\rangle\right) \otimes |0\rangle .
# $$
# 
# where $N = \sqrt{|c_{00}|^2 + |c_{01}|^2}$, $c_0=c_{00}/N$, and $c_1=c_{10}/N$.  After the measurement, Alice's qubit is now in  definite state $0\rangle$ but Bob's qubit remains in a superposition state.  Next, Bob measures his qubit and found it in $|1\rangle$.  Then, the state further collapses to $|1\rangle \otimes |0\rangle$.  
# 
# Recall that the outcome of quantum measurement is completely random and there is no way to predict it.  You can calculate the probability to find each state based on the Born rule.  The probability that Alice obtain $|0\rangle$ is $p_A(0) = |c_{00}|^2 + |c_{10}|^2$ because Alices qubit is $|0\rangle$ in $|00\rangle = |0\rangle \otimes |0\rangle$ and $|10\rangle = |1\rangle \otimes |0\rangle$. In other words, when Alice obtained $|0\rangle$, Bob's qubit can be still $|0\rangle$ or $|1\rangle$, hence we need to take into account both. 
# 
# The probability that Bob gets $|1\rangle$ after Alice get $|0\rangle$ is $p_B(1|0)=|c_1|^2$, which is the [*conditional probability*](https://en.wikipedia.org/wiki/Conditional_probability) after Alice gets $|0\rangle$. The net probability to find $|10\rangle$ is 
# 
# $$
# p_A(0) p_B(1|0) = \left(|c_{00}|^2 + |c_{01}|^2)\right) |c_1|^2 = |c_{10}|^2
# $$
# 
# which is the probability to obtain $|10\rangle$.  , The Born rule worked well for the composite case.

# **Exercise**  {numref}`%s <sec-2qubits>`.1 Suppose that Alice measured her qubit before Bob did and got $|1\rangle$.  Bob measured his qubit after Alice and obtained $|1\rangle$.  What is the state after their measurement and what is the probability to get it?

# Now an important question arises. If Bob measures before Alice, does the probability remain the same?
# 
# Suppose that Bob measured before Alice and got $|1\rangle$.  The probability that happens is $p_B(1)=|c_{10}|^2 + |c_{11}|^2$, which is different from the previous case despite that Bob gets the same outcome.   This is weird but let us move on.  After Bob's measurement the state collapse to
# 
# $$
# \frac{1}{N} (c_{10} |10\rangle + c_{11} |11\rangle) = |1\rangle \otimes \left(c_0 |0\rangle + c_1|1\rangle\right)
# $$(superposition-q2)
# 
# where $N = \sqrt{|c_{10}|^2 + |c_{11}|^2}$, $c_0=c_{10}/N$, and $c_1=c_{11}/N$.
# Next, Alice measured her qubit and obtained $0\rangle$ with the probability $p_A(0|1)=|c_0|^2$.  The final state is $|10\rangle$.  The net probability is
# 
# $$
# p_B(1) p_A(0|1) = \left(|c_{10}|^2 + |c_{11}|^2)\right) |c_1|^2 = |c_{10}|^2
# $$
# 
# in agreement with the previous case.  This agreement is guaranteed by the [*Bayes' theorem*](https://en.wikipedia.org/wiki/Bayes%27_theorem) $p_A(x)p_B(y|x) = p_B(y) p_A(x|y)$.
# 
# While the net probability does not depend on the order of the measurement, the probabilities of individual observers experience depend on it. Despite that Alice and Bob are separated by a far distance, the act of Alice on her qubit changed the state of Bob's qubit instantaneously.  This conclusion is quite counter intuitive and needs to be examined more carefully.

# ## Product states
# 
# Let us consider a special case where the two qubit state is 
# 
# $$
# |10\rangle = |1\rangle \otimes |0\rangle
# $$(product10)
# 
# that is $c_{00}=c_{01}=c_{11}=0$ and $c_{10}=1$ in Eq {eq}`superposition-q2`.  Alice always finds her qubit in $|0\rangle$ (probability=1) and Bob always find his in $|1\rangle$ without exception (probability=1).   In this case, the order of measurement does not affect the individual measurements. There seems no controversy.
# 
# Next we consider
# 
# $$
# |+-\rangle = \frac{1}{\sqrt{2}} \left(|0\rangle + |1\rangle\right ) \otimes \frac{1}{\sqrt{2}} \left(|0\rangle - |1\rangle\right ) = \frac{1}{2} \left(|00\rangle - |01\rangle + |10\rangle - |11\rangle \right).
# $$(product+-)
# 
# This state is closer to the general case {eq}`superposition-q2`.  However, the probability that Alice gets $|0\rangle$ is $\frac{1}{2}$ and the probability Bob gets $|1\rangle$ is also $\frac{1}{2}$ regardless of who measures first.
# 
# The state of the composite systems in these two examples can be written as *product state* $|q_1\rangle \otimes |q_0\rangle$.  In Eq. {eq}`product10`, $|q_0\rangle = |0\rangle$ and $|q_1\rangle = |1\rangle$.  In Eq. {eq}`product+-`, $|q_0\rangle = |-\rangle$ and $|q_1\rangle = |+\rangle$.  When a composite system is in a product state, the measurements of $q_0$ and $q_1$ are completely independent and thus the order does not matter.

# ## Entangled states
# 
# When the state of a composite system cannot be written in a form of product $|q_1\rangle \otimes |q_0\rangle$, we say that the system is *entangled*.  [*Quantum entanglement*](https://en.wikipedia.org/wiki/Quantum_entanglement) is unique to quantum systems.
# When the qubits are entangled, they are not independent. Measurement on one qubit change the state of the other qubit.  
# 
# A pair of qubits interact at a certain place and an entangle state
# 
# $$
# \frac{1}{\sqrt{2}} \left(|01\rangle + |10\rangle\right)
# $$(01+10)
# 
# is formed.  Alice takes $q_0$ and travels to a distant place with it. Bob takes the other qubit and travels in the opposite direction.  Alice and Bob are separated by a large distance.
# 
# The entangled state {eq}`01+10` indicates that Alice's qubit is either $|0\rangle$ or $|1\rangle$ and so is Bob's.  When Alice's measurement results in $|0\rangle$, then Bob's qubit necessarily in $|1\rangle$ since $|00\rangle$ is absent.  On the other hand, if Alice finds $|1\rangle$ then Bob's qubit must be in $|0\rangle$.   Alice immediately knows what Bob's will find.  Hence, their measurement is perfectly correlated.  
# 
# This correlation is not necessarily controversial since classical correlation exits.  Consider a pair of grabs.  Each side of the grab is placed in a separate box.  Alice took a box and Bob the other.  They don't know which side of the grab is in their of box.  They open the box at their home.  When Alice finds the left grab, the Bob must find the right grab.  This is an example of perfect classical correlation.  When Bob opened the box before Alice, the outcome remain the same.
# 
# The quantum correlation by entanglement seems the same as the classical case but it is actually quite different. Before measurement neither spin has a definite state.  Both qubits are mixture of $|0\rangle$ and $|1\rangle$.  Alice's measurement destroys the mixture of Bob's qubit *instantaneously* over *distance*.  How can Alice's action on her qubit changes the state of Bob's qubit instantaneously over an arbitrarily long distance?   This is known as [*EPR paradox*](https://en.wikipedia.org/wiki/EPR_paradox).  Einstein called it "Spooky action at a distance" and claimed that the theory of quantum mechanics is incomplete.  However, every experimental observation is found to be consistent with the standard theory of quantum mechanics.  In the next section, we discuss more about it. 
# 
# Once David Mermin explained the common attitude toward the theory of quantum mechanics as "Shut up and calculate". {cite}`Mermin1989`.   For the moment, we set aside the incomprehensible aspect of quantum entanglement and just accept the extraordinary properties of quantum entanglement.  It turns out that entanglement carries very useful properties that classical physics cannot offer. We exploit them in quantum computation.  In fact, the success of quantum computation relies on quantum entanglement.

# ## Bell basis
# 
# The Hilbert space of two qubits is four-dimensional and spanned by four basis vectors.  The computational basis {eq}`computational-basis-q2` is based on the product states.  In many cases, basis set based on entangled states is desired.  The most popular entangled basis is *Bell basis* defined by four Bell states:
# 
# $$
# \begin{align}
# |\Phi^{\pm}\rangle &= \frac{1}{\sqrt{2}} \left(|00\rangle \pm |11\rangle\right) \\
# |\Psi^{\pm}\rangle &= \frac{1}{\sqrt{2}} \left(|01\rangle \pm |10\rangle\right)
# \end{align}
# $$
# 
# Among them, $|\Psi^{-}\rangle$, known as *singlet state*, plays an important role in quantum information theory. 
# 
# No entangled state can be created by local transformation (one-qubit gates). We must use a two-qubits gate such as controlled-$X$. The following Qiskit example generates $\Phi^+\rangle$ and |\Pis^+\rangle$.

# In[1]:


from qiskit import *

qr=QuantumRegister(2,'q')
qc=QuantumCircuit(qr)

# generate |00>+|11>
qc.h(0)
qc.cx(0,1)

qc.draw()


# In[2]:


from qiskit.quantum_info import Statevector
Statevector(qc).draw('latex')


# In[3]:


# generate |01>+|10> by flipping q_0 or q_1
# either works.
qc.x(1)
qc.draw()


# In[4]:


Statevector(qc).draw('latex')


# **Exercise**  {numref}`%s <sec-2qubits>`.2  Generate $|\Phi^{-}\rangle$ and $|\Psi^{-}\rangle$ using Qiskit.  (There are several different ways. A simple one uses the $Z$ gate.  You can also apply $H$ to both qubits.  Find where to put these gates.)

# [^neg]: Symbol $\neg$ means negation.

# ## Two-qubit measurements in computational basis
# 
# We want to determine $|c_{ij}|$ in  {eq}`superposition-q2` by measurement.  It can be done easily in Qiskit.
# 
# 

# In[5]:


from qiskit import *
import numpy as np

cr=ClassicalRegister(2,'c')
qr=QuantumRegister(2,'q')
qc=QuantumCircuit(qr,cr)

qc.h(0)
qc.cx(0,1)
qc.ry(np.pi/5,0)
qc.rx(np.pi/3,0)

qc.barrier()
qc.measure(0,0)
qc.measure(1,1)

qc.draw()


# In[6]:


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

from qiskit.visualization import plot_histogram
plot_histogram(counts)


# ## Bell state measurement
# 
# We can expand any two qubit states in the Bell basis as
# 
# $$
# \ket{\psi} = c_{\Phi^+} |\Phi^{+}\rangle + c_{\Phi^-} |\Phi^{-}\rangle + c_{\Psi^+} |\Psi^{+}\rangle + c_{\Psi^-} |\Phi^{-}\rangle .
# $$(bell-expansion)
# 
# Now, we want find the probabilities to find the Bell states.  Since the Bell states are all entangled, standard measurement based on the computational basis does not help.  Applying $(H \otimes I)\cdot CX$ transforms the basis to the computational basis without changing the coefficients:
# 
# $$
# (H \otimes I)\cdot CX \ket{\psi} = c_{\Phi^+} |00\rangle + c_{\Phi^-} |10\rangle + c_{\Psi^+} |01\rangle + c_{\Psi^-} |11\rangle .
# $$(comp-expansion)
# 
# Now, the standard measurement in the computational basis determine the probabilities.

# **Exercise**  {numref}`%s <sec-2qubits>`.3  Derive {eq}`comp-expansion`.

# In[ ]:




