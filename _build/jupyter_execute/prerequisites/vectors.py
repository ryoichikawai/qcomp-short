#!/usr/bin/env python
# coding: utf-8

# (sec-statevectors)=
# # State vectors

# The theory of quantum mechanics is built on linear algebra.  I hope that you have studied elementary linear algebra prior to this book.  While I briefly introduce necessary mathematics, I expect you to review the theory of complex vector spaces (Hilbert spaces).  You can find a good summary of mathematics is also given in this book
# 
# * J. Audretsch: *Entangled Systems - New Directions in Quantum Physics* (Wiley-VCH, 2007) 
# 
# which I already recommended in the previous section.  
# 
# If you want to practice mathematical calculation in depth, there is an exercise book on quantum computation.
# 
# * W.-H. Steeb and Y. Hardy: *Problems and Solutions in Quantum Computing and Quantum Information* (World Scientific, 2012).
#  

# The following is a summary of Hilbert space using abstract mathematical expressions.  The ket and bra notation of vectors may be new to you.  Otherwise, it is just a standard linear algebra.  I will discuss each item in later chapters with practical examples for quantum computation.  For now, refresh your understanding of linear algebra.

# ## Ket and bra
# 
# The state of a quantum object is mathematically described by a complex vector in a *Hilbert space*, which is called *state vector*. The state vector is denoted as $|\bullet\rangle$, which is called *ket vector* or simply *ket*.  "$\bullet$" in the ket can be any symbol representing the state.  For example, an electron in a spin-up state is commonly expressed by $\ket{\uparrow}$. We could use $|$&hearts; $\rangle$, $|$&spades;$\rangle$, $|$&diams;$\rangle$, $|$&clubs;$\rangle$ to express the states of quantum cards (if they exist.)  We often write an arbitrary state as $| \psi\rangle$. 
# 
# For every ket $|\psi\rangle$, there is a corresponding complex vector $\langle\psi|$, which is known as *bra vector* or just *bra*. Mathematically, $\langle\psi|$ is the _adjoint_ or _dual_ of $|\psi\rangle$. 
# The corresponding bra with the same symbol as a ket represents the same state of the qubit.  For example, both $|\uparrow\rangle$ and $\langle\uparrow|$ represent the same spin-up state.
# We need bra vectors to compute inner products (See subsection {ref}`subsec-innerproduct`).
# 
# You are familiar with Euclidean vectors such as forces and velocities and the rules of calculation with them. 
# Since kets and bras are vectors, they share the same mathematical operations with the Euclidean vectors, namely two basic mathematical operations, *addition* $|a\rangle+|b\rangle$ and *scalar mulitplication* $\lambda |a\rangle$ ($\lambda$ is a complex number).  The regular rules of calculation are listed below.  The dual of the operations are $\langle a| + \langle b|$ and $\langle a | \lambda^*$ where $\lambda^*$ is a complex conjugate of $\lambda$. 

# ## Addition
# The following statements are valid for any $|a\rangle$, $|b\rangle$, $|c\rangle$ in the same vector space.
# The same rules are applied to bra vectors.
# 
# | rule | mathematical expression |
# | :---: | :---: |
# | closure | $\lvert a \rangle + \lvert b\rangle$ is a ket in the same vector space. |
# | commutativity | $\lvert a \rangle + \lvert b\rangle = \lvert b \rangle + \lvert a\rangle$ | 
# | associativity | $(\lvert a \rangle + \lvert b\rangle) +  \lvert c\rangle =  \lvert a\rangle + (\lvert b \rangle + \lvert c\rangle)$ |
# | null vector   | There exists null vector $0$ such that $\lvert a \rangle + 0 = \lvert a \rangle$ |
# | inverse       | There exists inverse vector $\lvert -a \rangle$ such that $\lvert a \rangle + \lvert -a \rangle = 0$. <br/> In a common expression, $\lvert -a \rangle = - \lvert a \rangle$  |

# ## Scalar multiplication
# 
# The following statements are valid for any $|a\rangle$ and $|b\rangle$ in the same vector space and any complex numbers $\alpha$ and $\beta$.
# The same rules are applied to bra vectors.
# 
# | rule | mathematical expression |
# | :---: | :---: |
# | closure | $\alpha \lvert a \rangle$ is another ket in the same vector space |
# | vector  distributivity | $\alpha (\lvert a \rangle + \lvert b\rangle) = \alpha \lvert a \rangle + \alpha \lvert b \rangle$ |
# | scalar  distributivity | $(\alpha + \beta) \lvert a \rangle = \alpha \lvert a \rangle + \beta \lvert a \rangle$ |
# | associativity | $\alpha (\beta \lvert a \rangle) = (\alpha\beta) \lvert a \rangle$|
# | identity |  There exists identity $I$ such that $I \lvert a \rangle = \lvert a \rangle$  (We write $I$ as $1$.) |

# ## Superposition
# 
# Combining addition and scalar multiplication, we can construct a superposition of vectors,
# 
# $$
# |\psi\rangle = \alpha |a\rangle + \beta |b\rangle
# $$
# 
# where $\alpha$ and $\beta$ are complex numbers.  The corresponding bra is
# 
# $$
# \langle \psi | = \langle a | \alpha^* + \langle b | \beta^*.
# $$
# 
# Notice that the coefficients are complex conjugate of the original ones in the ket.

# ___  
# 
# __Exercise__ {numref}`%s <chap-prerequisites>`.1 &nbsp;  Consider a superposition state $\alpha |a\rangle + e^{i \theta} \alpha |b\rangle$ where $\theta$ is real.  Find the corresponding bra vector.  
# 
# ___

# (subsec-innerproduct)=
# ## Inner product
# 
# In the Euclidean vector space, an inner product (dot product) $\,\vec{a} \cdot \vec{b}\,$ is real and $\,\vec{a} \cdot \vec{b} = \vec{b} \cdot \vec{a}$. The inner product in a Hilbert space differs in two points. Firstly, the inner product in a Hilbert space $\langle a|b \rangle$ is complex.  Secondly, the inner product is not symmetric between $a$ and $b$, that is $\langle a|b \rangle \ne \langle b|a \rangle$. Instead, the two inner products are complex conjugate to each other as $\langle a|b \rangle^* = \langle b|a \rangle$.
# 
# The inner product between $|c \rangle$ and a superposition state $|\psi \rangle = \alpha |a \rangle + \beta |b \rangle$ can be computed with the distribution rule
# 
# $$\begin{eqnarray}
# \langle c|\psi \rangle &=& \bra{c} \left(\alpha |a \rangle + \beta |b \rangle\right) = \alpha \langle c|a \rangle + \beta \langle c|b \rangle\\
# \langle \psi|c \rangle &=& \left(\alpha^* \langle a | + \beta^* \langle b |\right) \ket{c} = \alpha^* \langle a|c \rangle + \beta^* \langle b|c \rangle.
# \end{eqnarray}
# $$
# 

# ___
# __Exercise__ {numref}`%s <chap-prerequisites>`.2 &nbsp; 
# 1. In the above example of inner product, show that $\langle c|\psi \rangle^* = \langle \psi|c \rangle$. (otherwise, the distribution rule does not work.)  
# 2.  Show that $\langle \psi|\psi \rangle$ is real  for any $|\psi\rangle$.
# ___

# ## Orthogonality
# 
# The inner product of two Euclidean vectors $\vec{a}$ and $\vec{b}$ may be expressed as $\vec{a}\cdot\vec{b} = a b \cos\theta$ where $\theta$ is the angle between the two vectors. When $\theta = \pm \frac{\pi}{2}$, the inner product vanishes.  Then, the two vectors are said to be orthogonal. Although no such angle can be defined between two kets, we say that $|a\rangle$ and $|a\rangle$ are _orthogonal_ if $\langle a | b \rangle = 0$.

# ___
#   $|q\rangle$ and $|b\rangle$ are normalized and orthogonal to each other and have the. SHow that $|\psi\rangle = |a\rangle + i |b \rangle$ and $|\varphi\rangle = |a\rangle - i |b \rangle$. are orthogonal. if  

# ## Norm and normarization
# 
# Recall that the norm (magnitude) of an Euclidean vector is defined by $\|\vec{a}\| = \sqrt{\vec{a}\cdot\vec{a}}$.
# The norm of $\ket{a}$ is defined in the same way.  Replacing the dot product with inner product, we have the norm of $|a\rangle$ as
# 
# $$
# \||a\rangle\| = \sqrt{\langle a|a \rangle}  \ge 0.
# $$
# 
# When $\langle a|a \rangle = 1$, the ket is said to be _normalized_.  Although we cannot express the ket as an arrow, physicists often use an imaginary arrow to represent a ket and the norm can be viewed as the length of the imaginary arrow.  This analogy works quite well.  So, the normalized ket is much like a unit vector. 

# ___
# 
# __Exercise__ {numref}`%s <chap-prerequisites>`.3 &nbsp;  Show that $|b\rangle = \frac{|a\rangle}{\sqrt{\langle a|a \rangle}}$ is normalized.     
# 
# __Exercise__ {numref}`%s <chap-prerequisites>`.4 &nbsp;   $|a\rangle$ and $|b\rangle$ are normalized and orthogonal to each other. Show that $|\psi\rangle = |a\rangle + i |b \rangle$ and $|\varphi\rangle = |a\rangle - i |b \rangle$ are orthogonal.  
# 
# ___

# ## Global phase
# 
# It is easy to show that if $|\psi\rangle$ is normalized, $e^{i \theta}|\psi\rangle,\,\theta \in \mathbb{R}$ is also normalized.
# Although they are mathematically different, the two kets corresponds to the same physical state.  The factor $e^{i \theta}$ is known as global phase and does not play any significant role in physics.  Hence, we can ignore it.  Quantum computation can be simplified by utilizing the freedom to chose any global phase.

# ## Basis sets
# 
# In a freshman physics course, perhaps you expressed a force vector in the three-dimensional Euclidean space as $\vec{F} = F_x \vec{i} + F_y \vec{j} + F_z \vec{k}$.  In fact, any vector can be expressed in the same way using the basis vectors  $\vec{i}$, $\vec{j}$ and $\vec{k}$.  These three vectors are orthogonal to each other and their magnitude is 1.  Hence they are *orthonormal basis*.
# 
# 
# Similarly, a $n$-dimensional Hilbert space is _spanned_ by a basis set $\{\ket{e_0}, \ket{e_1}, \cdots, \ket{e_{n-1}}\}$.  We assume that the basis vectors are normized and orthogonal to each other.  Such basis set is called _orthonormal basis_ and the basis vectors satisfy
# 
# $$
# \langle e_i | e_j \rangle = \delta_{ij}
# $$(orthonormal)
# 
# where $\delta_{ij}$ is the usual Kronecker's delta.
# 
# The basis vectors are _linearly independent_ and _complete_.  That means that any ket vector  can be expressed as a linear combination of the base vectors as
# 
# $$
# |\psi\rangle = c_0 |e_0\rangle + c_1 |e_1\rangle  \cdots c_{n-1} |e_{n-1}\rangle = \sum_{i=0}^{n-1} c_i |e_i\rangle
# $$ (basis_expansion)
# where $c_i$ is complex.
# Using the orthonormality condition {eq}`orthonormal` , we can find the expansion coefficient as $c_i=\langle  e_i|\psi \rangle$ which is a crucial quantity in quantum mechanics.
# 
# 
# The corresponding bra vector are expressed as
# 
# $$
# \langle \psi| = c^*_0 \langle e_0| + c^*_1 \langle e_1|  \cdots c^*_{n-1} \langle e_{n-1}| = \sum_{i=0}^{n-1} c^*_i \langle e_i|.
# $$
# 
# Notice that the expansion coefficients of the bra are complex conjugate of the coefficients of the ket.
# 
# If $|\psi\rangle$ is normalized, the coefficients is normalized as $\sum_j |c_j|^2 = 1$.
# 

# ## Completeness
# 
# In Equation {eq}`basis_expansion` we expanded an arbitrary vector in a complete basis set.  The following _closure relation_ guarantees the completeness.
# 
# $$
# |e_0\rangle\langle e_0| + |e_1\rangle\langle e_1| + \cdots + |e_{n-1}\rangle\langle e_{n-1}| = I
# $$ (completeness)
# 
# where $\{|e_i\rangle\}$ is an orthonormal basis.  $|e_i\rangle\langle e_i|$ is a kind of operator called _projection operator_, which we study in XXX.  It acts on a ket as follows:
# 
# $$
# (|e_i\rangle\langle e_i|)\, |\psi\rangle =  |e_i\rangle (\langle e_i|\psi\rangle) = c_i e_i\rangle 
# $$
# where $c_i = \langle e_i|\psi\rangle$.

# In[ ]:




