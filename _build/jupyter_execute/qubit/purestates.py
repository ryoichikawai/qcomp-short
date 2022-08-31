#!/usr/bin/env python
# coding: utf-8

# (sec-purestates)=
# # Pure states
# 

# Quantum computers store information in a two-dimensional Hilbert space called a qubit.   In this section, I will introduce mathematical description of a single qubit.

# ## Pure states
# 
# In ideal situations, the state of a qubit is specified by a single ket vector in a two-dimensional Hilbert space.  We call the ket *state vector* and the ideal state *pure state*.  Unless otherwise is specified, the state vectors are assumed to be normalized. That is $\langle \psi | \psi \rangle = 1$ (See {numref}`sec-statevectors`). 
# In less ideal situations, a qubit is in a *mix state* involving multiple pure states, which will be discussed in a later chapter.  In this chapter, we focus on pure states.
# 
# Any qubit state can be written as 
# 
# $$
# | \psi \rangle = c_0 | 0 \rangle + c_1 | 1 \rangle
# $$(qubit-purestate)
# 
# where $| 0 \rangle $ and $| 1 \rangle$ are orthonormal basis vectors satisfying $\langle 0 | 0 \rangle = \langle 1 | 1 \rangle = 1$ and $\langle 0 | 1 \rangle = \langle 1 | 0 \rangle = 0$.  The coefficients $c_0$ and $c_1$ are complex numbers. The normalization requirement is satisfied if $|c_0|^2 + |c_1|^2 = 1$.
# 
# This orthonormal complete basis set $\{|0\rangle, |1\rangle\}$ is known as *computational basis* which is the default basis in quantum computing.  However, this basis set do not represent any particular physical basis set.  In real quantum computers,  a qubit can be realized, for example, by an electron spin, $|0\rangle \equiv | \uparrow \rangle$ and $|1\rangle \equiv |\downarrow \rangle$ or the polarization of a photon, $|0\rangle \equiv | H \rangle$ (horizontal polarization) and $|1\rangle \equiv | V \rangle$ (vertical polarization).  By using the computational basis set, we don't have to worry about what type of hardware is used.  The mathematical expression based on the computational basis can be applied to all of qubit-based quantum computers.

# ## Standard Basis sets
# 
# In addition to the computational basis (also known as *z-basis*) $\{|0\rangle,|1\rangle\}$, we often use other orthonormal basis set, namely *x-basis* $\{|+\rangle, |-\rangle\}$ and *y-basis* $\{|L\rangle,|R\rangle\}$.
# They are related to the computational basis as follows:
# 
# $$
# |+\rangle = \frac{1}{\sqrt{2}}\left(|0\rangle + |1\rangle\right), \quad
# |-\rangle = \frac{1}{\sqrt{2}}\left(|0\rangle - |1\rangle\right)
# $$(XBasis)
# 
# $$
# |L\rangle = \frac{1}{\sqrt{2}}\left(|0\rangle + i |1\rangle\right), \quad
# |R\rangle = \frac{1}{\sqrt{2}}\left(|0\rangle - i |1\rangle\right)
# $$(YBasis)

# 
# ---
# **Exercise** {numref}`%s <sec-purestates>`.1 &nbsp;  Assuming that the computational basis is orthonormal, show that the x-basis and the y-basis are orthonormal.
# 
# ---
# 

# ## The basis sets in Qiskit
# 
# In Qiskit, the computatioal basis kets $\{|0\rangle, |1\rangle\}$ and x-basis kets $\{|+\rangle, |-\rangle\}$ are predefined.  See the following Qiskit note. 

# :::{admonition} Qiskit note: Computational Basis
# :class: tip
# 
# The `qiskit.opflow` library provides us with basic tools to describe quantum mechanics using expressions very similar to the original methematical expressions.  Here are the correspondence between mathematical expressions and `opflow` expressions.
# 
# > $|0\rangle \quad \Rightarrow \quad$ `Zero`  
# > $|1\rangle \quad \Rightarrow \quad$ `One`  
# > $|+\rangle \quad \Rightarrow \quad$ `Plus`  
# > $|-\rangle \quad \Rightarrow \quad$ `Minus`     
# 
# The vector with "~" indicates bra.  For example,  
# > $\langle 0| \quad  \Rightarrow \quad$ `~One` 
# 
# The regular addition works.
# > $|0\rangle + |1\rangle \quad \Rightarrow \quad$  `Zero + One`
# 
# The operator for inner product is "@". You need to evalute it with `.eval()`.
# > $\langle 0 | + \rangle \quad \Rightarrow \quad$  `(~Zero @ Plus).eval()`
# 
# `eval` is a method associated with `OperatorBase` class in `qiskit.opflow`.
# 
# For more detail, see [Qiskit API Document: qiskit.opflow](https://qiskit.org/documentation/apidoc/opflow.html)
# 
# :::

# 
# ---
# **Qiskit Example** {numref}`%s <sec-purestates>`.1 &nbsp; Let us check the orthonormality of the computational basis set in Qiskit.

# In[1]:


# Import numpy (for sqrt)
import numpy as np

# Import the base vectors from qiskit.opflow library
from qiskit.opflow import Zero, One, Plus, Minus

# Example of inner product calculation with qiskit

# First example calculate the norm of |0> and |1>
# Zero and One are ket
# ~Zero and ~One are corresponding bra
# @ product between bra and ket, that is inner product
# To complete the operation @, we must evaluate it by .eval()

Norm_of_Zero = np.sqrt((~Zero @ Zero).eval())
Norm_of_One  = np.sqrt((~One @ One).eval())

# Show the reults
print("Norm of |0> =", Norm_of_Zero)
print("Norm of |1> =", Norm_of_One)

# Next we check the orthogonality between |0> and |1>
Inner_Product = (~Zero @ One).eval()

# Show the result.
print("<0|1> =", Inner_Product)


# 
# ---
# **Qiskit Example** {numref}`%s <sec-purestates>`.2 &nbsp;  Let us construct another orthonormal basis set $|L\rangle = \frac{1}{\sqrt{2}}\left(|0\rangle + i |1\rangle\right)$ and $|R\rangle = \frac{1}{\sqrt{2}}\left(|0\rangle - i |1\rangle\right)$.  Notice the complex unit $i$ on $|1\rangle$.

# In[2]:


# Let us try more complicated case.
# we will solve the above exercise problem using Qiskit

# import numpy 
import numpy as np

# imaginary unit "i" is "1j" in python.
L = (Zero + 1j* One)/np.sqrt(2)
R = (Zero - 1j* One)/np.sqrt(2)

print( "<L|L> =",(~L@L).eval() )
print( "<R|R> =",(~R@R).eval() )
print( "<L|R> =",(~L @ R).eval() )

# Anser should be 0 since they are orthogonal.


# :::{admonition} Python note: Complex numbers
# 
# In `python`, a complex number is expressed as $2 + 3j$.  Note that symbol $j$ is used instead of $i$.  The imaginary unit $i$ is $1j$.  Notice $1$ in from of $j$.  $j$ must be used with a regular number.  $j$ alone causes an error.
# ::: 

# 
# ---
# **Exercise** {numref}`%s <sec-purestates>`.2 &nbsp;  
# 
# 1. Confirm that base vectors `Plus` and `Minus` are orthonormal using Qiskit.
# 2. Calculate the inner product between `One` and `Minus` by hand and confirm your answer using Qiskit.
# 

# 
# ---
# **Exercise** {numref}`%s <sec-purestates>`.2 &nbsp;  In the previous example, change the order of rotations to `rx`, `rz`, `ry`.  Does it come back to the initial state?  

# 
# ---
# Last modified: 08/31/2022

# In[ ]:




