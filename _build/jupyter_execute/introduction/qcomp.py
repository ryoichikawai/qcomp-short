#!/usr/bin/env python
# coding: utf-8

# (sec-qcomp)=
# # Quantum computation
# 
# Here is a brief description of quantum computer and the details will be discussed in this book.  It is necessary for you to understand the following at this stage.  Just read them and move on.

# ## Qubits
# 
# Quantum computers are also made of many small building blocks but unlike classical computers we need to use quantum mechanics to describe their state. Current quantum computers use the smallest quantum system, that is a two-dimensional Hilbert space $\mathbb{C}_2$ spanned by complex vectors $\ket{0}$ and $\ket{1}$, known as _qubit_. These two basis states looks similar to `0` and `1` for a classical bit . However, unlike the classical bit,  the state of a qubit  can be in a superposition state
# 
# $$
# \ket{\psi} = c_{0} \ket{0} + c_{1} \ket{1}
# $$ (eqn:superposition)
# 
# where $c_0$ and $c_1$ are complex number satisfying $|c_0|^2+|c_1|^2=1$ (normalization). Similarly to the classical bit, we obtain either $\ket{0}$ or $\ket{1}$  when the superposition state is measured.   We shall call them _computational basis_. However,  the state of the qubit is neither $\ket{0}$ nor $\ket{1}$  but  $\ket{0}$ AND $\ket{1}$ simultaneously. Hence, a qubit can compute two different cases at once (if a programmer is smart enough). Quantum computers exploit this superposition state.  Unlike the classical bit which has only two possible states, a qubit can take infinitely many different states since $c_0$ and $c_1$ can be any complex numbers satisfying the normalization condition. 
# 
# Obviously, quantum computers are made of many qubits.  The superposition states of the whole computer can be very complicated.  Let us consider two qubits, $q_0$ and $q_1$.  Like the classical bits, we have four possibilities $\ket{00}$, $\ket{01}$, $\ket{10}$, and $\ket{11}$.  The qubits can be in a superposition state
# 
# $$
# \ket{\Psi} = c_{00} \ket{00} + c_{01} \ket{01} + c_{10} \ket{10} + c_{00} \ket{11}
# $$
# 
# The four different possibilities are simultaneously considered in the superposition state. The complexity of the superposition state grows very rapidly as the number of qubits increases.  If there are $n$ qubits, the number of terms in the superposition state can be as many as $2^n$.   Then, $2^n$ different cases are simultaneously computed. 
# 
# In classical computers,  a bit string $b_{n-1}\, b_{n-2}\,\cdots\, b_1\, b_0$ expresses the state of the system.  In quantum computer, not a vector $\ket{q_{n-1}\,q_{n-2}\,\cdots\,q_1\,q_0}$ but their superposition expresses the state.  This is the major advantage of the quantum computer over the classical ones.

# ## Gates
# 
# Like classical computers, quantum computers changes the state of qubits as instructed. Unlike classical computers, which can only flip the bits , quantum computer can change the state of a qubit in infinitely many different ways.  Here we use also the concept of gates.  A qubit enters a gate and comes out in a different state.  In other words, a state vector of the qubit is transformed to another state vector by the gate.  In quantum mechanics, that is achieved by a unitary transformation $U$.   The transformation $\ket{\psi'}=U \ket{\psi}$ in quantum mechanics is equivalent to applying a 1-qubit gate $U$ to a qubit and expressed as
# 
# ```{figure} u1-gate.png
# ---
# name: u1-gate
# ---
# Action of one-qubit gate.
# ```
# 
# As an example, consider a Pauli operator $X\equiv \sigma_x$.  When it acts on the computational basis, $X \ket{0}=\ket{1}$ and $X \ket{1}=\ket{0}$.  Hence, it acts like $\texttt{NOT}$ in the classical computation. See the {numref}`quantum-gate-X`. The qubit can be in a superposition state.  The  classical truth table is not enough. When it acts on a general state, we get
# 
# $$
# X \ket{\psi} = c_0 X \ket{0} + c_1 X \ket{1} = c_0 \ket{1} + c_1 \ket{0} = c_1 \ket{0} + c_0\ket{1}
# $$ (Xgate)
# which actually swaps the coefficients.  The first two rows in  {numref}`quantum-gate-X` is much like the classical truth {numref}`table %s <classical-NOT>`.  The third row makes quantum computers more powerful than the classical computers.
# 
# 

# ```{table} X Gate
# :name: quantum-gate-X
# | &nbsp;| $i$ | $o$ |
# | :---:| :---: | :---: |
# | &nbsp;| $\ket{0}$ | $\ket{1}$  |
# | &nbsp;| $\ket{1}$ | $\ket{0}$  |
# | &nbsp;| $c_0 \ket{0} + c_1\ket{1}$ | $c_1 \ket{0} + c_0\ket{1}$ |
# ```

# Like classical computers, quantum computers use gates that take two qubits as input.   Two-qubit gates are also a unitary operator and express as
# 
# ```{figure} u2-gate.png
# ---
# name: u2-gate
# ---
# Action of two-qubit gate.
# ```
# 
# 
# Logically, infinitely many 1-qubit and 2-qubits gates are possible but actual devices can understand only some of them. Depending on the underlying quantum systems, the available gates are different.  However, almost any gate can be expressed equivalently with a set of other gates in principle (gate _decomposition_).  So, if a desired gate is not available on the device you are using, you  must find a decomposition of the gate.  For IBM devices, $\texttt{Qiskit}$ finds a decomposition suitable for them.  

# ## Encoding
# 
# Encoding the information of the problem to be solved to qubits in a quantum computer is not a trivial task.  Let us try to use the same encoding scheme as the above classical case: 
# 
# $$
# \texttt{False} \Rightarrow \ket{0}, \quad \texttt{True} \Rightarrow \ket{1}
# $$
# 
# This works fine.  However, there are many other encoding schemes since a qubit can take a superposition state.  For example,
# 
# $$
# \texttt{False} \Rightarrow \ket{+}\equiv \frac{1}{\sqrt{2}}\left(\ket{0}+\ket{1}\right), \quad
# \texttt{True} \Rightarrow \ket{-}\equiv \frac{1}{\sqrt{2}}\left(\ket{0}-\ket{1}\right)
# $$
# 
# is another choice. 
# 
# To make a good use of quantum computer, finding a good encoding scheme is crucial.
# 

# ## Instructions
# 
# Once an encoding scheme is chosen, we need to give a set of instructions to a quantum computer.  That is we find a set of unitary operators that are applied on qubits one after the other. Unlike classical computation, no advanced programming language is available for quantum computing.  Therefore, programmers must right  instructions the device can understand directly (similar to coding with machine or assembly language for classical computers.)  A code for quantum computation looks like
# 
# 
# ```{figure} qc.png
# ---
# name: qc-example
# ---
# An example of quantum circuit.
# ```
# 
# which is known as quantum circuit.  Each object in the circuit is a unitary gate.
# 
# The following circuit computes $x \oplus y$ using a quantum computer.
# 
# 
# ```{figure} quantum_x+y.png
# ---
# name: quantum_x+y
# ---
# Quantum computation of $x \oplus y$.
# ```
# 
# The gate in the circuit is known as _controlled X_ or _controlled NOT_.  It applies $X$ on $q_0$ only when $q_1 = \ket{1}$. This is equivalent to the classical computation with $\texttt{XOR}$ gate if input qubits are either $\ket{0}$ or $\ket{1}$.   We can see the difference between classical and quantum computation  when a superposition state is used as input. Consider a case where $q_0=\ket{0}$ and $q_1=c_0 \ket{0} + c_1 \ket{1}$.  The state of the two qubits is
# 
# $$
# \ket{\Psi_\text{in}} = \ket{0} \otimes (c_0 \ket{0} + c_1 \ket{1}) = c_0 \ket{0}\otimes \ket{0} + c_1 \ket{0}\otimes \ket{1}.
# $$
# 
# The output is
# 
# $$
# \ket{\Psi_\text{out}} =  c_0 \ket{0}\otimes \ket{0} + c_1 \ket{1}\otimes \ket{1},
# $$
# 
# which is known as  _entangled_ state.   There is no way to express this state in a classical computer.  Quantum computation utilizes entangled states.
# 

# ## Readouts
# 
# When a qubit is in $\ket{0}$ or $\ket{1}$, readout is in principle accurate (not on current NISQ computers due to device errors). However, the outcome is completely uncertain if the qubit is in a superposition state {eq}`eqn:superposition`. We will obtain $\texttt{0}$ or $\texttt{1}$ at random.  If we prepare many qubits in the same superposition state, we obtain $\texttt{0}$ from some and $\texttt{1}$ from others. Hence, the readout of qubits is stochastic, from which we know that the qubits are in a superposition state but which one?  The principle of quantum mechanics tells us that the probability of getting $\texttt{0}$ is given by $|c_0|^2$ and $\texttt{1}$ by $|c_1|^2$.  By measuring many qubits in the same state, we can calculate the probabilities from which $|c_0|^2$ and $|c_1|^2$ can be determined.  The phase of $c_0$ and $c_1$ are still missing.  There is a complicate procedure, known as _quantum tomography_, which can determine the superposition state if and only if sufficiently large number of the same superposition states are measured.  Therefore, it is necessary to repeat the same quantum computation many times if the final result is a superposition state.  Even when the result of the computation is designed to be $\ket{0}$ or $\ket{1}$ by the algorithm, the outcome can be a superposition state due to device errors.  Even worse, the final state can be so-called _mixed state_, which contains a mixture of classical and quantum uncertainties simultaneously.  A good quantum circuit avoids both classical and quantum uncertainties as much as possible.

# In[ ]:




