#!/usr/bin/env python
# coding: utf-8

# (sec-math-qubit)=
# # Mathematical expression of a qubit
# 

# Quantum computers store information in a two-dimensional Hilbert space called a qubit.   In this section, I will introduce mathematical description of a single qubit.

# ## Pure states
# 
# The state of a classical particle is precisely identified by its position and momentum, which is a point in the phase space.  Hence, the classical state is a _phase point_.  The phase point moves in the phase space according to the Newton's laws of motion and forms a _phase trajectory_. In contrast,
# 
# > the state of a quantum object is specified by a complex vector in the Hilbert space,  
# 
# The vector is known as *state vector* and expressed with a *ket* as explained below. In ideal situations, a single state vector contains everything about the state of the qubit. Such a state is called *pure state*. The pure state evolves in time according to Schr&ouml;dinger which I introduce shortly.
# 
# In less ideal situations, a qubit is in a *mix state* involving multiple state vectors, which will be discussed in a later chapter.  In this chapter, we focus on pure states.

# ## Ket and bra for a qubit
# 
# .
# 
# 
# 
# Unless otherwise is specified, state vectors are assumed to be normalized. That is $\langle \psi | \psi \rangle = 1$ (See {numref}`sec-math`). 
# 
# A qubit is a two-dimensional Hilbert space and thus any qubit state can be written as 
# 
# $$
# | \psi \rangle = c_0 | 0 \rangle + c_1 | 1 \rangle
# $$(eq-qubit-purestate)
# 
# where $| 0 \rangle $ and $| 1 \rangle$ are orthonormal basis vectors satisfying $\langle 0 | 0 \rangle = \langle 1 | 1 \rangle = 1$ and $\langle 0 | 1 \rangle = \langle 1 | 0 \rangle = 0$.  The coefficients $c_0$ and $c_1$ are complex numbers. The normalization requirement is satisfied if $|c_0|^2 + |c_1|^2 = 1$.
# 
# This basis set is known as *computational basis* and the basis vectors do not represent any particular physical basis set.  In real quantum computers,  a qubit can be realized, for example, by an electron spin, $|0\rangle \equiv | \uparrow \rangle$ and $|1\rangle \equiv |\downarrow \rangle$ or a polarization of photon, $|0\rangle \equiv | H \rangle$ (horizontal polarization) and $|1\rangle \equiv | V \rangle$ (vertical polarization).  By using the computational basis set, we don't have to worry about what type of hardware is used.  The mathematical expression we use can be applied to all of quantum computers based on qubits.
#  

# ## Normalization and global phase
# 
# The state of a quantum object is express by a ket in the Hilbert space.  However, the ket is not unique.  Many kets actually corresponds to the same physical state.  If $\ket{\varphi}$ represents a state, $|\psi\rangle = \alpha \ket{\varphi}$ also represent the same state where $\alpha$ is any complex number. For example, $\ket{\varphi}, -\ket{\varphi}, i \ket{\varphi}, \frac{1}{2} \ket{\varphi}, 2 \ket{\varphi}$ all represent the same quantum state. However, the difference is only the scalar factor.    In mathematics, $\{ \alpha \ket{\varphi}, \forall \alpha \in \mathbb{C}\}$ is known as *ray*.   Any ray represents the same quantum state.  Although this ambiguity does not cause a fundamental trouble, it is certainly inconvenient.  We attempt to reduce the ambiguity.    This leads to $|\alpha|^2=1$.  However, the ambiguity still remains since $\alpha = e^{i \theta}$ satisfies the normalization condition with any real value of $\theta$. In summary, if $|\varphi\rangle$ is a normalized state vector, $e^{i \theta} | \varphi\rangle$ is also a normalized state vector and both represent the same physical state. In other word,s $e^{i \theta}$, which is called *global phase*, does not contribute to the physical state of qubit.  Hence, it can be ignored.  This property is utilized when we develop efficient quantum computing codes.
# 

# In[ ]:




