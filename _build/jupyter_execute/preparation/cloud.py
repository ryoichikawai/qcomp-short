#!/usr/bin/env python
# coding: utf-8

# (sec-cloud)=
# # Cloud IDE

# If your computer does not have enough storage or power to run python and jupyter, you can develop python codes and run them on cloud-based online IDEs.  You can also upload the jupyter notebook files used in this book and run them.  The most popular one is *Google Colab*.  However, it is a general purpose IDE and some packages we use are not available.  You must install them manually each time you use their service.[^cloud]  *IBM Quantum Lab* is another cloud-based online IDE and it is designed to work with IBM Quantum Computing service via Qiskit and thus all packages we need are preloaded.  For our purpose, IBM Quantum Lab works better than Google Colab.

# (sec-IBMQLab)=
# ## IBM Quantum Lab
# 
# IBM Quantum Lab allows to run JupyterLab on their server.  It is designed for quantum computing and thus it is ready to run the codes in this book.  Then, upload it to IBM Quantum Lab.  You can run it on their server for free.    
# 
# If you created your IBM Quantum Experience account as instructed in {numref}`sec-qiskit`, you are ready to use IBM Quantum Lab.
# Login to [IBM Quantum Dashboard](https://quantum-computing.ibm.com/).  Click "Launch Lab".  Then you enter IBM Quantum Lab, which is JupyterLab running on their computer.  On the left panel, you can create new folders, new files, or upload existing jupyter notebook files.
# 

# (sec-Colab)=
# ## Google Colab
# 
# Google Colab also gives you a similar free development environment. It is not identical but compatible to JupyterLab.  However, it is for general purpose and you must install necessary python packages such as qiskit each time.  Nevertheless, it is convenient if you do not have access to a local jupyter environment.
# 
# You need to have a google account to use this free service. If you don't have one yet, you can open an account at [accounts.google.com](https://accounts.google.com/signup).  Once you obtained your account, sign in at [golan.research.google.com](https://colab.research.google.com/).  You can start writing codes or upload jupyter notebook files.  
# 
# Unfortunately, Colab does not have qiskit.  However, you can install it.  Add the following code block at the beginning.
# ```
# !pip install qiskit ipywidgets pylatexenc
# ```
# Now, your qiskit codes run in Colab.  The installation is only temporary.  When you close the session, qiskit is removed.  You must install it each time you start new Colab session.

# ```{admonition} Running Qiskit on Google Colab
# :class: tip
# :name: download-page
# 
# If you want to run qiskit codes on Google Colab, you need to add the following command in a code block.
# 
# `!pip install qiskit ipywidgets pylatexenc`
# 
# ```

# [^cloud]: There are methods to store packages permanently but the procedure is rather complicated.  Therefore, we do not discuss it here.
