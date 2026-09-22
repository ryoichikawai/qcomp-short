#!/usr/bin/env python
# coding: utf-8

# (sec-sxgate)=
# # SX and SXdg Gates
# 
# SX gate is a native gate of IBMQ hardware. Do not get confused with $S$ times $X$.
# 
# [API References: SXGate](https://qiskit.org/documentation/stubs/qiskit.circuit.library.SXGate.html#qiskit.circuit.library.SXGate)  
# [API References: SXdgGate](https://qiskit.org/documentation/stubs/qiskit.circuit.library.SXdgGate.html#qiskit.circuit.library.SXdgGate) 

# ## Definition
# 
# **Transformation**
# 
# >$$
# \begin{align}
# &SX |0\rangle = e^{i\pi/4}|R\rangle,  &&SX |1\rangle = e^{i\pi/4}|L\rangle\\
# &SX^\dagger |0\rangle = e^{-i\pi/4}|L\rangle, &&SX^\dagger |1\rangle = e^{-i\pi/4}|R\rangle
# \end{align}
# $$
# 
# **Matrix expression**
# 
# >$$
# SX \doteq \frac{1}{2} \begin{bmatrix} 1+i & 1-i \\ 1-i & 1+i \end{bmatrix}, \quad
# SX^\dagger \doteq \frac{1}{2} \begin{bmatrix} 1-i & 1+i \\ 1+i & 1-i \end{bmatrix}
# $$(SXGate-matrix)
# 
# 
# **U gate expression**
# 
# >$$
# SX = e^{i \pi/4}\, U\left(\frac{\pi}{2}, -\frac{\pi}{2}, \frac{\pi}{2} \right)
# $$
# 
# **R gate expression**
# 
# >$$
# SX = e^{i \pi/4} R_x(\pi/2), \quad SX^\dagger = e^{-i \pi/4} R_x(-\pi/2)
# $$
# 
# 
# Notice that $SX^2 = (SX^\dagger)^2 = X$.  Hence, $SX$ and $SX^\dagger$ are square roots of $X$ and they are often expressed as  $SX=X^{1/2}$ and $SX^\dagger = X^{-1/2}$.
# 
# The Qiskit circuit code symbols are `sx` and `sxdg`, respectively. They appear in quantum circuits as

# In[1]:


from qiskit import QuantumCircuit
qc=QuantumCircuit(1)
qc.sx(0)
qc.sxdg(0)
qc.draw('mpl')


# or

# In[2]:


qc.draw()


# ## Transformation of other basis kets
# 
# * $x$-basis
# 
# >$$
# \begin{align}
# &SX |+\rangle = |+\rangle,  &&SX |-\rangle = i |-\rangle \\
# &SX^\dagger |+\rangle = |+\rangle, &&SX^\dagger |-\rangle = -i |-\rangle
# \end{align}
# $$
# 
# * $y$-basis
# 
# >$$
# \begin{align}
# &SX |L\rangle = e^{i\pi/4}|0\rangle,  &&SX |R\rangle = e^{i\pi/4}|1\rangle\\
# &SX^\dagger |L\rangle = e^{-i\pi/4}|1\rangle, &&SX^\dagger |R\rangle = e^{-i\pi/4}|0\rangle
# \end{align}
# $$
# 

# ## Acting on a superposition state
# 
# When SXGate and SXdgGate are applied to a super position state the coefficient to $|0\rangle$ remains the same but that of $|1\rangle$ gets additional phase factor.  That is
# 
# >$$
# SX \left (c_0 |0\rangle + c_1 |1\rangle\right) = \frac{1}{\sqrt{2}}\left(e^{i \pi/4} c_0 + e^{-i \pi/4} c_1\right) |0\rangle + \frac{1}{\sqrt{2}}\left(e^{-i \pi/4} c_0 + e^{i \pi/4} c_1\right) |1\rangle 
# $$(SX-on-superpos)
# 
# >$$
# SX^\dagger \left (c_0 |0\rangle + c_1 |1\rangle\right) = \frac{1}{\sqrt{2}}\left(e^{-i \pi/4} c_0 + e^{i \pi/4} c_1\right) |0\rangle + \frac{1}{\sqrt{2}}\left(e^{i \pi/4} c_0 + e^{-i \pi/4} c_1\right) |1\rangle 
# $$(SXdg-on-superpos)
# 
# 
# In $\{|+\rangle,|-\rangle\}$ basis,
# 
# >$$
# SX \left(c_0 |+\rangle + c_1|-\rangle\right) = c_0 |+\rangle + i c_1 |-\rangle
# $$(SX-on-supoerpos+)
# 
# >$$
# SX^\dagger \left(c_0 |+\rangle + c_1|-\rangle\right) = c_0 |+\rangle - i c_1 |-\rangle
# $$(SXdg-on-supoerpos+)
# 
# Comparing these relations with Eqs. {eq}`S-on-superpos` and {eq}`Sdg-on-superpos`, we find that SXGate and SGate work in the same way but in different basis sets.

# ## Additional useful Properties
# 
# $SX \cdot SX = SX^\dagger \cdot SX^\dagger = X$ implies that
# 1. $SX = X \cdot SX^\dagger = SX^\dagger\cdot X, \quad SX^\dagger = X \cdot SX = SX \cdot X$.
# 2. $X = SX \cdot X \cdot SX^\dagger = SX^\dagger \cdot X \cdot SX$
# 3. $SX = X \cdot SX \cdot X, \quad SX^\dagger = X \cdot SX^\dagger \cdot X$.

# 
# ---
# Last modified: 08/31/2022
