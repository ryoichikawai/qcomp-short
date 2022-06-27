#!/usr/bin/env python
# coding: utf-8

# (sec-single-qubit)=
# # Single qubit
# 

# Quantum computers store information in a two-dimensional Hilbert space called a qubit.   In this section, I will introduce mathematical description of a single qubit.

# ## Pure states
# 
# In ideal situations, the state of a qubit is specified by a ket vector in a two-dimensional Hilbert space.  Unless otherwise is specified, state vectors are assumed to be normalized. That is $\langle \psi | \psi \rangle = 1$ (See {numref}`sec-statevectors`). 
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

# ## The basis sets in Qiskit
# 
# In Qiskit, the basis sets $\{|0\rangle, |1\rangle\}$ and $\{|+\rangle, |-\rangle\}$ are predefined.  See the following Qiskit note. 

# :::{admonition} Qiskit note: Computational Basis
# :class: tip
# 
# `qiskit.opflow` module allows us to compute basic quantities using expressions very similar to the original methematical expressions.  Here are the correspondence between mathematical expressions and `opflow` expression.
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

# **Qiskit Example** {numref}`%s <sec-single-qubit>`.1 &nbsp; The orthonormality of the computational basis set is tested in Qiskit.

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

# ___
# **Exercise** {numref}`%s <sec-single-qubit>`.1 &nbsp;  
# 
# 1. Confirm that base vectors `Plus` and `Minus` are orthonormal using Qiskit.
# 2. Calculate the inner product between `One` and `Minus` by hand and confirm your answer using Qiskit.
# ___

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
# 
# $$
# \ket{\psi} = \cos\left(\frac{\theta}{2}\right) \ket{0} + \sin\left(\frac{\theta}{2}\right) e^{i \phi} \ket{1},\quad 0 \le \theta \le \pi, \, 0 \le \phi < 2 \pi .
# $$(eq-blochvector)
# 
# This expression suggests that any pure state can be map to a point on the surface of a unit sphere using spherical coordinates $\theta$ and $\phi$.   The north pole of the sphere ($\theta=0$) corresponds to $\ket{0}$ and the south pole to $\ket{1}$ (recall that the global phase $e^{i \phi}$ can be omitted.  When $\theta = \frac{\pi}{2}$ and $\phi=0$, we obtain $|+\rangle$ and when $\theta = \frac{\pi}{2}$ and $\phi=\pi$, we have $|-\rangle$. 
# 
# The sphere is known as *Bloch sphere* and the arrow from the center of the sphere to the point on the surface is called *Bloch vector*. 

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

# **Qiskit Example** {numref}`%s <sec-single-qubit>`.3 &nbsp; The following example plots the Bloch vectors of $|0\rangle$, $|1\rangle$, and $|\pm\rangle$.  To plot all of them at once, we need to use a tensor product of all vectors.  In Qiskit, tensor product is done by "^".

# In[3]:


# Example of statevector
# import Statevector class
from qiskit.visualization import plot_bloch_multivector

# import basic state vectors
from qiskit.opflow import Zero, One, Plus, Minus

plot_bloch_multivector(Zero^One^Plus^Minus)


# **Qiskit Example** {numref}`%s <sec-single-qubit>`.4 &nbsp; Plot the Bloch vectors of the states $|L\rangle$ and $|R\rangle$ discuessed in **Qiskit Example** {numref}`%s <sec-single-qubit>`.2.

# In[4]:


plot_bloch_multivector(L^R)


# **Qiskit Example** {numref}`%s <sec-single-qubit>`.5 &nbsp;  A statevector is initially $|0\rangle$.  It is rotated around $y$, $z$, and $x$ by angle $\frac{\pi}{2} for each rotation. It is done by rotation gates `ry`, `rz`, and `rx`.  Construction of quantum circuits will be discussed later in great detail.   The Bloch vector should come back to the starting point. See the animation.

# In[5]:


get_ipython().run_cell_magic('capture', '', '# The output block is disabled.\n\n# load numpy and qiskit\nimport numpy as np\nfrom qiskit import *\n\n# create an empty quantum circuit\nqr = QuantumRegister(1)\nqc = QuantumCircuit(qr)\n\n# add rotation gates to the circuit\nqc.ry(np.pi/2,0)\nqc.rz(np.pi/2,0)\nqc.rx(np.pi/2,0)\n\n# load the visdualization tool\nfrom qiskit.visualization import visualize_transition\n\n# generate a movie (it will be shown in next cell,\nmovie=visualize_transition(qc,fpg=50, spg=1)')


# In[6]:


# SHow the movie
movie


# **Exercise** {numref}`%s <sec-single-qubit>`.2 &nbsp;  In the previous example, change the order of rotations to `rx`, `rz`, `ry`.  Does it come back to the initial state?

# ## Matrix representation
# 
# Kets are vectors defined in an abstract mathematical form.  Computers won't understand it directly. So far we used kets predefined in Qiskit.  In principle, you can construct any ket using the predefined basis vectors.  However, it is convenient if we can express kets directly without using the basis vectors. In other words, we need a simple expression of a ket in a form computers can understand.  The matrix expression (see xxx) is the solution.
# 
# When we use matrix representation, the computation basis is assumed unless otherwise is stated.  The state vector {eq}`eq-qubit-purestate` is $|\psi\rangle \doteq [c_0, c_1]$ in the matrix expression. The matrix representation of the computational basis is $|0\rangle = [1,0]$ and $|1\rangle = [0,1]$.
# 
# Qiskit has several different ways to express the state vector depending on the tasks you are working on.
# 
# 1. Statevector class
# 2. VectorSTateFn class
# 3. DictStateFn class

# ##  Statevector class
# 
# `Statevector` class is defined in `qiskit.quantum_info` library.  Its usage is described in 
# [API reference: Statevector (in qiskit.quantum_info)](https://qiskit.org/documentation/stubs/qiskit.quantum_info.Statevector.html#qiskit.quantum_info.Statevector).  
# 
# The following example generates a state vector of qubit in the way Qiskit understands.

# **Qiskit Example** {numref}`%s <sec-single-qubit>`.6 &nbsp;  Let us construct the general qubit state {eq}`eq-blochvector` in `Statevector` class.

# In[7]:


import numpy as np
from qiskit.quantum_info import Statevector

# set parameter values
theta = np.pi/5
phi=2*np.pi/3
c0=np.cos(theta)+0j
c1=np.sin(theta)*np.exp(phi*1j)
psi = Statevector([c0,c1])
psi.draw('bloch')


# The `Statevector` contains more information than the matrix expression. As shown below, it includes the dimension of Hilbert space.  In the current example, `dim=(2,)` means the statevector belongs to $\mathbb{C}^2$.

# In[8]:


# show the whole contents in the statevector
psi


# To get the matrix out of the `Statevector`, use an attribute `data` as shown below.  The output is numpy ndarray.  The matrix elements can be accessed by the standard method.

# In[9]:


psi_in_matrix = psi.data

# check the type of the matrix
print("type of matrix =",type(psi_in_matrix))

# output the whole matrix
print("matrix =",psi_in_matrix)

# output the individual matrix elements
print("c_0=",psi_in_matrix[0])
print("c_1=",psi_in_matrix[1])


# `Statevector` class behaves as mathematical vector.  Hence, addition among class objects and scalar multiplication to them work as expected. See the following example.

# In[10]:


# generate |0> and |1> as statevector class
ket0 = Statevector([1,0])
ket1 = Statevector([0,1])

# construct cos(pi/4) |0> + sin(pi/4) |1>
psi = np.cos(np.pi/4) * ket0 + np.sin(np.pi/4) * ket1

# print out the result as latex equation
psi.draw('latex')


# `Statevector` class provides many useful methods and attributes (See [API reference: Statevector](https://qiskit.org/documentation/stubs/qiskit.quantum_info.Statevector.html#qiskit.quantum_info.Statevector)).    We will be using some of them in later chapters.  I will introduce them as needed.

# ## VectorStateFn class
# 
# `VectorStateFn` class deals with state vectors in matrix format much like `StateVector` class does.  In fact, `VectorStateFn` class expresses state vectors exactly in the same way as `Statevector` class.  However, there are some difference bettween them.  As shown bellow, `VectorStateFn` wraps around `Statevector` along with a couple of more information about the vector.
# 
# The `VectorStateFn` class is defined in `qiskit.opflow.statefn` library and its usage is given in
# [API Document: VectorStateFn](https://qiskit.org/documentation/stubs/qiskit.opflow.state_fns.VectorStateFn.html#qiskit.opflow.state_fns.VectorStateFn).

# The following example shows that `VectorStateFn` `coeff` and `is_measurement` variables in addition to a Statevector class object.  WE will discuss them later.  For now, we focus on the matrix representation.  You can extract `Statevector` out of `VectorStateFn` using `primitive` attribute.

# In[11]:


# Load VectorStateFn class
from qiskit.opflow.state_fns import VectorStateFn

# contruct VectorStateFn object in the same way as Statevector object
psi = VectorStateFn([c0,c1])

# Show its content. Notice that it contains Statevector in it.
psi


# In[12]:


# Extract Statevector out of VectorStateFn using primitive attribute
psi.primitive


# ---
# 
# Addition and scalar multiplication work for `VectoStateFn` objects as it should be.

# In[13]:


# generate |0> and |1> as statevector class
ket0 = VectorStateFn([1,0])
ket1 = VectorStateFn([0,1])

# construct cos(pi/4) |0> + sin(pi/4) |1> and print the statevector via `Statevector` class
psi = np.cos(np.pi/4) * ket0 + np.sin(np.pi/4) * ket1
psi.primitive.draw('latex')


# The predefined basis vector, `Zero`, `One`, `Plus`, and `Minus` are not `Statevector` class object.

# In[14]:


from qiskit.opflow import Zero, One, Plus, Minus

print(One)
Statevector(One.to_matrix())


# In[15]:


print(Zero)


# In[16]:


print(Plus)


# In[ ]:




