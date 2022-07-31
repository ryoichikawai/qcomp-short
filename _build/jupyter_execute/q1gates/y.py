#!/usr/bin/env python
# coding: utf-8

# (sec-ygate)=
# # YGate 
# 
# This gate is not popular since it can be replaced with other common operators.  Hence, this section only briefly covers its properties.

# [API References: YGate](https://qiskit.org/documentation/stubs/qiskit.circuit.library.YGate.html#qiskit.circuit.library.YGate)

# ## Definition
# 
# **Transformation**
# 
# >$$
# Y |0\rangle = i|1\rangle, \qquad Y |1\rangle = -i |0\rangle
# $$
# 
# 
# **Matrix expression**
# 
# >$$
# Y \doteq \begin{bmatrix} 0 & -i \\ i & 0 \end{bmatrix}
# $$(YGate-matrix)
# 
# 
# **U gate expression**
# 
# >$$
# Y = U\left(\pi,\frac{\pi}{2},\frac{\pi}{2}\right)
# $$(YGate-U)
# 
# **R gate expression**
# 
# >$$
# Y = i R_y(\pi)
# $$
# 
# The qiskit circuit symbol is `y` and it appears in quantum circuit as

# In[1]:


from qiskit import QuantumCircuit
qc=QuantumCircuit(1)
qc.y(0)
qc.draw()


# ## Acting on a superposition state
# 
# When Ygate is applied to a super position state the coefficient is swapped.  That is
# 
# >$$
# Y \left (c_0 |0\rangle + c_1 |1\rangle\right)  = -i (c_1 |0\rangle - c_0 |1\rangle)
# $$(Y-on-superpos)
# 
# If the global phase factor is omitted, we have
# 
# >$$
# Y \left (c_0 |0\rangle + c_1 |1\rangle\right) \simeq c_1 |0\rangle - c_0 |1\rangle
# $$(Y-on-superpos2)
# 
# Like Xgate, the coefficients are swapped.  In addition the relative phase of $\pi$ is applied.

# ## Important Properties
# 
# > $Y^2 = I$
# 
# This means that
# 1.  $Y^2$ does not do any thing on the qubit.
# 2.  $Y$ is  self-inverse, that is $Y^{-1} = Y$.
# 3.  $Y$ is self-adjoint ($Y^\dagger = Y$) since $Y$ is unitary ($Y^\dagger = Y^{-1}$) by definition.
# 

# 
# ---
# **Exercise** {numref}`%s <sec-ygate>`.1&nbsp;  Show that $Y|+\rangle = -i |-\rangle$ and $Y|-\rangle = i |+\rangle$.
# Apart from the phase factor, $Y$ flips $|\pm\rangle$.
# 
# ---
# 

# Late modified xxx
