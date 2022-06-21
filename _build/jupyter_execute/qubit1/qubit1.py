#!/usr/bin/env python
# coding: utf-8

# (sec-math-qubit)=
# # Mathematical expression of a qubit
# 

# Quantum computers store information in a two-dimensional Hilbert space called a qubit.   In this section, I will introduce mathematical description of a single qubit.

# ## Pure states
# 
# In ideal situations, the state of a qubit is specified by a ket vector in a two-dimensional Hilbert space.  Unless otherwise is specified, state vectors are assumed to be normalized. That is $\langle \psi | \psi \rangle = 1$ (See {numref}`sec-math`). 
# In less ideal situations, a qubit is in a *mix state* involving multiple state vectors, which will be discussed in a later chapter.  In this chapter, we focus on pure states.
# 
# Any qubit state can be written as 
# 
# $$
# | \psi \rangle = c_0 | 0 \rangle + c_1 | 1 \rangle
# $$(eq-qubit-purestate)
# 
# where $| 0 \rangle $ and $| 1 \rangle$ are orthonormal basis vectors satisfying $\langle 0 | 0 \rangle = \langle 1 | 1 \rangle = 1$ and $\langle 0 | 1 \rangle = \langle 1 | 0 \rangle = 0$.  The coefficients $c_0$ and $c_1$ are complex numbers. The normalization requirement is satisfied if $|c_0|^2 + |c_1|^2 = 1$.
# 
# This orthonroaml complete basis set $\{|0\rangle, |1\rangle\}$ is known as *computational basis* and it is a convention to use it in quantum computing.  However, the basis vectors do not represent any particular physical basis set.  In real quantum computers,  a qubit can be realized, for example, by an electron spin, $|0\rangle \equiv | \uparrow \rangle$ and $|1\rangle \equiv |\downarrow \rangle$ or a polarization of photon, $|0\rangle \equiv | H \rangle$ (horizontal polarization) and $|1\rangle \equiv | V \rangle$ (vertical polarization).  By using the computational basis set, we don't have to worry about what type of hardware is used.  The mathematical expression based on the computational basis can be applied to all of quantum computers based on qubits.
# 
# 

# ## Bloch sphere
# 
# While Eq. {eq}`eq-qubit-purestate` can describe any qubit state, we can simplify it without losing generality. 
# Writing the complex coefficient in the polar expression,
# $c_0 = r_0 e^{i \phi_0}$ and $c_1 = r_1 e^{i \phi_1}$ where $r_i$ and $\phi_i$ are modulus and argument. Then, we remove a global phase as 
# 
# $$
# \ket{\psi} = r_0 e^{i \phi_0} \ket{0} + r_1 e^{i \phi_1} \ket{1} = e^{i \phi_0} \left( r_0  \ket{0} + r_1 e^{i (\phi_1-\phi_0)} \ket{1} \right) \simeq r_0  \ket{0} + r_1 e^{i \theta} \ket{1}
# $$
# 
# where $\phi=\phi_1-\phi_0,\ \phi \in [0, 2\pi)$ and $\simeq$ means "equivalent state vector".  Now, the normalization condition becomes $r_0^2 + r_1^2 = 1$.  Since $r_0$ and $r_1$ are positive, we can write them as $r_0 = \cos\left(\frac{\theta}{2}\right)$ and $r_1 = \sin\left(\frac{\theta}{2}\right)$ with $0 < \theta < \pi$.  Now the general qubit state is written as
# $$
# \ket{\psi} = \cos\left(\frac{\theta}{2}\right) \ket{0} + \sin\left(\frac{\theta}{2}\right) e^{i \phi} \ket{1},\quad 0 \le \theta \le \pi, \, 0 \le \phi < 2 \pi .
# $$

# In[ ]:




