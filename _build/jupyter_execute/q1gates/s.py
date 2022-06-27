#!/usr/bin/env python
# coding: utf-8

# (sec-sgate)=
# # S Gate and S$^\dagger$ Gate
# 
# We shall call $S$ and $S^\dagger$ gates SGate and SdgGate, respectively.

# [API References: SGate](https://qiskit.org/documentation/stubs/qiskit.circuit.library.SGate.html#qiskit.circuit.library.SGate)  
# [API References: SdgGate](https://qiskit.org/documentation/stubs/qiskit.circuit.library.SdgGate.html#qiskit.circuit.library.SdgGate)  

# ## Definition
# 
# > $S |0\rangle = |0\rangle, \qquad S |1\rangle = i|1\rangle$   
# > $S^\dagger |0\rangle = |0\rangle, \qquad S^\dagger |1\rangle = -i|1\rangle$
# 
# 
# The qiskit circuit symbol is $S$ for SGate and $Sdg$ for SdgGate. They appear in quantum circuits as

# In[1]:


from qiskit import QuantumCircuit
qc=QuantumCircuit(1)
qc.s(0)
qc.sdg(0)
qc.draw()


# ## Acting on a superposition state
# 
# When SGate and SdgGate are applied to a super position state the coefficient is swapped.  That is
# 
# >$$
# S \left (c_0 |0\rangle + c_1 |1\rangle\right) = c_0 |0\rangle + i c_1 |1\rangle 
# $$(S-on-superpos)
# >$$
# S^\dagger \left (c_0 |0\rangle + c_1 |1\rangle\right) = c_0 |0\rangle - i c_1 |1\rangle 
# $$(Sdg-on-superpos)
#  
# Notice that the relative phase changes by $e^{\pm i\pi/2} = \pm i$.  Recall that $Z$ changes the relative phase by $e^{i \pi} = -1$. Further notice that $(e^{\pm i \pi/2})^2 = e^{i \pi}$.  Hence, $S^2 = (S^\dagger)^2 = Z$.  Because of this relation,  $S$ is sometimes expressed as $\sqrt{Z}$.

# Setting $c_0=c_1=\frac{1}{\sqrt{2}}$, we find basis transformation
# 
# >$$
# S|+\rangle = |L\rangle, \quad S|-\rangle = |R\rangle
# $$(Sgate-fwd)
# >$$
# S^\dagger|+\rangle = |R\rangle, \quad S^\dagger|-\rangle = |L\rangle
# $$(SdgGate-fwd)
# 
# Since $S$ is unitary $S S^\dagger = I$ and thus $S^{-1}=S^\dagger$ and $(S^\dagger)^{-1} = S$.  Now the inverse of {eq}`Sgate-fwd` and `SdgGate- fwd` are
# 
# >$$
# S^\dagger |L\rangle = |+\rangle, \quad S^\dagger|R\rangle = |-\rangle
# $$(Sgate-inv)
# >$$
# S|L\rangle = |-\rangle, \quad S|R\rangle = |+\rangle
# $$(SdgGate-inv)
# 

# Combining HGate and SGate, we can transform the computational basis $\{|0\rangle, |1\rangle\}$ to $\{|L\rangle, |R\rangle\}$ by $S H$ and its inverse is $H S^\dagger$.  Now, we know we can move from one basis to another by $H$, $S$, and $SH$. 

# 
# ---
# **Qiskit Example** {numref}`%s <sec-sgate>`.1&nbsp; We demonstrate the above basis set transformation using Qiskit.  First, we construct a quantum circuit corresponding to the following transformation
# 
# $$
# |0\rangle \xrightarrow{H} |+\rangle \xrightarrow{S} |L\rangle \xrightarrow{S^\dagger} |+\rangle \xrightarrow{H} |0\rangle
# $$
# 
# Notice that the whole operation can be written as $H S^\dagger S H |0\rangle$ it can be simplified as
# 
# $$
# H S^\dagger S H |0\rangle = H (S^\dagger S) H = H I H = H^2 = I
# $$
# 
# Hence, the whole operation does nothing at all.  In order to avoid unnecessary computation like this, we need to understand the properties of gates.  You will surprise that a long circuit can be significantly shortened by contracting gates.

# In[2]:


get_ipython().run_cell_magic('capture', '', 'from qiskit import *\nfrom qiskit.visualization import visualize_transition\n\nqc=QuantumCircuit(1)\n\nqc.h(0)\nqc.s(0)\nqc.sdg(0)\nqc.h(0)\n\nmovie=visualize_transition(qc,fpg=50, spg=1)')


# In[3]:


qc.draw('mpl')


# In[4]:


movie


# ## Additional useful Properties
# 
# $S\, S = S^\dagger \, S^\dagger = Z$ implies that
# 1. $S = Z S^\dagger = S^\dagger Z, \quad S^\dagger = Z S = S Z$.
# 2. $Z = S Z S^\dagger = S^\dagger Z S$
# 3. $S = Z S Z, \quad S^\dagger = Z S^\dagger Z$.

# ---
# Actions on X, Y, and Z-basis
