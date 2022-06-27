#!/usr/bin/env python
# coding: utf-8

# (chap-qubit1)=
# # A Qubit
# 

# In quantum computer, information is encoded in a set of qubits.  Hence, understanding the properties of a single qubit is the first step to quantum computation. Mathematically, a qubit is the smallest meaningful Hilbert space, i.e., a two-dimensional Hilbert space. Physically, a qubit is realized in many different form.  A quantum system that has only two states is a good candidate of a qubit.  For example, the spin of an electron has two states, spin-up state $|\uparrow\rangle$  and spin-down state $|\downarrow\rangle$.  A photon has two directions of linear polarization.  The horizontal and vertical polarization are expressed as $|H\rangle$ and $|V\rangle$, respectively.  Atoms have many energy levels and thus not exactly a qubit.  However, if two adjacent energy levels are far from other levels, they can be considered as a qubit.  Regardless its physical implementation, the same mathematical theory can be used for any form of a qubit.
# 
# In this chapter, first mathematical expressions and properties of a single qubit are explained. It is very important for you to familiarize yourself with the notations and the rules of calculation since they are used through the book.  Secondly, the concept of quantum measurement is introduced.  As we discussed in the previous chapter, the quantum measurement is quite different from the classical measurement.  You must get rid of the classical intuition and believe in the principles of quantum mechanics. 
# 
# After the theory of a qubit, I explain how to create a qubit in Qiskit and how to visualize the state of the qubit.  At the end, you simulate quantum coin tossing using a quantum computer. 

# In[ ]:




