#!/usr/bin/env python
# coding: utf-8

# (chap-one-qubit-gates)=
# # One-qubit gates

# In quantum computing, we manipulate the state of qubits by applying a series of gates on qubits. In this chapter, I introduce various one-qubit gates commonly used in quantum computing. When a one-qubit gate acts on a single qubit, the Bloch vector of the qubit rotates around a certain axis by a certain angle.  The most general rotation is [*Euler rotation*](https://en.wikipedia.org/wiki/Euler_angles), which is done by $U$ gate.  In theory, we need only this gate. However, it is not convenient since we have to figure out three parameters (angles) for each operation.  Furthermore, in actual quantum computing devices, the general gate may not be available.   In practice, we use parameter-free gates with predefined rotation axes and angles, and a few others that require a single parameter.
# 
# Mathematically, the gates are unitary operators in $\mathbb{C}^2$. Some are Hermitian and others are not.  {numref}`tbl-q1gates` lists commonly used single-qubit gates.  I explain some the most important ones in the following section.  See also Qiskit documentation:
# 
# [Qiskit Circuit Library](https://qiskit.org/documentation/apidoc/circuit_library.html).

# ```{table} Commonly used single-qubit gates
# :name: tbl-q1gates
# 
# 
# | Generaic Name      |  Qiskit Ciruit Name  | # of Parameters | Symbols |
# | :-----------:      | :------------------: | :-------------: | :-----: |
# | Unitary            |  u                   |         3       |  $U$    |
# | Rotation X         |  rx                  |         1       |  $R_x$  |
# | Rotation Y         |  ry                  |         1       |  $R_y$  |
# | Rotation Z         |  rz                  |         1       |  $R_z$  |
# | Pauli X            |  x                   |         0       |  $X$    |
# | Pauli Y            |  y                   |         0       |  $Y$    |
# | Pauli Z            |  z                   |         0       |  $Z$    |
# | Hadamard           |  h                   |         0       |  $H$    |
# | Sqrt X             |  sx                  |         0       |  $SX$   |
# | Inverse sqrt X     |  sxdg                |         0       |  $SX^\dagger$ |
# | Sqrt Z             |  s                   |         0       |  $S$     |
# | Inverse sqrt Z     |  sdg                 |         0       |  $S^\dagger$ |
# | 4th root Z         |  t                   |         0       |  $T$     |
# | Inverse 4th root Z |  tdg                 |         0       |  $T^\dagger$ |
# | Phase              |  p                   |         1       |  $P$     |
# 
# 
# ```

# Their definition and typical usage of those gates are explained in the following sections.

# ## Mathematical expressions
# 
# There are several ways to define the gates. In the following sections, the gates are defined in four different ways but they  are mathematically all equivalent.  In one definition, a gate is defined by how the computational basis kets are transformed by the gate.  This definition is practical.  For computational purpose, the matrix expression of the gate is more convenient.  The matrix expression assumes the computational basis. Since every gate is a special case of the general $U$ gate, the gate can be expressed with $U$, which is the third definition.
# 

# ## Transformation of general superposition states
# 
# The definitions do not give you a clear idea on the operational functionality of a gate.  It is important to understand how a superposition state is transformed by the gate. Pay attention to how the coefficients are transformed.

# ## Combination of gates
# 
# When gate $Y$ is applied after $X$, we write it $Y \cdot X$. We can think of a gate $(Y \cdot X)$  acts on a state vector as
# 
# $$
# Y (X |\psi\rangle) = (Y \cdot X) |\psi\rangle
# $$
# 
# We put "$\cdot$" between the gates to avoid confusion.  For example $SX$ is a single gate and $S \cdot X$ is a product of $S$ and $X$.
# 
# The order is important.  $Y \cdot X$ is not necessarily equal to $X \cdot Y$.
# 
# In quantum circuit, the gates act from left to right.  For example,  $Y\cdot X |0\rangle$ becomes

# In[1]:


from qiskit import QuantumCircuit

qc=QuantumCircuit(1)
qc.x(0)
qc.y(0)
qc.draw()


# 
# ---
# 
# Last modified: 07/09/2022
