#!/usr/bin/env python
# coding: utf-8

# (sec-teleportation)=
# # Quantum Teleportation

# Suppose that Alice has a qubit in an arbitrary state $|\psi\rangle$ carrying some information.  She wants to send the information to Bob. In other words, Bob needs to obtain a qubit in the same state $|\psi\rangle$.  The simple solution is to deliver the Alice's qubit to Bob.  Let us assume that the Alice's qubit is not mobile and must stay with her.  What can they do?  First of all, Bob needs a qubit.  It can be any state but let us assume it us in a "reset state" $|0\rangle$.  Further, we assume that the two qubits are initially not entangled. This assumption allows Bob to bring a qubit from anywhere he likes.  We apply some unitary operation (gates) to the both qubits so that the state of Bob's qubit  is transformed to $|\psi\rangle$.  Copying the state from Alice to Bob is not possible due to the no-cloning theorem.  Applying local unitary operation (one-qubit gates) to each qubit does not transmit any information and thus the Bob's qubit is independent of the Alice's. We need non-local operation (two-qubit gates).   We know such a non-local operation.  The SWAP operation makes the Bob's qubit $|\psi\rangle$ and Alice loses the information entirely.  Unfortunately, the SWAP operation works only when the two qubits are close to each other, hence one of them must travel to the other.
# 
# Is there a way to create a desired state over a distance by communication?  Classical communication such as telephone call won't help due to the no-teleportation theorem. We must use a quantum communication.  That means we need a messenger qubit that can be sent from one cite to another, such as a photon. It turns out that quantum communication along with classical communication *teleport* the state $|\psi\rangle$ from Alice to Bob over a large distance.  We use three qubits, $q_A$ for Alice, $q_B$ for Bob, and $q_M$ messenger (often called *ancila* qubit).  The protocol is called [*quantum teleportation*](https://en.wikipedia.org/wiki/Quantum_teleportation).

# ## The protocol
# 
# Consider a Hilbert space of three qubits $\mathcal{H}_A \otimes \mathcal{H}_M \otimes \mathcal{H}_B$.  $q_A$ is in a arbitrary state
# $\alpha |0\rangle + \beta |1\rangle$, and  $q_B$ and $q_M$ are both in $|0\rangle$.  Thus the initial state is
# 
# $$
# |\psi_0\rangle = \left( \alpha |0\rangle + \beta |1\rangle\right) \otimes |00\rangle
# $$
# 
# We want find a protocol that makes $q_B$ becomes $\left( \alpha |0\rangle + \beta |1\rangle\right)$ at the end.  We don't care the final state of $q_A$ and $q_M$.
# 
# **Step 1**  
# 
# Assume that $q_M$ is near by $q_B$.  Bob applies H and CX on $q_M$ and $q_B$ so that they becomes Bell state $|\Phi^{+}$.(See {eq}`cbase-Bell`.)
# 
# $$
# |\psi_0\rangle = \left( \alpha |0\rangle + \beta |1\rangle\right) \otimes |00\rangle \quad \Rightarrow \quad  |\psi_1\rangle =\left( \alpha |0\rangle + \beta |1\rangle\right) \otimes |\Phi^{+}\rangle
# $$
# 
# 
# **Step 2**
# 
# Now the messenger qubit travels to Alice. In order to distinguish $\alpha$ and $\beta$, Alice applies CX$_{q_A}^{q_M}$.
# $$
# |\psi_1\rangle =\left( \alpha |0\rangle + \beta |1\rangle\right) \otimes |\Phi^{+}\rangle \quad \Rightarrow \quad  |\psi_2\rangle = \alpha |0\rangle \otimes |\Phi^{+}\rangle + \beta |1\rangle \otimes |\Psi^{+}\rangle
# $$
# 
# Note that $q_M$ and $q_B$ are separated by a distance, entanglement in the Bell states survives.
# 
# **Step 3**
# 
# Alice applies H on $q_A$ to change the basis of $q_A$ from the $z$-basis to $x$-basis.
# 
# $$
# |\psi_2\rangle = \alpha |0\rangle \otimes |\Phi^{+}\rangle + \beta |1\rangle \otimes |\Psi^{+}\rangle  \quad \Rightarrow \quad |\psi_3\rangle = \alpha |+\rangle \otimes |\Phi^{+}\rangle + \beta |-\rangle \otimes |\Psi^{+}\rangle
# $$
# 
# Now, we rewrite $|\psi_3\rangle$ from the Alice's view
# 
# $$
# |\psi_3\rangle = \frac{1}{2}\left[|00\rangle\otimes \left(\alpha|0\rangle + \beta |1\rangle\right) + |01\rangle\otimes \left(\alpha|1\rangle + \beta |0\rangle\right) + |10\rangle\otimes \left(\alpha|0\rangle - \beta |1\rangle\right) + |11\rangle\otimes \left(\alpha|1\rangle + \beta |0\rangle\right) \right]
# $$
# 
# **Step 4**
# 
# Alice measures $q_A$ and $q_M$ in the computational basis.  There are four possible outcomes, $|00\rangle$, $|01\rangle$, $|10\rangle$, and $|11\rangle$ with the equal probability $\frac{1}{4}$.  The state vector collapses accordingly.   The outcomes of the measurement are listed in {numref}`table-teleport`. 
# 
# ```{table} The outcome of measurement
# :name: table-teleport
# 
# | Alice's outcome | Bob's state |  Classical message  | 
# | :-----------: | :---------------: | :------------------: |
# | $\lvert 00\rangle$ | $\alpha \lvert 0\rangle + \beta \lvert 1\rangle$ |  Do nothing. |
# | $\lvert 01\rangle$ | $\alpha \lvert 1\rangle + \beta \lvert 0\rangle$ |  Apply X. |
# | $\lvert 10\rangle$ | $\alpha \lvert 0\rangle - \beta \lvert 1\rangle$ |  Apply Z. |
# | $\lvert 11\rangle$ | $\alpha \lvert 1\rangle - \beta \lvert 0\rangle$ |  Apply Z$\cdot$X |
# 
# ```
# 
# 
# **Step 5**
# 
# If Alice obtain $00\rangle$, then Bob's qubit is in the desired state.  Otherwise, Bob needs to transform his qubit but he does not know what to do.  Alice sends a message given in {numref}`table-teleport` to Bob through classical channel (such as telephone). In quantum circuit, this final adjustment can be done by applying CX$_{q_M}^{q_B}$ and CZ$_{q_A}^{q_B}$ after the measurement.  Note this CX and CZ are just mimicking the classical communication.
# 
# Bob follows the message.  Now, Bob has the desired state in all cases.

# In[1]:


import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, Aer
from qiskit.quantum_info import Statevector, partial_trace, purity
backend = Aer.get_backend('statevector_simulator')

cr=ClassicalRegister(2,'c')
qr=QuantumRegister(3,'q')
qc=QuantumCircuit(qr,cr)

# Generate a state Alice has
# set parameters
theta=np.pi/3
phi=0.0
qc.u(theta,phi,0,0)

psi0=Statevector(qc)

qc.barrier()

# Step 1
qc.h(1)
qc.cx(1,2)

# Step 2
qc.cx(0,1)

# Step 3
qc.h(0)
qc.barrier()

# Step 4
qc.measure([0,1],[0,1])

# Step 5
qc.cx(1,2)
qc.cz(0,2)

qc.draw()


# In[2]:


result=backend.run(qc).result()
full_statevector = result.get_statevector()


# In[3]:


# get the density matrix for the first qubit by taking the partial trace
print("Alice's initial state")
rhoA = partial_trace(psi0, [1,2])
print("purity=",purity(rhoA))
psiA = Statevector(np.sqrt(np.diagonal(rhoA)))
psiA.draw('latex')


# In[4]:


# get the density matrix for the first qubit by taking the partial trace
print("Bob's initial state")
rhoB = partial_trace(full_statevector, [0,1])
print("purity=",purity(rhoB))
psiB = Statevector(np.sqrt(np.diagonal(rhoB)))
psiB.draw('latex')


# The result shows that the state of Bob's qubit is pure and identical to the original state of Alice's qubit.

# In[ ]:




