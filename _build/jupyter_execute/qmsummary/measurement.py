#!/usr/bin/env python
# coding: utf-8

# (chap-measurement)=
# # Quantum measurement
# 
# [Wikipedia: Measurement in quantum mechanics](https://en.wikipedia.org/wiki/Measurement_in_quantum_mechanics)

# An important role of theoretical physics is to predict physical quantities such as energy and experimental physics tries to measure them.  Without measurement as accurate as possible.  Without measurement, there is no physics.
# 
# In classical mechanics, we can obtain a precise value from any  physical quantity  upon measurement and we can predict it by solving the Newton equation.  If the same measurement is done on identical copies of the original system, the same value is always obtained. If the outcomes differ, then that must be due to measurement error (e.g., a bad measurement device). 
# 
# In quantum mechanics, as we already discussed in previous chapters, the outcomes of measurement is *stochastic* even when the measurement apparatus is perfect. The principle of quantum mechanics cannot predict the outcome of single measurement. Only we can predict is the probabilities.   In this chapter, we present a formal theory of quantum measurement.

# ## Observables
# 
# [Wikipedia: Observable](https://en.wikipedia.org/wiki/Observable)
# 
# We haven't discussed how to describe physical quantities in quantum mechanics.  They are not number.  They are a special kind of operators in the Hilbert space of a quantum system. The operators corresponding to physical quantities are called *observable*. 
# In order for operator $A$ to be observable, it must be *Hermitian* (self-adjoint).  That is $A^\dagger = A$.  Since it satisfies $[A^\dagger, A]=0$, the observable is also a *normal* operator,  which guarantees that the observable has eigenvalues $a_i$ and eigenvectors $\ket{e_i}$.  Thus we have
# 
# $$
# A \ket{a_i} = a_i \ket{a_i}, \quad i=1,\cdots,d
# $$
# 
# where $d$ is the dimension of Hilbert space.  There are two important properties of the observable:
# 
# > 1. all eigenvalues are real
# > 2. eigenvectors form a complete orthonormal basis  
# 
# which are essential to the quantum measurement.
# 
# In quantum computation,  computational basis vectors $\ket{0}$ and $\ket{1}$ are the eigenvectors of a Pauli operator $Z$.  Hence, we measure $Z$.

# ## Outcomes of measurement
# 
# When we measure a physical quantity, we expect that the outcome is a number, not an operator.  The role of operator (observable) is to determine possible outcome.  The outcome of the measurement must be an eigenvalue of the observable.  We obtain one of $a_i$ when $A$ is measured.  But there are many eigenvalues.  Which one are we going to obtain?   Quantum mechanics can't tell us what precisely we get.  No one can predict it. Only we know the probability to obtain a particular eigenvalue.   If the state of the system is $\rho$, the probability of finding $a_i$ is given by
# 
# $$
# p_i = \bra{a_i} \rho \ket{a_i}.
# $$(born-rule-density)
# 
# which is vaklid for both pure and mixed states.
# 
# For pure state, we already use the probability.  Consider the system on a pure state $\ket{\psi}$, we expand it in basis $\{\ket{a_i}\}$ (We can do so since the eigenvectors form a complete orthonormal basis):
# 
# $$
# \ket{\psi} = c_1 \ket{a_1} + c_2 \ket{a_2} + \cdots + c_d \ket{a_d}
# $$
# 
# The Born rule indicates that we obtain $a_i$  with probability $p_i= |c_i|^2 = |\langle a_i | \psi \rangle |^2$.  Recalling that the density operator of  the pure state is $\rho = \ket{\psi}\bra{\psi}$, Eq. {eq}`born-rule-density` gives the same probability. 
# 

# 
# ___   
# 
# __Exercise__  {numref}`%s<chap-measurement>`.1&nbsp;  Show that $\bra{a_i} \rho \ket{a_i} =  |\langle a_i | \psi \rangle |^2$ for the pure state $\ket{\psi}$.
# 
# ___   
# 

# ## Projective measurement
# 
# In classical mechanics, we can measure a physical quantity without disturbing the system state.  That is not the case of quantum systems.  When  the measurement results in $a_i$, the state also is transformed to $\ket{a_i}$ regardless of the original state before the measurement.  This transformation is known as *wave function collapse*.  The mechanism of the collapse is still not known but we are able to explain experiment results based on this postulate.  No exception has been reported since the inception of quantum mechanics 100 years ago. 
# 
# Recall that the quantum mechanics is is applied to an ensemble and measurement is needed to be repeated.  If we throw away other states and keep only $\ket{a_i}$, then the resulting state is a pure state $\ket{a_i}$.  This kind of measurement is called *selective measurement*.   On the other hand, if we keep all outcomes (*non-selective measurement*), we have a classical mixture of $\ket{a_i}$ with probability {eq}`born-rule-density`:
# 
# $$
# \rho_\text{out} = \sum_i p_i \ket{a_i}\bra{a_i}  = \sum_i \ket{a_i}\bra{a_i} \rho_\text{in} \ket{a_i}\bra{a_i}.
# $$(rho-out)
# 
# where $\rho_\text{in}$ and $\rho_\text{out}$ are the density operators before and after the measurement, respectively.   Noting that $\ket{a_i}\bra{a_i}$ is a projection operator, we can interpret Eq. {eq}`rho-out` as a projection of the state to $\ket{a_i}$ and this type of measurement is called *projective measurement*.

# ## Expectation values

# ## Uncertainty principle

# In classical mechanics, we can obtain a precise value from any  physical quantity  upon measurement and we can predict it by solving the Newton equation.  If the same measurement is done on indentical copies of the original system, the same value is always obtained. If the outcomes differ, then tha must be due to measurement error (e.g., a bad measurement device). 
# 
# In quantum mechanics, as we already discussed in previous chapters, the outcomes of measurement is *stochastic* even when the measurement apparatus is perfect. The principle of quantum mechanics cannot predict the outcome of single measurement. Only we can predict is the probabilities.   In this chapter, we present a formal theory of quantum measurement.
# 
# 
# When we have many copies of the identical quantum states, the outcomes of measurement are usually different.  What quantum mechanics can tell us is a _probability_ of finding a particular value.  That means that the outcome of  measurement is randomly chosen according to the probability.  Only in special cases, we can get the same value from the all copies,  which we can predict from the state vector.  
# 
# When the outcome is stochastic, we need to resort to the methods of statistics. Computing expectation value and standard deviation is essential since we can predict them based on the current theory of quantum mechanics.
# 
# Furthermore, the measurement changes the state and the new state depends on the value of the outcome.  When the measurement picked an eigenvalue of the observable, the state jumps to the corresponding eigenvector. This jump cannot be described by the current theory of quantum mechanics.  _Decoherence_ may explain a part of this process but the detail remains unclear. 
# 
# In addition to the stochastic nature of quantum measurement, there is another notable difference between classical and quantum measurements.  In classical mechanics,  we can determine the precise values of two or more physical quantities simultaneously by measurement. That may not be possible in quantum mechanics depending on what you measures.  For example, the position and momentum of a classical particle can be precisely determined. In quatum mechanics, on the other hand, if both quantities are measured from many identical copies, it is impossible to have the same outcome from the all copies.  If all copies have the same position, then every copy has very different value of momentum.  In typical cases, each copy results in a pair of different values from other copies, hence there are uncertainties in both quantities.
# 
# The interpretation of quantum measurement is very counter intuitive. We still don’t know  how quantum measurement takes place.  Many physicists are not fully convinced by the current theory of quantum mechanics and believe that the theory of quantum mechanics is still incomplete.   There are other interpretation of quantum mechanics such as the pilot wave theory. However, all experimental results agree with the probabilities computed from the state vector.  Therefore, we adopt the standard theory of quantum mechanics in this book.  
# 
# 
# Finding the state of a system is not necessarily the final goal of physics.  We want to know the  values of other quantities such as  energy  In classical mechanics, physical quantities are naturally defined as number and the measurement of a physical quantity produces a unique value.  On contrary to our intuition, physical quantities in quantum mechanics are not number.  They are _self-adjoint operator_ in the Hilbert space.  The outcome of a measurement is one of the _eigenvalues_ of the operator and we don’t know which one will be the result of the measurement.  This strange behaviors are the next topics.

# **Related topics in Wikipedia**
# 
# * <a href="https://en.wikipedia.org/wiki/Measurement_in_quantum_mechanics" target="_blank"> Measurement in quantum mechanics</a>
# * <a href="https://en.wikipedia.org/wiki/Observable"  target="_blank">Observable</a>
# * <a href="https://en.wikipedia.org/wiki/Born_rule"  target="_blank">Born rule</a>
# * <a href="https://en.wikipedia.org/wiki/Wave_function_collapsee"  target="_blank">Wave function collapse</a>

# 
# ___  
# 
# 
# Version 0.1.0: &nbsp; Last modified on May 3, 2022

# In[ ]:




