#!/usr/bin/env python
# coding: utf-8

# # Classical computation 
# 
# Before going to quantum computation, let us briefly look at classical computation.

# ## Clcassical information
# 
# 
# 
# 
# A classical computer consists of many small building blocks, each of them has two possible states.  We assign indexes to these states, $\texttt{0}$ and $\texttt{1}$.  When the device is in one state, we interpret it as `0` and in the other state as `1`.  We call the information stored in this device unit `bit` and use a symbol $b \in \{\texttt{0},\texttt{1}\}$.  The computer consists of many bits, bit 0, bit 1, bit 2, .......  For convenience, we denote the bits as $b_0, b_1, b_2, \cdots $ and altogether the information is stored in a string of n bits, $'\, b_{n-1}\, b_{n-2}\, \cdots\, b_1\, b_0\, '$, for example $\texttt{0010101}$.

# ## Gates
# 
# The computer can change the state of any bit at our command.  A simple operation is to flip a bit, that is $0\rightarrow 1$  and $1 \rightarrow 0$.  We express it using a concept of _gate_.  A bit enters a gate and comes out with a different value.  In the classical computer, there are only two possibility,  no flip or flip.  "No flip" means nothing happens to the bit and thus we are not interesting it.  The gate that flips a bit is called `NOT` gate. (See {numref}`classical-gates`.)  This is the only gate acts on a single bit outputs a single bit.  The relation between the input and the output bit is given in the truth {numref}`table %s <classical-NOT>`.
# 
# 

# ```{list-table} NOT Gate
# :header-rows: 1
# :name: classical-NOT
# :align: center
# 
# * - &nbsp;
#   - $i$
#   - &nbsp;
#   - $o$
#   - &nbsp; 
# * - &nbsp;
#   - 0
#   - &nbsp;
#   - 1
#   - &nbsp;    
# * - &nbsp;
#   - 1
#   - &nbsp;
#   - 0
#   - &nbsp;  
# ```

# Classical computation uses various kind of gates which takes two input bits ($i_0$ and $i_1$) and outputs one bit.  For example, `AND` gate outputs $i_0 \times i_1$.  (See {numref}`classical-gates`.)
# The corresponding truth table is given in {numref}`classical-AND`.  Notice that this process is _irreversible_, meaning that we cannot recover the input information $i_0$ and $i_1$ from the output $o$.  Hence, we says that a bit of information is lost.  Two-bit classical gates  are in general irreversible and 1 bit of information is lost. 

# ```{list-table} AND Gate
# :header-rows: 1
# :name: classical-AND
# :align: center
# 
# * - &nbsp;
#   - $i_0$
#   - &nbsp;
#   - $i_1$
#   - &nbsp;  
#   - $o$
#   - &nbsp; 
# * - &nbsp;
#   - 0
#   - &nbsp;
#   - 0
#   - &nbsp;  
#   - 0
#   - &nbsp;   
# * - &nbsp;
#   - 0
#   - &nbsp;
#   - 1
#   - &nbsp;  
#   - 0
#   - &nbsp;  
# * - &nbsp;
#   - 1
#   - &nbsp;
#   - 0
#   - &nbsp;  
#   - 0
#   - &nbsp;
# * - &nbsp;
#   - 1
#   - &nbsp;
#   - 1
#   - &nbsp;  
#   - 1
#   - &nbsp;  
# ```

# ```{figure} ./classical-gate.png
# :name: classical-gates
# :align: center
# :width: 400px
# 
# An example of classical gates. The $\texttt{NOT}$ gate takes one bit and output one bit.
# ```

# In principle, classical computation needs only $\texttt{NOT}$ and $\texttt{AND}$ gates.  It is using other gates makes classical computing much more efficient.

# **Exercise**  Is $\texttt{NOT}$ gate reversible?

# ## Encoding
# 
# The computer can understand only bit strings and manipulates them by applying gates.  However, problems we want to solve are usually not expressed in bit strings.  Somehow, we need to map the problems to bit strings the computer can understand. In other words, we need to _encode_ the information in our expression to the bit strings. As a simple example, we consider a boolean operation between two logical variables $x$ and $y$.  Their value is either $\texttt{True}$ or $\texttt{False}$.   Since the valiables takes only one of two possibilities, the mapping between the boolean variables and bits are naturally
# 
# $$
# \texttt{False} \Rightarrow \texttt{0}, \quad \texttt{True} \Rightarrow \texttt{1}
# $$
# 
# Now, variable $x$ is expressed by a bit $b_0$ and $y$  by $b_1$.  
# 
# In many problems, encoding is not obvious at all.  Integer numbers can be mapped to bit strings using their binary expressions.  For example, $5 \Rightarrow \texttt{101}$, which requires three bits.  Exact encoding of continuous numbers is not possible  since bits are digital.  Approximated representation such as _floating point_ numbers are used.
# , quantum or classical

# ## Instructions
# 
# Computation means that by manipu, quantum or classicallating the state of bits toward the solution.  The device can flip the specified bits .  It can be thought of bits entering a _gate_ and coming out with different values.  We need to instruct the device how to change the state of the bits.  In other words we to find find what gates should be applied to the bits. Let us consider a simple operation $x+y \mod 2$ where $x, y \in \{0, 1\}$.  WE shall write this operation simply as $x \oplus y$ . We map $x$ and $y$ to bits $b_0$ and $b_1$. Applying an `XOR` gate on $q_0$ and $b_1$ produces desired outputs.   The following diagram classically computes $x \oplus y$ and the output is stored in $x$. The value of $y$ remains the same.

# ```{figure} ./classical-half-adder.png
# :name: classical-half-adder
# :align: center
# :width: 400px
# 
# An example of classical circuit.  This circuit computer $x \oplus y$ using $\texttt{XOR}$ and $\texttt{AND}$.  In addition to the answer, carry over bit 
# ```

# In real world applications, we don’t apply the gates by ourselves.  Instead, we use a programming language such as `python`. The language translates the mathematical  expression such as $x + y$ into gate instructions. So, we really don't need to know about the classical gate.  Quantum computation has not reached that level yet. Users must picks appropriate gates by themselves.

# ## Readout and decoding
# 
# Once the computation is completed at the device level, we need to read out the values of the bits and decode the outcome to an integer.  The readout of the classical bits can be done without damaging their state.  The value of the classical bits remains the same before and after the readout.  (That is not the case in quantum computers.)

# In[ ]:




