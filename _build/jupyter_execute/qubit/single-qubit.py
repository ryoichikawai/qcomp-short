#!/usr/bin/env python
# coding: utf-8

# (sec-single-qubit)=
# # Single qubit
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
# $$(eq-qubit-purestate)
# 
# where $| 0 \rangle $ and $| 1 \rangle$ are orthonormal basis vectors satisfying $\langle 0 | 0 \rangle = \langle 1 | 1 \rangle = 1$ and $\langle 0 | 1 \rangle = \langle 1 | 0 \rangle = 0$.  The coefficients $c_0$ and $c_1$ are complex numbers. The normalization requirement is satisfied if $|c_0|^2 + |c_1|^2 = 1$.
# 
# This orthonormal complete basis set $\{|0\rangle, |1\rangle\}$ is known as *computational basis* which is the default basis in quantum computing.  However, this basis set do not represent any particular physical basis set.  In real quantum computers,  a qubit can be realized, for example, by an electron spin, $|0\rangle \equiv | \uparrow \rangle$ and $|1\rangle \equiv |\downarrow \rangle$ or the polarization of a photon, $|0\rangle \equiv | H \rangle$ (horizontal polarization) and $|1\rangle \equiv | V \rangle$ (vertical polarization).  By using the computational basis set, we don't have to worry about what type of hardware is used.  The mathematical expression based on the computational basis can be applied to all of qubit-based quantum computers.

# ## The basis sets in Qiskit
# 
# In Qiskit, the basis sets $\{|0\rangle, |1\rangle\}$ and $\{|+\rangle, |-\rangle\}$ are predefined.  See the following Qiskit note. 

# :::{admonition} Qiskit note: Computational Basis
# :class: tip
# 
# The `qiskit.opflow` library provides us with basic tools to describe quantum mechanics using expressions very similar to the original methematical expressions.  Here are the correspondence between mathematical expressions and `opflow` expressions.
# 
# > $\ket{0} \quad \Rightarrow \quad$ `Zero`  
# > $\ket{1} \quad \Rightarrow \quad$ `One`  
# > $\ket{+} \quad \Rightarrow \quad$ `Plus`  
# > $\ket{-} \quad \Rightarrow \quad$ `Minus`     
# 
# The vector with "~" indicates bra.  For example,  
# > $\bra{0} \quad  \Rightarrow \quad$ `~One` 
# 
# The regular addition works.
# > $\ket{0} + \ket{1} \quad \Rightarrow \quad$  `Zero + One`
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
# **Qiskit Example** {numref}`%s <sec-single-qubit>`.1 &nbsp; Let us check the orthonormality of the computational basis set in Qiskit.

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
# **Qiskit Example** {numref}`%s <sec-single-qubit>`.2 &nbsp;  Let us construct another orthonormal basis set $|L\rangle = \frac{1}{\sqrt{2}}\left(|0\rangle + i |1\rangle\right)$ and $|R\rangle = \frac{1}{\sqrt{2}}\left(|0\rangle - i |1\rangle\right)$.  Notice the complex unit $i$ on $|1\rangle$.

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
# **Exercise** {numref}`%s <sec-single-qubit>`.1 &nbsp;  
# 
# 1. Confirm that base vectors `Plus` and `Minus` are orthonormal using Qiskit.
# 2. Calculate the inner product between `One` and `Minus` by hand and confirm your answer using Qiskit.
# ---

# ## Bloch sphere
# 
# While Eq. {eq}`eq-qubit-purestate` can describe any qubit state, there is a better expression suitable for visualizing the qubit state.
# Writing the complex coefficient in the polar expression,
# $c_0 = r_0 e^{i \phi_0}$ and $c_1 = r_1 e^{i \phi_1}$ where $r_i$ and $\phi_i$ are modulus and argument. Then, we remove a global phase as 
# 
# $$
# \ket{\psi} = r_0 e^{i \phi_0} \ket{0} + r_1 e^{i \phi_1} \ket{1} = e^{i \phi_0} \left( r_0  \ket{0} + r_1 e^{i (\phi_1-\phi_0)} \ket{1} \right) \simeq r_0  \ket{0} + r_1 e^{i \theta} \ket{1}
# $$
# 
# where $\phi=\phi_1-\phi_0,\ \phi \in [0, 2\pi)$ and "$\simeq$" means "equivalent up to global phase".  Now, the normalization condition becomes $r_0^2 + r_1^2 = 1$.  Since $r_0$ and $r_1$ are positive, we can write them as $r_0 = \cos\left(\frac{\theta}{2}\right)$ and $r_1 = \sin\left(\frac{\theta}{2}\right)$ with $0 < \theta < \pi$.  Now the general qubit state is written as
# 
# $$
# \ket{\psi} = \cos\left(\frac{\theta}{2}\right) \ket{0} + \sin\left(\frac{\theta}{2}\right) e^{i \phi} \ket{1},\quad 0 \le \theta \le \pi, \, 0 \le \phi < 2 \pi .
# $$(eq-blochvector)
# 
# This expression suggests that any pure state can be map to a point on the surface of a unit sphere using spherical coordinates $\theta$ and $\phi$.   The north pole of the sphere ($\theta=0$) corresponds to $\ket{0}$ and the south pole ($\theta=\pi$) to $\ket{1}$ (recall that the global phase $e^{i \phi}$ can be omitted.  When $\theta = \frac{\pi}{2}$ and $\phi=0$, we obtain $|+\rangle$ and when $\theta = \frac{\pi}{2}$ and $\phi=\pi$, we have $|-\rangle$. 
# 
# The sphere is known as *Bloch sphere* and the arrow from the center of the sphere to the point on the surface is called *Bloch vector*. Each Bloch vector corresponds to a qubit state. 

# :::{admonition} Qiskit note: Bloch sphere
# :class: tip
# 
# Qiskit provides four tools to visualize the Bloch sphere and vector.
# 
# 1. Use `plot_bloch_vector` in `qiskit.visuakization` if $\theta$ and $\phi$ are known.
# > `plot_bloch_vector([r,theta,phi], coord_type='spherical', figsize=(w,h) )`  
# [API reference:plot_bloch_vector](https://qiskit.org/documentation/stubs/qiskit.visualization.plot_bloch_vector.html)
# 
# 2. Use `plot_bloch_multivector` if a state vector is known.  
# > `plot_bloch_multivector(state)`  
# > `state` is a quantum state. Various format is allowed, including Statevector class objects.
# For other optional arguments.  
# [API reference:plot_bloch_multivector](https://qiskit.org/documentation/stubs/qiskit.visualization.plot_bloch_multivector.html)
# 
# 3. Use `draw` method associated with `statevector` class
# > psi`.draw('mpl')`  
# > where psi is a `staetvector` class object.  `mpl` specifies the use of `matplotlib` module.  This method is just a front end to plot-bloch-multivector.   
# [API reference:Statevector.draw](https://qiskit.org/documentation/stubs/qiskit.quantum_info.Statevector.draw.html#qiskit.quantum_info.Statevector.draw)
# 
# 4. We can even draw evolution of the Bloch vector as a movie using `visualize_transition`.
# > visualize_transition(qc,fpg=50, spg=1)
# > where `qc` is a quantum circuit (I will explain it later.)   See the following documentation for other parameters.
# [API reference:visualize_transition](https://qiskit.org/documentation/stubs/qiskit.visualization.visualize_transition.html)
# 
# :::

# 
# ---
# **Qiskit Example** {numref}`%s <sec-single-qubit>`.3 &nbsp; The following example plots the Bloch vectors of $|0\rangle$, $|1\rangle$, and $|\pm\rangle$.  To plot all of them at once, we use a tensor product of all vectors.  In Qiskit, tensor product is done by "^".

# In[3]:


# import the visualization tool
from qiskit.visualization import plot_bloch_multivector

# import basis vectors
from qiskit.opflow import Zero, One, Plus, Minus

plot_bloch_multivector(Zero^One^Plus^Minus)


# 
# ---
# **Qiskit Example** {numref}`%s <sec-single-qubit>`.4 &nbsp; Plot the Bloch vectors of the states $|L\rangle$ and $|R\rangle$ discuessed in **Qiskit Example** {numref}`%s <sec-single-qubit>`.2.

# In[4]:


plot_bloch_multivector(L^R)


# 
# ---
# **Qiskit Example** {numref}`%s <sec-single-qubit>`.5 &nbsp;  A statevector is initially $|0\rangle$.  It is rotated around $y$, $z$, and $x$ by angle $\frac{\pi}{2} for each rotation. It is done by rotation gates `ry`, `rz`, and `rx`.  Construction of quantum circuits will be discussed later in great detail.   The Bloch vector should come back to the starting point. See the animation.

# In[5]:


get_ipython().run_cell_magic('capture', '', '# The output block is disabled.\n\n# load numpy and qiskit\nimport numpy as np\nfrom qiskit import *\n\n# create an empty quantum circuit\nqr = QuantumRegister(1)\nqc = QuantumCircuit(qr)\n\n# add rotation gates to the circuit\nqc.ry(np.pi/2,0)\nqc.rz(np.pi/2,0)\nqc.rx(np.pi/2,0)\n\n# load the visdualization tool\nfrom qiskit.visualization import visualize_transition\n\n# generate a movie (it will be shown in next cell,\nmovie=visualize_transition(qc,fpg=50, spg=1)')


# In[6]:


# Show the movie
movie


# ---
# **Exercise** {numref}`%s <sec-single-qubit>`.2 &nbsp;  In the previous example, change the order of rotations to `rx`, `rz`, `ry`.  Does it come back to the initial state?  
