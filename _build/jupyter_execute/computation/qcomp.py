#!/usr/bin/env python
# coding: utf-8

# (sec-qcomp)=
# # Quantum computation
# 
# Here is a brief description of quantum computer and the details will be discussed in this book.  It is necessary for you to understand the following at this stage.  Just read them and move on.

# ## Qubits
# 
# Quantum computers are also made of many small building blocks but unlike classical computers we need to use quantum mechanics to describe their state. Current quantum computers use the smallest quantum system, that is a two-dimensional Hilbert space $\mathbb{C}_2$ spanned by complex vectors $\lvert 0 \rangle$ and $\lvert 1 \rangle$, known as _qubit_. These two basis states looks similar to `0` and `1` for a classical bit . However, unlike the classical bit,  the state of a qubit  can be in a superposition state
# 
# $$
# \ket{\psi} = c_{0} \lvert 0 \rangle + c_{1} \lvert 1 \rangle
# $$ (eqn:superposition)
# 
# where $c_0$ and $c_1$ are complex number satisfying $|c_0|^2+|c_1|^2=1$ (normalization). Similarly to the classical bit, we obtain either $\ket{0}$ or $\lvert 1 \rangle$  when the superposition state is measured.   We shall call them _computational basis_. However,  the state of the qubit is neither $\lvert 0 \rangle$ nor $\lvert 1 \rangle$  but  $\lvert 0 \rangle$ AND $\lvert 1 \rangle$ simultaneously. Hence, a qubit can compute two different cases at once (if a programmer is smart enough). Quantum computers exploit this superposition state.  Unlike the classical bit which has only two possible states, a qubit can take infinitely many different states since $c_0$ and $c_1$ can be any complex numbers satisfying the normalization condition. 
# 
# Obviously, quantum computers are made of many qubits as a composite system. Let us consider two qubits, $q_0$ and $q_1$.  A composite system of two classical bits can have four different states, '00', '01', 10', and '11'.  Similarly  the pair of qubits are spanned by four basis vectors $\lvert 00 \rangle$, $\lvert 01 \rangle$, $\lvert 10 \rangle$, and $\lvert 11 \rangle$.  Unlike the classical bits, the qubits can be in a superposition state
#  
# $$
# \lvert \psi \rangle = c_{00} \lvert 00 \rangle + c_{01} \lvert 01 \rangle + c_{10} \lvert 10 \rangle + c_{00} \lvert 11 \rangle
# $$
# 
# The four different possibilities are simultaneously considered in the superposition state. The complexity of the superposition state grows very rapidly as the number of qubits increases.  If there are $n$ qubits, the number of terms in the superposition state can be as many as $2^n$.   Then, $2^n$ different cases are simultaneously computed. We will take the advantage in various applications.
# 
# In classical computers,  a bit string $b_{n-1}\, b_{n-2}\,\cdots\, b_1\, b_0$ expresses the state of the system.  In quantum computer, a tensor product $\lvert q_{n-1} \rangle \otimes \lvert q_{n-2}\rangle \otimes \cdots \otimes \lvert q_1 \rangle \otimes \lvert q_0 \rangle$ represents the state of $n$ qubits.  For two qubits, $\lvert 01 \rangle = \lvert 0 \rangle \otimes \lvert 1 \rangle$.

# ## Restriction on quantum information processes
# 
# Qubits have many advantages over classical bits, which is the main topics of this book.  However, they have also many disadvantages.  Here are some restrictions imposed on the quantum information.
# 
# 1. [**No-cloning theorem**](https://en.wikipedia.org/wiki/No-cloning_theorem)  
# The theorem states that it is not possible to duplicate an arbitrary qubit.   During quantum computation we cannot make a copy of a qubit in an unknown state.  Recall that classical bit can be cloned.
# 
# 2. [**No-teleportation theorem**](https://en.wikipedia.org/wiki/No-teleportation_theorem)  
# If the information stored in a qubit can be converted to a classical bit string and vice versa, we can *teleport* the quantum information to a distant place via a classical bit string. Such teleportation is not possible.  This theorem imposes more important restriction.  We cannot read out the full information in an arbitrary qubit since the outcome of the measurement is classical.
# 
# 3. [**No-deleting theorem**](https://en.wikipedia.org/wiki/No-deleting_theorem)  
# If two qubits happened to be in the same but arbitrary state, it is not possible to delete the information in one of the qubits.  This is a no-go theorem and time-reversal of no cloning theorem.
# 
# 4. [**No-broadcasting theorem**](https://en.wikipedia.org/wiki/No-broadcasting_theorem)  
# It is possible to transfer the full information in an arbitrary qubit to another qubit but the information in the original qubit must be destroyed.  This is known as *quantum teleportation*.  However, broadcasting the full information in an arbitrary qubit to multiple qubits is not possible. This is a corollary of no cloning theorem.
# 
# 5. [**No-hiding theorem**](https://en.wikipedia.org/wiki/No-hiding_theorem)  
# Briefly stating, the information stored in quantum system must be conserved. It is not possible to create or destroy quantum information.  In contrast, classical information can be created or destroyed.
# 
# 

# ## Quantum Information
# 
# Recall that information is about uncertainty or probability.  a classical bit is dichotomous and there is only one uncertainty, 0 or 1.  In contrast, the state of a qubit is continuous and there are infinitely many different states.  The no-teleportation theorem tells us that even infinitely many classical bits cannot describe the state of a qubit.  Does this mean a qubit contains infinite amount of information? It turns out that we can ask only a dichotomous question.  
# 
# Consider a qubit in a superposition state
# 
# $$
# \lvert \psi \rangle = \frac{1}{\sqrt{2}} \lvert 0 \rangle +  \frac{1}{\sqrt{2}} \lvert 1 \rangle
# $$
# 
# If we ask if the qubit is in $\lvert 0 \rangle$, the answer is either "yes" or "no" but there is no definite answer.  There is 50% chance to get "yes" and 50% chance to get "no".  The situation is quite similar to the coin tossing. 
# However, there are differences. Even when we know precisely that the qubit is in the state $\lvert \psi \rangle$, there is still the uncertainty, hence it is no due to our ignorance.  The uncertainty is not due to future event since $\lvert \psi \rangle$ already exists.  Nevertheless, the amount of information seems $\log 2$.
# 
# You can ask a different question.  Is the state $\lvert + \rangle =  \frac{1}{\sqrt{2}} \lvert 0 \rangle +  \frac{1}{\sqrt{2}} \lvert 1 \rangle$ or $\lvert - \rangle =  \frac{1}{\sqrt{2}} \lvert 0 \rangle -  \frac{1}{\sqrt{2}} \lvert 1 \rangle$?  $\lvert \pm \rangle$ forms an orthonormal basis, this question makes a sense.  Now, the answer is "yes" without ambiguity.  For this question,  $\lvert \psi \rangle$ contains no information!   Although the question we can ask is always dichotomous, we can ask infinitely many different questions.  This is the main difference between qubit and classical bit.
# 
# We define quantum information entropy using density operator $\rho = \lvert \psi \rangle \langle \psi \rvert$ as
# 
# $$
# S = - \text{Tr} \left(\rho \log \rho\right)
# $$
# 
# which is known as von-Neumann entropy. Plugin $\rho = \lvert \psi \rangle \langle \psi \rvert$ , we find $S=0$.  Hence, the state has no information (uncertainty).  When quantum measurement is done, the state collapses to a different state, which can have a non-vanishing information entropy.  In this sense, information is created, when measurement is done.  For the current example, the state after measurement of $\lvert 0 \rangle$ and $\lvert 1 \rangle$, the state after the measurement is
# 
# $$
# \rho = \frac{1}{2}  \lvert 0 \rangle \langle 0 \rvert + \frac{1}{2}  \lvert 1 \rangle \langle 1 \rvert
# $$
# 
# and its von Neumann entropy is $S = \log 2$ as expected. 
# 

# ## Gates
# 
# As a general purpose computer, a quantum computer must be able to change the state of qubits based on given instructions. Recall that a classical bit can only be flipped.  In contrast, quantum computers can change the state of a qubit in infinitely many different ways.  Here we use also the concept of gates.  A qubit enters a gate and comes out in a different state.  In other words, a state vector of the qubit is transformed to another state vector by the gate.  In quantum mechanics, that is achieved by a unitary transformation $U$.   The transformation $\ket{\psi'}=U \ket{\psi}$ in quantum mechanics is equivalent to applying a 1-qubit gate $U$ to a qubit and expressed as
# 
# ```{figure} u1-gate.png
# ---
# name: u1-gate
# ---
# Action of one-qubit gate.
# ```
# 
# As an example, consider a Pauli operator $X \equiv \sigma_x$.  When it acts on the computational basis, $X \lvert 0 \rangle = \lvert 1 \rangle$ and $X \lvert 1 \rangle=\lvert 0 \rangle$.  Hence, it acts like $\texttt{NOT}$ in the classical computation. See the {numref}`quantum-gate-X`. The qubit can be in a superposition state.  The  classical truth table is not enough. When it acts on a general state, we get
# 
# $$
# X \lvert \psi \rangle = c_0 X \lvert 0 \rangle + c_1 X \lvert 1 \rangle = c_0 \lvert 1 \rangle + c_1 \lvert 0 \rangle = c_1 \lvert 0 \rangle + c_0 \lvert 1 \rangle
# $$ (Xgate)
# which actually swaps the coefficients.  The first two rows in  {numref}`quantum-gate-X` is much like the classical truth {numref}`table %s <classical-NOT>`.  The third row makes quantum computers more powerful than the classical computers.
# 
# 

# ```{table} X Gate
# :name: quantum-gate-X
# | &nbsp;| $i$ | $o$ |
# | :---:| :---: | :---: |
# | &nbsp;| $\lvert 0 \rangle$ | $\lvert 1 \rangle$  |
# | &nbsp;| $\lvert 1 \rangle$ | $\lvert 0 \rangle$  |
# | &nbsp;| $c_0 \lvert 0 \rangle + c_1 \lvert 1 \rangle$ | $c_1 \lvert 0 \rangle + c_0 \lvert 1 \rangle$ |
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
# \texttt{False} \Rightarrow \lvert 0 \rangle, \quad \texttt{True} \Rightarrow \lvert 1 \rangle
# $$
# 
# This works fine.  However, there are many other encoding schemes since a qubit can take a superposition state.  For example,
# 
# $$
# \texttt{False} \Rightarrow \lvert + \rangle \equiv \frac{1}{\sqrt{2}}\left(\lvert 0 \rangle+\lvert 1 \rangle\right), \quad
# \texttt{True}  \Rightarrow \lvert - \rangle \equiv \frac{1}{\sqrt{2}}\left(\lvert 0 \rangle-\lvert 1 \rangle\right)
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
# The gate in the circuit is known as _controlled X_ or _controlled NOT_.  It applies $X$ on $q_0$ only when $q_1 = \lvert 1 \rangle$. This is equivalent to the classical computation with $\texttt{XOR}$ gate if input qubits are either $\lvert 0 \rangle$ or $\lvert 1 \rangle$.   We can see the difference between classical and quantum computation  when a superposition state is used as input. Consider a case where $q_0=\lvert 0 \rangle$ and $q_1=c_0 \ket{0} + c_1 \lvert 1 \rangle$.  The state of the two qubits is
# 
# $$
# \lvert \Psi_\text{in} \rangle = \lvert 0 \rangle \otimes (c_0 \lvert 0 \rangle + c_1 \lvert 1 \rangle) = c_0 \lvert 0 \rangle\otimes \lvert 0 \rangle + c_1 \lvert 0 \rangle \otimes \lvert 1 \rangle.
# $$
# 
# The output is
# 
# $$
# \lvert \Psi_\text{out} \rangle =  c_0 \lvert 0 \rangle \otimes \lvert 0 \rangle + c_1 \lvert 1 \rangle \otimes \lvert 1 \rangle,
# $$
# 
# which is known as  _entangled_ state.   There is no way to express this state in a classical computer.  Quantum computation utilizes entangled states.
# 

# ## Readouts
# 
# When a qubit is in $\lvert 0 \rangle$ or $\lvert 1 \rangle$, readout is in principle accurate (not on current NISQ computers due to device errors). However, the outcome is completely uncertain if the qubit is in a superposition state {eq}`eqn:superposition`. We will obtain $\texttt{0}$ or $\texttt{1}$ at random.  If we prepare many qubits in the same superposition state, we obtain $\texttt{0}$ from some and $\texttt{1}$ from others. Hence, the readout of qubits is stochastic, from which we know that the qubits are in a superposition state but which one?  The principle of quantum mechanics tells us that the probability of getting $\texttt{0}$ is given by $|c_0|^2$ and $\texttt{1}$ by $|c_1|^2$.  By measuring many qubits in the same state, we can calculate the probabilities from which $|c_0|^2$ and $|c_1|^2$ can be determined.  The phase of $c_0$ and $c_1$ are still missing.  There is a complicate procedure, known as _quantum tomography_, which can determine the superposition state if and only if sufficiently large number of the same superposition states are measured.  Therefore, it is necessary to repeat the same quantum computation many times if the final result is a superposition state.  Even when the result of the computation is designed to be $\lvert 0 \rangle$ or $\lvert 1 \rangle$ by the algorithm, the outcome can be a superposition state due to device errors.  Even worse, the final state can be so-called _mixed state_, which contains a mixture of classical and quantum uncertainties simultaneously.  A good quantum circuit avoids both classical and quantum uncertainties as much as possible.

# In[ ]:




