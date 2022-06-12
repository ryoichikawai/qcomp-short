#!/usr/bin/env python
# coding: utf-8

# (sec-bloch-sphere)=
# # Bloch sphere

# In[1]:


get_ipython().run_cell_magic('capture', '', '# The output block is disabled.\n\nimport numpy as np\nfrom qiskit import *\n\nqr = QuantumRegister(1)\nqc = QuantumCircuit(qr)\n\nqc.ry(np.pi/2,0)\nqc.rz(np.pi/2,0)\nqc.rx(np.pi/2,0)\n\nfrom qiskit.visualization import visualize_transition\nmovie=visualize_transition(qc,fpg=50, spg=1)')


# In[2]:


movie


# In[ ]:




