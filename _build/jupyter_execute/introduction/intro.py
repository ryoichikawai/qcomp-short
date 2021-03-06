#!/usr/bin/env python
# coding: utf-8

# (chap-whatisqcomp)=
# # What is a Quantum Computer?

# In modern life style, computers are used everywhere, inside cars, TV sets, kitchen appliances and cell phones, to name a few.  They are all operated in the same way with classical *bits*.  The principles of computation are developed by major mathematicians such as Alan Turing ([universal Turing machine](https://en.wikipedia.org/wiki/Turing_machine)) and von Neumann ([von Neumann architecture](https://en.wikipedia.org/wiki/Von_Neumann_architecture)).  Furthermore, classical [information theory](https://en.wikipedia.org/wiki/Information_theory) developed by another genius mathematician, Claude Shannon advanced the classical computation to a much higher level.
# 
# While the classical computation technology is matured, the [computability theory](https://en.wikipedia.org/wiki/Computability_theory) shows that there are many hard problems that cannot be solved by the classical computer. See for example [travelling salesman problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem).  The demands of new computers that can solve such hard problems keep rising.  On the other hand, the current encryption based on [RSA keys](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) works precisely because classical computers have the limitation.  However, in 1994 Peter Shore found a *quantum algorithm* to breaking the RSA encryption.  If quantum computers should become available, data security based on the RSA keys would be obsolete. This is a national security problem ([See this national security memorandom on May 4, 2022](https://www.whitehouse.gov/briefing-room/statements-releases/2022/05/04/national-security-memorandum-on-promoting-united-states-leadership-in-quantum-computing-while-mitigating-risks-to-vulnerable-cryptographic-systems/))  and it is quickly becoming a real issue.  [See "The race to save the Internet from quantum hackers"](https://www.nature.com/articles/d41586-022-00339-5#:~:text=The%20quantum%20computer%20revolution%20could,secure%20algorithms%20can%20safeguard%20privacy.&text=In%20cybersecurity%20circles%2C%20they%20call,relentless%20hum%20of%20cryptographic%20algorithms.).
# 
# So, what is a quantum computer?  It is our current understanding that all physical phenomena are governed by quantum mechanics. The computer you are using is indeed built upon the laws of quantum mechanics. Electrons in the semiconductor chips must be treated as quantum particles.  Nevertheless, it is called classical computer.  The difference between classical and quantum computing is how *information* is stored and processed.  Information must be stored in certain *stable* physical states.  If they are unstable, information is lost quickly.  Information in classical devices is safely stored in  macroscopic states against disturbances from the environment but an important signature of quantum mechanical behavior, *coherence*, is completely abandoned.  On the other hand, quantum computers store in information in a microscopic state which is fragile and easily disturbed by the environmental noises but quantum mechanical coherence is used as computational resources.  The recent advances in quantum technology have made it possible to keep quantum information alive long enough to carry out computation. 
# 
# In this chapter, I  briefly introduce basic idea of classical and quantum computers and discuss what can be advantage of quantum computers over classical ones.

# In[ ]:




