#!/usr/bin/env python
# coding: utf-8

# (sec-jupyter)=
# # JupyterLab
# 

# Jupyter is a project to develop an interactive environment for data science and scientific computing. (See [jupyter.org](https://jupyter.org/).)  It provides a popular web-based interactive development environment (IDE), *Jupyter Notebook*.  We use a next-generation of notebook called *JupyterLab* in this book.  With JupyterLab, you can create an interactive document consisting of texts written in *Markdown* and Python codes.  In fact, this book is entirely written in JupyterLab. Since it runs in a web browser, you can use JupyterLab running on remote computers.  There are free online services that allow anyone to use their JupyterLab.  However, it is convenient to have it on your own computer since we use some extensions which may not be available at the free services.  

# ## Installation  [^skip-jupyter-installation]
# 
# Anaconda install JupyterLab by default.  However, certain extensions used in this book are not automatically installed.  To install them, open an Anaconda terminal window and install them as shown below.
# 
# * nbextensions
# 
# ```
# pip install jupyter-contrib-nbextensions
# jupyter contrib nbextension install --user
# ```
# 
# * spellchecker
# ```
# pip install jupyterlab-spellchecker
# ```
# 
# * mathjax
# ```
# pip install jupyter-serever-mathjax
# pip install jupyterlab-mathjax3
# ```

# ## Launching 
# 
# There are several different ways to launch JupyterLab depending on the OS.  On any OS, you can launch it from the Anaconda terminal:
# ```
# jupyter-lab
# ```
# This opens an default web browser and JupyterLab appears in it.  If the web browser is already opened, it appears in a new tab.
# 
# On MS Windows, you can start Anaconda Navigator from Start Menu.  It takes a minute to launch the navigator.  Just click JupyterLab shown inside the navigator.  Anaconda does not provide an icon to launch JupyterLab but you find one for Jupyter Notebook in Start Menu.  You can copy it to desktop and modify it.  Simply replace notebook with lab in the target.
# 
# On Linux, you can create a desktop application file easily.  The actual name of executable is jupyter-lab and it is located in ~/anaconda3/bin.  Depending on the Linux distribution, notebook files with ".ipynb" extension is associated with jupyter-lab.  If you click a notebook file in a file manager,  jupyter-lab is automatically launched. (It seems difficult to do it on MS Windows.)
# 

# ## Usage
# 
# JupyterLab create a notebook consisting of three types of blocks, Markdown block, input code block, and output code block.  In a Markdown block, you write texts, tables, images, and equations using Markdown. Markdown is used in many other applications such as wikipedia and github. Most of formatting methods used in github also work in JupyterLab.  See [writing-on-github](https://docs.github.com/en/get-started/writing-on-github) for the formatting syntax. 
# 
# In a code block, you write python codes. They are computed right a way. Right now, I am in Markdown block.  The next block is an input code block.  You see a python code in it and its output appears in output block right below the input code block.

# In[1]:


x=2
y=3
print("x^2+y^2=",x**2+y**2)


# ## Mathematical expression
# 
# For us, ability to write mathematical expression is important.  Here are examples.  You can write mathematical equation using LaTeX.  An in-line equation start with `$` and another `$` after the equation. For example,
# 
# ```
# $ \int \cos x dx = \sin x$
# ```
# is rendered as $ \int \cos x dx = \sin x$.
# 
# A display equation begins with `$$` which start a equation environment.  In a new line, you write an equation.  Then, another `$$` closes the environment.  For example,
# ```
# $$
# \int_0^\infty e^{-x} dx = 1
# $$
# ```
# becomes
# 
# $$
# \int_0^\infty e^{-x} dx = 1
# $$
# 

# ## Closing JupyterLab  
# 
# Just closing web browser does not stop JupyterLab.  It is still running in the background.  To close JupyterLab, use "shutdown" in "File".

# [^skip-jupyter-installation]: If your computer does not have enough storage or power to run Python and JupyterLab, skip Installation.  Use an online IDE introduced in {numref}`sec-cloud`.
