#!/usr/bin/env python
# coding: utf-8

# (sec-rgate)=
# # Rotation Gates, RX, RY, RZ
# 
# The rotation gates $R_x(\theta)$, $R_y(\theta)$, and $R_z(\theta)$ rotate the vector by $\theta$ around $x$, $y$, and $z$ axis, respectively.  All rotation gates require one parameter $\theta$.
# 
# Qiskit circuit names are `rx`, `ry`, and `rx`, respectively.

# [API References: RXGate](https://qiskit.org/documentation/stubs/qiskit.circuit.library.RXGate.html)  
# [API References: RYGate](https://qiskit.org/documentation/stubs/qiskit.circuit.library.RYGate.html)  
# [API References: RZGate](https://qiskit.org/documentation/stubs/qiskit.circuit.library.RZGate.html)  

# ## Definition
# 
# **Transformation**
# 
# >$$
# \begin{align}
# R_x(\theta)|0\rangle &= \cos(\theta/2)|0\rangle - i \sin(\theta/2) |1\rangle\\ 
# R_x(\theta)|1\rangle &= -i \sin(\theta/2) |0\rangle + \cos(\theta/2) |1\rangle
# \end{align}
# $$
# 
# >$$
# \begin{align}
# R_y(\theta)|0\rangle &= \cos(\theta/2)|0\rangle - \sin(\theta/2) |1\rangle\\
# R_y(\theta)|1\rangle &= \sin(\theta/2) |0\rangle + \cos(\theta/2) |1\rangle
# \end{align}
# $$
# 
# >$$
# \begin{align}
# R_z(\theta)|0\rangle &= e^{-i \theta/2} |0\rangle\\
# R_z(\theta)|1\rangle &= e^{i \theta/2} |1\rangle
# \end{align}
# $$
# 
# **Pauli expressions**
# 
# > $$
# \begin{align}
# R_x(\theta) &= e^{-i X \theta/2} = \cos(\theta/2) I - i \sin(\theta/2) X\\   
# R_y(\theta) &= e^{-i Y \theta/2} = \cos(\theta/2) I - i \sin(\theta/2) Y\\  
# R_z(\theta) &= e^{-i Z \theta/2} = \cos(\theta/2) I - i \sin(\theta/2) Z
# \end{align}
# $$
# 
# **Matrix expressions**
# 
# >$$
# \begin{align}
# R_x(\theta) &\doteq \begin{bmatrix} \cos(\theta/2) & -i \sin(\theta/2) \\ -i \sin(\theta/2)& \cos(\theta/2)\end{bmatrix} \\
# R_y(\theta) &\doteq \begin{bmatrix} \cos(\theta/2) & - \sin(\theta/2) \\ \sin(\theta/2)& \cos(\theta/2)\end{bmatrix}\\
# R_z(\theta) &\doteq \begin{bmatrix} e^{-i \theta/2} & 0 \\0 & e^{i \theta/2}\end{bmatrix}
# \end{align}
# $$
# 
# These gates rotates the Bloch vector arounf $x$, $y$, and $z$ axis by $\theta$, respectively.
# 
# The qiskit circuit code symbols are `rx`, `ry`, and `rz`, respectively and they appear in quantum circuit as

# In[1]:


from qiskit.circuit import QuantumCircuit, Parameter

# set parameter symbol to theta
t=Parameter('\u03B8')

# costruct the circuit
qc=QuantumCircuit(1)
qc.rx(t,0)
qc.ry(t,0)
qc.rz(t,0)

# show the circuit
qc.draw('mpl')


# or

# In[2]:


qc.draw()


# **Example** {numref}`%s <sec-rgate>`.1&nbsp;  Starting with $|0\rangle$, rotate about the $y$ axis by $\pi/3$, about $z$ axis by $\pi/2$, and about $x$ axis by $-2\pi/3$. This example shows that the final state is $|1\rangle$.  

# In[3]:


get_ipython().run_cell_magic('capture', '', 'import numpy as np\nfrom qiskit.circuit import QuantumCircuit\nfrom qiskit.quantum_info import Statevector\n\nqc=QuantumCircuit(1)\nqc.ry(np.pi/3,0)\nqc.rz(np.pi/2,0)\nqc.rx(-2*np.pi/3,0)\n\n# load the visdualization tool\nfrom qiskit.visualization import visualize_transition\n\n# generate a movie (it will be shown in next cell,\nmovie=visualize_transition(qc,fpg=20, spg=1)')


# In[4]:


movie


# ## Additional useful Properties
# 
# In the following $R$ represent any of $RX$, $RY$, and $RZ$.
# 
# 1. $R^\dagger(\theta) = R^{-1}(\theta) = R(-\theta)$
# 2. $R^{\alpha} (\theta) = R(\alpha\theta)$
# 3. $R(\theta_2) \cdot R(\theta_1) = R(\theta_1 + \theta_2)$  (note: all rotations must be around the same axis.)

# ## Relation with other gates
# 
# By definition a one-qubit gate transforms a Bloch vector to another, which is a rotation of the Bloch vector.  Hence, Any one-qubit gate can be expressed as rotation.  In turn, any rotation can be expressed by a combination of rotations.  Hence, any one-qubit gate can be expressed with a comination of RXGate, RYGate, and RZGate.  Mathematically, these three gates are enough to describe quantum computation.  However, the combination of rotation gates are not necessarily the most efficient implementation of gates.  Parameter-free gates are still preferred.
# 
# The previous gates are related to the rotation as
# 
# * $X = i RX(\pi) \simeq RX(\pi)$
# * $Y = i RY(\pi) \simeq RY(\pi)$
# * $Z = i RZ(\pi) \simeq RZ(\pi)$
# * $H = X \cdot Y^{1/2} \simeq RX(\pi) RY(\pi/2)$
# * $S = Z^{1/2} \simeq RZ(\pi/2)$
# * $T = Z^{1/4} \simeq RZ(\pi/4)$
# * $SX = X^{1/2} \simeq RX(\pi/2)$
# 

# 
# ---
# Last modified: 08/31/2022
