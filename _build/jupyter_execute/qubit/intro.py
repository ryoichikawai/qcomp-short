#!/usr/bin/env python
# coding: utf-8

# (chap-qubit1)=
# # Single qubit
# 

# In quantum computer, information is processed in a set of qubits.  Correlation among the qubits distinguishes the quantum computation from the classical computation.  However, understanding the properties of a single qubit is the first step toward the quantum computation. 
# 
# Mathematically, a qubit lives in the smallest Hilbert space, that is a two-dimensional Hilbert space. Physically, a qubit is realized in many different form.  Any quantum system that has only two states or two states well separated from other states is a good candidate of a qubit.    For example, a photon  has two directions of linear polarization,  the horizontal and vertical polarization.  Hence, a single photon can be used as a qubit.  Various different types of qubits are developed, including [Superconducting quantum computing](https://en.wikipedia.org/wiki/Superconducting_quantum_computing) and [Trapped ion quantum computer](https://en.wikipedia.org/wiki/Trapped_ion_quantum_computer).  Regardless its physical implementation, the same mathematical theory can be used for any type of a qubit.
# 
# In this chapter, first mathematical expressions and properties of a single qubit are explained. It is very important for you to familiarize yourself with the notations and the rules of calculation since they are used through the book.  Secondly, the concept of quantum measurement is introduced.  As we discussed in the previous chapter, the quantum measurement is quite different from the classical measurement.  You must get rid of the classical intuition and believe in the principles of quantum mechanics. 
# 
# After the theory of a qubit, I explain how to create a qubit in Qiskit and how to visualize the state of the qubit.  At the end, we simulate quantum coin tossing and quantum state tomography using a quantum computer. 

# In[ ]:




