#!/usr/bin/env python
# coding: utf-8

# (chap-time-evolution)=
# # Time-evolution

# The state of the classical particles change according to the Newton equation, which is a set of ordinary differential equations. Equivalently,  the trajectory can be computed from the Hamilton equations of motion, by measurement
# 
# $$
# \dot{q} = \frac{\partial H}{\partial p}, \qquad \dot{p} = -\frac{\partial H}{\partial q}
# $$
# 
# where $H$ is a Hamiltonian.
# 
# The state vector of a quantum system evolves in time according to the Schr&ouml;dinger equation
# 
# $$
# i \frac{\partial}{\partial t} |\psi\rangle = H |\psi\rangle
# $$
# 
# where $H$ is Hamiltonian operator.  Equivalently,  the solution can be written as
# 
# $$
# |\psi(t)\rangle = U(t) |\psi(0)\rangle
# $$
# 
# where $U(t)$ is a unitary operator and $|\psi(0)\rangle$ an initial state.  We call this type of evolution _unitary_ evolution. Quantum computation solves this equation.  We will solve it using `Qiskis`.

# 
# ___  
# 
# (version 0.0.1: &nbsp;   Lat modified on April 7, 2022)
# 

# In[ ]:




