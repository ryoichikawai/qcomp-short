#!/usr/bin/env python
# coding: utf-8

# (ch-composites)=
# # Composite Systems

# A single qubit is a smallest information carrying unit similar to classical bit.  Despite that a qubit can take infinitely many different states on the surface of a Bloch sphere, it carries the same amount of information as a classical bit since measurement of a qubit produces only two different values like a classical bit.  A practically useful quantum computer needs many qubits. Desktop computers process 64 bits of information inside a CPU and store information in giga bits of memory. At least similar number of qubits are needed for practical quantum computation.  However, the states of multiple qubits are much more complicated that the same number of classical bits. There are a special kind of superposition states known as *quantum entanglement*, which cannot realized in classical bits.  It turns out the entanglement is the most powerful resource for quantum computation.
# 
# In this chapter, we study mathematical properties of a composite system consisting of multiple qubits and two-qubit gates which act on two qubits in such a way that the transformation of one qubit  depends on the other qubit and vice versa. 

# In[ ]:




