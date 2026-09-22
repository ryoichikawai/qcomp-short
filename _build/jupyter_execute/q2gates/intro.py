#!/usr/bin/env python
# coding: utf-8

# # Two-qubits Gates

# When two gates $A$ and $B$ are applied to qubits $q_0$ and $q_1$, respectively, we can write the combined gates as $C = A \otimes B$. We do not call it 2-qubit gate. In fact, $A$ and $B$ are not necessarily applied to the qubits at the same time.   A 2-quibit gate  cannot be expressed as a tensor product of two 1-qubit gates and it must act simultaneously on two qubits.
# 
# Commonly used 2-qubit gates are _controoled_ gates, which are actually conditional 1-qubit gates. A 1-qubit gate such as `X` is applied to $q_1$ only when $q_0$ is in $|1\rangle$.  Otherwise, no action is taken.  
# There are other kind of 2-qubit gates such as `Swap` gate.
# 
# Most of common 2-qubit gates are spectial cases of more general canonical gates.  Many  models used in condensed matter physics are directly expressed by canonical gates, understandin the relation between canonical gates and common 2-qubit gates are particluarly important.

# | Generaic Name | Qiskit Class Name |  Qiskit Ciruit Name  | Symbols |
# | :-----------: | :---------------: | :------------------: | :-----: |
# | Controlled X     | CXGate            |  cx  or cnot         | `CX` or `CNOT` |
# | Controlled Y     | CYGate            |  cy                  | `CY`    |
# | Controlled Z     | CZGate            |  cz                  | `CZ`    |
# | Controlled Hadamard | CHGate         |  ch                  | `CH`    |
# | Controlled SX    | CSXGate           |  csx                 | `CSX`   |
# | Controlled Phase | CPhaseGate        |  cp                  | `CP`    |
# | Controlled Rotaion X  | CRXGate      |  crx                 |`CR`$_x$ |
# | Controlled Rotaion Y  | CRYGate      |  cry                 |`CR`$_y$ |
# | Controlled Rotaion Z  | CRZGate      |  crz                 |`CR`$_z$ |
# | Controlled Unitary 1  | CU1Gate      |  cu1                 |`CU`$_1$ |
# | Controlled Unitary 3  | CU3Gate      |  cu3                 |`CU`$_3$ |
# | Controlled Unitary    | CUGate       |  cu                  |`CU`     |

# __Others__  
# 
# * `Swap`
# * `H`$_2$

# __Canonical Gates__  
# 
# `Can`$(t_x,t_y,t_z)=\exp\left[-i\frac{\pi}{2}\left( t_x X\otimes X + t_y Y\otimes Y + t_z \otimes ZZ\right) \right]$

# In[ ]:




