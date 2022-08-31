#!/usr/bin/env python
# coding: utf-8

# (sec-cpgate)=
# # Controlled- Z, S, T, P gates

# Recall that that Z, S, and T gates all change the phase of $|1\rangle$ and that the general phase gate P($\theta$) can replace them as Z = P($\pi$), S = P($\pi/2$), and T = P($\pi/4$)  (See {numref}`chap-one-qubit-gates`.)  In this section, controlled- Z, S, T, and P gates (CZ, CS, CT, and CP, respectively) are introduced.  Since all of them work in the similar manner, only controlled-P is explained in most parts.

# **Operational Definition**
# 
# When gate  CP$_{q_0}^{q_1}(\theta)$ acts on $|q_1\, q_0\rangle$, P($\theta$) is applied to $q_1$ if $q_0=1$ and nothing is done otherwise. Qubit $q_0$ serves as source and $q_1$ as target.  AS shwon bellow, CP$_{q_0}^{q_1}(\theta) =$ CP$_{q_1}^{q_0}(\theta)$.  Hence, it is not necessary to specify a source and a target qubit.  
# 
# Mathematically, it is expressed as
# 
# $$
# \text{CP}_{q_0}^{q_1}(\theta)|q_1\, q_0\rangle = \text{I} \otimes |0\rangle\langle 0| + \text{P}(\theta) \otimes |1\rangle\langle 1|
# $$
# 
# Switching source and target qubits, 
# 
# CP$_{q_1}^{q_0} (\theta) |q_1\, q_0\rangle$  applies P($\theta$) to $q_0$ if $q_1=1$ and do nothing otherwise.  Mathematically, it is expressed as
# 
# $$
# \text{CP}_{q_1}^{q_0}|q_1\, q_0\rangle (\theta) = |0\rangle\langle 0| \otimes \text{I}   +   |1\rangle\langle 1| \otimes \text{P}(\theta)
# $$
# 
# **Transformation**
# 
# CP$_{q_0}^{q_1}(\theta)$ and CP$_{q_1}^{q_0}(\theta)$ transforms computational basis as follows:
# 
# $$
# \begin{align}
# &\text{CP}_{q_0}^{q_1}(\theta) \lvert 00\rangle = \lvert 00\rangle\\ 
# &\text{CP}_{q_0}^{q_1}(\theta) \lvert 01\rangle = \lvert 01\rangle\\
# &\text{CP}_{q_0}^{q_1}(\theta) \lvert 10\rangle = \lvert 00\rangle\\
# &\text{CP}_{q_0}^{q_1}(\theta) \lvert 11\rangle = e^{i \theta}\lvert 11\rangle
# \end{align}
# $$
# 
# Since only $\lvert 11\rangle$ is affected, $\text{CP}_{q_0}^{q_1}(\theta)= \text{CP}_{q_1}^{q_0}(\theta)$.
# 
# **Matrix representation**
# 
# $$
# \text{CP}_{q_0}^{q_1}(\theta) = \text{CP}_{q_0}^{q_1}(\theta)  = \begin{bmatrix} 1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&e^{i\theta}\end{bmatrix}
# $$
# 
# 

# ## Qiskit circuit functions
# 
# The Qiskit circuit functions for CZ and CP are `cz` and `cp`, respectively and it appears in a circuit as follows.  Unlike CX gate, the source and target are not distinguished.

# In[1]:


from qiskit import *
from qiskit.circuit import Parameter
from qiskit.quantum_info import Statevector
t=Parameter('\u03B8')

qr  = QuantumRegister(2)
qc = QuantumCircuit(qr)

# control CZ gate
qc.cz(0,1)

# contrl CP gate
qc.cp(t,0,1)

qc.draw()


# Qiskit does not have standard circuit functions for CS and CT but they are predefined in `qiskit.circuit.library.standard_gates`.  You just have to create a shorthand expression from the library and use `append` function to add the gate to the circuit. We can always use CP($\pi/2$) and CP($\pi/4$) for CS and CT, respectively.

# In[2]:


from qiskit import *
from qiskit.circuit.library.standard_gates import SGate, TGate

cs = SGate().control(1) # the parameter is the amount of control points you want
ct = TGate().control(1)
qr=QuantumRegister(2,'q')
qc = QuantumCircuit(qr)

qc.append(cs, [0, 1])
qc.append(ct, [0, 1])

qc.draw()


# ## Acting on superposition state
# 
# CP$_{q_0}^{q_1}(\theta)$ multiplies phase factor $e^{i\theta}$ only to $|11\rangle$.  Other basis vectors are not affected.  Note also that the modulus of the coefficients remain the same and thus probabilities of finding the computational basis vectors are not modified by CP.
# 
# $$
# \text{CP}_{q_0}^{q_1} (\theta) \left (c_{00} |00\rangle + c_{01} |01\rangle + c_{10} |10\rangle + c_{11} |11\rangle \right ) =
# c_{00} |00\rangle + c_{11} |01\rangle + c_{10} |10\rangle + e^{i \theta} c_{01} |11\rangle
# $$
# 
# How can we change the phase of a basis vector other than $|11\rangle$?  A possible strategy is to transform the target basis vector to $|11\rangle$, apply CP and transform back to the original basis vector.  For example, if we want to multiply $i$ to $|00\rangle$ without changing other basis vector, apply $(\text{X} \otimes \text{X}) \cdot \text{CS} \cdot (\text{X} \otimes \text{X})$ 

# **Example**  
# How can we change the phase of a basis vector other than $|11\rangle$?  A possible strategy is to transform the target basis vector to $|11\rangle$, apply CP and transform back to the original basis vector.  For example, if we want to multiply $i$ to $|00\rangle$ without changing other basis vector, apply $(\text{X} \otimes \text{X}) \cdot \text{CS} \cdot (\text{X} \otimes \text{X})$.  In this example, we start with a product state $|+\rangle \otimes |+\rangle$.  Then, the above gate is applied to it.  Check that $i$ is multiplied only to  $|00\rangle$.  The final state is entangled. (See {numref}`sec-2qubits`.

# In[3]:


from qiskit import *
from qiskit.quantum_info import Statevector
import numpy as np

qr=QuantumRegister(2,'q')
qc = QuantumCircuit(qr)

# prepare a super position state
qc.h([0,1])

print("initial state")
Statevector(qc).draw('latex')



# In[4]:


qc.barrier()
qc.x([0,1])
qc.cp(np.pi/2,0,1)
qc.x([0,1])
qc.draw()


# In[5]:


print("final state")
Statevector(qc).draw('latex')


# 
# 
# 
# 
# **Exercise**
# 
# Construct a circuit that transforms $\frac{1}{2}\left(|00\rangle + |01\rangle + |10\rangle + |11\rangle\right)$ to $\frac{1}{2}\left(|00\rangle + |01\rangle - |10\rangle + |11\rangle\right)$.
# 
# 
# 
# 

# In[ ]:




