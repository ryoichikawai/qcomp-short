#!/usr/bin/env python
# coding: utf-8

# # CZ

# | input |  |output |
# | :----: |:---: |:----: |
# | $\lvert 00\rangle$ | $\Rightarrow$ | $\lvert 00\rangle$ |
# | $\lvert 01\rangle$ | $\Rightarrow$ | $\lvert 01\rangle$ |
# | $\lvert 10\rangle$ | $\Rightarrow$ | $\lvert 10\rangle$ |
# | $\lvert 11\rangle$ | $\Rightarrow$ | $-\lvert 11\rangle$ |

# In[1]:


import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, Aer
from qiskit.quantum_info import Statevector
backend = Aer.get_backend('statevector_simulator')


# * We check only $|11\rangle \Rightarrow -|11\rangle$.

# In[2]:


qr  = QuantumRegister(2)
qc = QuantumCircuit(qr)
qc.x([0,1])
qc.barrier()
qc.cz(0,1)
qc.draw()


# In[3]:


result=backend.run(qc).result()
(result.get_statevector()).draw('latex')


# * Relation with `CX`

# `CX` can be expressed with `H` and `CZ`.  Here we just check $|11\rangle \Rightarrow |10\rangle$.

# In[4]:


qr  = QuantumRegister(2)
qc = QuantumCircuit(qr)
qc.x([0,1])
qc.barrier()
qc.h(0)
qc.cz(0,1)
qc.h(0)
qc.draw()


# In[5]:


result=backend.run(qc).result()
(result.get_statevector(decimals=3)).draw('latex')

