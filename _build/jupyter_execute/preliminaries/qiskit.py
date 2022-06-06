#!/usr/bin/env python
# coding: utf-8

# (sec-jupyter)=
# # Qiskit
# 

# Qiskit is an open-source software development kit (SDK) for quantum computation. It provides a large set of tools for creating and manipulating quantum programs, running them on simulators on a local computer, or running them on real quantum devices on IBM Quantum Experience.  You can find useful information about Qiskit including tutorials and API documentation at [qiskit.org](https://qiskit.org).

# ## Installation
# 
# It is a set of python modules but not included in Anaconda.  We need to install them manually.
# 
# ```
# pip install qiskit
# pip install qiskit[visualization]
# ```
# 
# Since conda does not manage these packages, you must update the package when a new version becomes available.  To check the current version, run the following command in the anaconda terminal window.
# 
# On MS Windows, use Anaconda Powershell Prompt.
# ```
# pip list | select-string "qiskit"
# 
# qiskit                            0.36.2
# qiskit-aer                        0.10.4
# qiskit-ibmq-provider              0.19.1
# qiskit-ignis                      0.7.1
# qiskit-terra                      0.20.2
# ```
# 
# On Linux
# ```
# pip list | grep qiskit
# 
# qiskit                            0.36.2
# qiskit-aer                        0.10.4
# qiskit-ibmq-provider              0.19.1
# qiskit-ignis                      0.7.1
# qiskit-terra                      0.20.2
# ```
# 
# To check updates, the following command shows available new versions.
# 
# ```
# # On MS Windows
# pip list --outdated | select-string "qiskit"
# 
# #
# pip list --outdated | grep qiskit
# ```
# 
# 

# ## IBM Quantum Experience
# 
# In order to take the full advantage of qiskit, you must first create your IBM Quantum Experience account.  With IBMid, you can run qiskit codes on real IBM quantum computers as well as on realistic simulations on your computer.  Go to 
# [quantum-computing.ibm.com](https://quantum-computing.ibm.com/) and set up an account.
# Log in to your account.  You are in IBM Quantum Dashboard where you find many useful stuffs which we discuss in later chapters. 
# 

# ## API key
# 
# Next, you need to obtain an API key and save it in a local computer.
# 
# 1. Log in to IBM Quantum Experience at [quantum-computing.ibm.com](https://quantum-computing.ibm.com/)
# 2. Click the user icon at the upper-right corner.
# 3. Click "Account setting".
# 4. Click "Generate new token"
# 5. Click copy icon at the right end of the token box.  Your token is copied to the clipboard.
# 6. Open a text editor and paste the token.  Save it it to a temporary file so that you can copy the token at a later time if needed. Delete the file after the key is properly installed.
# 7. Open an Anaconda terminal window.
# 8. Start python and execute the following command at the python prompt:
# 
# ```
# >>> from qiskit import IBMQ
# >>> IBMQ.save_account('past your token here')
# ```
# The token must be inside the single quotes.  Now, we verify if the token works.
# 
# ```
# >>> IBMQ.load_account()
# ```
# You should get the following response:
# ```
# <AccountProvider for IBMQ(hub='ibm-q', group='open', project='main')>
# ```
# If it worked, delete the temporary file created at step 6.  Otherwise, something went wrong. Try step 8 again.  Make it sure that the whole key is pasted.
# 
# If you work on multiple computers, you have to install the same API on each machine.

# ## Using Qiskit
# 
# Since Qiskit is a collection of python modules, we must import it to your code before using it.  The package is so large that importing the entire package is not a good idea. In this book, we use only a small portion of it.  As you move on, this book introduces some basic modules absolutely necessary for quantum computing and explains how to use them step by step.

# In[ ]:




