#!/usr/bin/env python
# coding: utf-8

# (sec-change-basis)=
# # Change of basis sets
# 
# Although the computational basis $\{|0\rangle,|1\rangle\}$ is the primary basis set, $\{|+\rangle,|-\rangle\}$ and $\{|L\rangle,|R\rangle\}$ are often used when quantum algorithms are developed.  A few examples are given in this section.
# 
# The difference is only the basis set and the coefficients are the same in all three cases.  Then, there are simple relation among the gates.
# 
# $$
# G' = H \cdot G \cdot H, \quad G'' = S \cdot G' \cdot S^\dagger
# $$

# ## Transformation of gates
# 
# Suppose that gates $G$, $G'$, and $G''$ transform state vectors as 
# 
# $$
# G \left (a_0 |0\rangle + a_1 |1\rangle\right) = b_0 |0\rangle + b_1 |1\rangle
# $$
# 
# $$
# G' \left (a_0 |+\rangle + a_1 |-\rangle\right) = b_0 |+\rangle + b_1 |-\rangle
# $$
# 
# $$
# G'' \left (a_0 |L\rangle + a_1 |R\rangle\right) = b_0 |L\rangle + b_1 |R\rangle
# $$
# 
# The difference is only the basis set and the coefficients are the same in all three cases.  Then, there are simple relation among the gates.
# 
# $$
# G' = H \cdot G \cdot H, \quad G'' = S \cdot G' \cdot S^\dagger
# $$

# **Example 1**  Swapping coefficients
# 
# Suppose that a state vector is given in $\{|+\rangle,|-\rangle\}$ basis as $c_0 |+\rangle + c_1 |-\rangle$. We want to swap the coefficients. 
# 
# $$
# c_0 |+\rangle + c_1 |-\rangle \quad \xrightarrow{?} \quad c_1 |+\rangle + c_0 |-\rangle
# $$
# 
# What gate do we need?  In {numref}`sec-xgate`, we learned that XGate swaps the coeeficients in the computational basis. Recalling that HGate switches basis set between $\{|+\rangle,|-\rangle\}$ and $\{|0\rangle,|1\rangle\}$.  $H \cdot X \cdot H$ should do the job.  Let us try it.
# 
# $$
# c_0 |+\rangle + c_1 |-\rangle \quad \xrightarrow{H} \quad c_0 |0\rangle + c_1 |1\rangle
# \quad \xrightarrow{X} \quad  c_1 |0\rangle + c_0 |1\rangle \quad \xrightarrow{H} \quad
# c_1 |+\rangle + c_0 |-\rangle
# $$
# 
# In {numref}`sec-hgate`, we derived $Z=H \cdot X \cdot H$.  Hence, ZGate is the best solution. This example tells us that there are many ways to do the same transformation.  However, finding the simplest combination of gates is not trivial.

# 
# ---
# **Exercise** {numref}`%s <sec-change-basis>`.1&nbsp;  Show that $S \cdot H \cdot S^\dagger$ works as desired.

# 
# **Exercise** {numref}`%s <sec-change-basis>`.2&nbsp;  In {numref}`sec-sxgate`, we noticed that SGate and SXGate work in the same way but in different basis sets.  Show that $SX = H \cdot S \cdot H$ and $SX^\dagger = H \cdot S^\dagger \cdot H$.
# 

# 
# ---
# **Example 2** addition and subtraction of the coefficients
# 
# We want to find a gate that transforms a state vector as
# 
# $$
# c_0 |+\rangle + c_1|-\rangle \quad \xrightarrow{?} \quad \frac{1}{\sqrt{2}}\left(c_0+c_1\right)|+\rangle + \frac{1}{\sqrt{2}}\left(c_0-c_1\right)|-\rangle 
# $$
# 
# Recalling that HGate does the same for the computational basis.  Hgate itself is also used to change the basis set. Hence, $H \cdot H \cdot H$ will do the job. However, we recall that $H^2=I$.  Hence, $H \cdot H \cdot H=H$.  Interestingly, HGate works in the same way on the two basis sets.
# 
# Similarly, we want to find a gate that transforms a state vector in $\{|L\rangle,|R\rangle\}$ basis as
# 
# $$
# c_0 |L\rangle + c_1|R\rangle \quad \xrightarrow{?} \quad \frac{1}{\sqrt{2}}\left(c_0+c_1\right)|L\rangle + \frac{1}{\sqrt{2}}\left(c_0-c_1\right)|R\rangle 
# $$
# 
# SGate and SdgGate swap the basis set between $\{|+\rangle,|-\rangle\}$ and $\{|L\rangle,|R\rangle\}$. We also know that HGate works for $\{|+\rangle,|-\rangle\}$.  Hence, $S \cdot H \cdot S^\dagger$ should work for $\{|L\rangle,|R\rangle\}$.
# 

# 
# ---
# **Exercise** {numref}`%s <sec-change-basis>`.3&nbsp;  Show that $S \cdot H \cdot S^\dagger$ works as desired.
# 
# ---
# 

# (ex-relative phase)=
# ## Qiskit Example:  Finding the relative phase.
# 
# This is
# Consider a superposition state, 
# 
# $$
# |\phi\rangle = \frac{1}{\sqrt{2}}\left(|0\rangle + e^{i \phi} |1\rangle\right)
# $$
# 
# We want to find out the value of the relative phase angle $\phi$.  If we measure this state, we only get the modulus of the coefficients and thus no information on the phase is obtained.  In physics, the phase difference between two waves is measured by the interference pattern.  Here, we use the same method.  Applying the $H$ gate, the state is transformed to
# 
# $$
# H |\psi\rangle = \frac{1}{2}\left(1+e^{i \phi}\right) |0\rangle + \frac{1}{2}\left(1-e^{-i \phi}\right) |1\rangle
# $$
# 
# Now, we measure this state.  The probabilities to find $|0\rangle$ and $|1\rangle$ are
# 
# $$
# p_0 = \frac{1}{2}\left(1+\cos \phi\right), \qquad p_1 = \frac{1}{2}\left(1-\cos \phi\right)
# $$
# 
# The difference $\delta_x = p_0 - p_1 = \cos\phi$ which gives the real part of $e^{i ]phi}$.
# 
# Next, we measure the imaginary part by using the $y$-basis.  Applying $H S^\dagger$, the state is transformed as
# 
# $$
# H S^\dagger |\psi\rangle = \frac{1}{2}\left(1- i e^{i \phi}\right) |0\rangle + \frac{1}{2}\left(1+ i e^{-i \phi}\right) |1\rangle
# $$
# 
# The outcome of the measurement is 
# 
# $$
# p_0 = \frac{1}{2}\left(1+\sin \phi\right), \qquad p_1 = \frac{1}{2}\left(1-\sin \phi\right)
# $$
# 
# and thus $\delta_y=p_0-p_1=\sin \phi$.  Now, we know $e^{i \phi}$.
# 
# Let us try this method using Qiskit.
# 
# First we create the superposition state using $H$ and $P$ gates.  We set $\phi=\pi/3$.  The goal of the quantum computation is to obtain this angle by quantum measurement.  In the following quantum circuit, we use two qubits, one for the real part and the other for the imaginary part.
# 

# In[1]:


import numpy as np

from qiskit import *

cr=ClassicalRegister(2,'c')
qr=QuantumRegister(2,'q')
qc=QuantumCircuit(qr,cr)

# Generation of the superposition state
qc.h([0,1])
qc.p(np.pi/3,[0,1])
qc.barrier([0,1])

# real part
qc.h(0)

# imaginary part
qc.sdg(1)
qc.h(1)

# measure the both qubits
qc.measure(qr,cr)

qc.draw()


# In[2]:


# Chose a general quantum simulator without noise.
# The simulator behaves as an ideal quantum computer.
backend = Aer.get_backend('qasm_simulator')

# set number of tries
nshots=10000

# execute the quantum circuit and store the outcome
job = backend.run(qc,shots=nshots)

# extract the result
result = job.result()

# count the outcome
counts = result.get_counts()

# calculate the marginal probability for the imaginry part
p0=counts['00'] + counts['01']
p1=counts['10'] + counts['11']
dy=(p0-p1)/(p0+p1)

# calculate the marginal probability for the real part
p0=counts['00'] + counts['10']
p1=counts['01'] + counts['11']
dx=(p0-p1)/(p0+p1)

# evaluate the phase angle
phi=np.arctan2(dy,dx)
print("measured phi = {:6.3f}".format(phi))
print("original phi = {:6.3f}".format(np.pi/3))
print("error =  {:6.3f}".format(phi - np.pi/3))


# The result of quantum computing is quite close to the original phase angle.

# 
# ---
# Last modified: 07/09/2022

# In[ ]:




