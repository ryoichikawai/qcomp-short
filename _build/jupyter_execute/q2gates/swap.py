#!/usr/bin/env python
# coding: utf-8

# #  SWAP

# | input |  |output |
# | :----: |:---: |:----: |
# | $\lvert 00\rangle$ | $\Rightarrow$ | $\lvert 00\rangle$ |
# | $\lvert 01\rangle$ | $\Rightarrow$ | $\lvert 10\rangle$ |
# | $\lvert 10\rangle$ | $\Rightarrow$ | $\lvert 01\rangle$ |
# | $\lvert 11\rangle$ | $\Rightarrow$ | $\lvert 11\rangle$ |

# SWAP gate can be a native gate for certain types of quantum computer through exchange interaction.  Here we show a circuit equivalent to `SWAP`.

# In[1]:


import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, Aer
from qiskit.quantum_info import Statevector
backend = Aer.get_backend('statevector_simulator')


# Using the built-in SWAP gate:  |01⟩⇒|10⟩

# In[2]:


cr=ClassicalRegister(2)
qr  = QuantumRegister(2)
qc = QuantumCircuit(qr,cr)
qc.x(0)
qc.barrier()
qc.swap(0,1)
qc.measure([0,1],[0,1])
qc.draw()


# In[3]:


result=backend.run(qc).result()
(result.get_statevector()).draw('latex')


# * Equivalent circuit to `SWAP` using `CX`

# In[4]:


qr = QuantumRegister(2)
qc = QuantumCircuit(qr)
qc.x(1)
qc.cnot(0,1)
qc.cnot(1,0)
qc.cnot(0,1)
qc.draw()


# In[5]:


result=backend.run(qc).result()
(result.get_statevector()).draw('latex')


# Symmetric property: Swapping qubits themselves (not their states) should give the same results.

# In[6]:


qr = QuantumRegister(2)
qc = QuantumCircuit(qr)
qc.x([0,1])
qc.barrier()
qc.cnot(1,0)
qc.cnot(0,1)
qc.cnot(1,0)
qc.draw()


# In[7]:


result=backend.run(qc).result()
(result.get_statevector()).draw('latex')


# There is no particular reason to use X direction.  `CY` should be able to realize `SWAP` as well.

# In[8]:


qr = QuantumRegister(2)
qc = QuantumCircuit(qr)
qc.x(0)
qc.barrier()
qc.cy(1,0)
qc.cy(0,1)
qc.cy(1,0)
qc.draw()


# In[9]:


result=backend.run(qc).result()
(result.get_statevector()).draw('latex')


# In[ ]:




