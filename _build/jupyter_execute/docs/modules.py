#!/usr/bin/env python
# coding: utf-8

# # Modules
# 
# *This notebook contains content from the Whirlwind Tour of Python by Jake VanderPlas*
# 
# One feature of Python that makes it so useful is the fact that it contains tools for a wide range of tasks. On top of this, there is a broad ecosystem of third-party modules that offer more specialized functionality. 
# 
# :::{note}
# Python modules are a set of useful functions that eliminate the need for writing codes from scratch.
# :::
# 
# A Python module is a reusable chunk of code that you can import in your own projects so you don't have to write all the code by yourself. There are around 140000 available Python projects and one way to discover and install them is to use the [Python Package Index (PyPI)](https://pypi.org/). Note that we will use another way to install Python modules since we work with the open source data science platform Anaconda (as a general rule, you shouldn't use PyPI in Anaconda).

# ## Import modules
# 
# For loading built-in and third-party modules, Python provides the import statement. There are a few ways to use the statement, which we will briefly mention in this chapter, from most recommended to least recommended.
# 
# 
# ### Explicit module import
# 
# Explicit import of a module preserves the module's content in a namespace. The namespace is then used to refer to its contents with a "." between them. For example, here we'll import the built-in math module and compute the cosine of pi:
# 
# ```python
# import math
# math.cos(math.pi)
# ```
# 
# ### Explicit module import by alias
# 
# For longer module names, it's not convenient to use the full module name each time you access some element. For this reason, we'll commonly use the `"import ... as ..."` pattern to create a shorter alias for the namespace. 
# 
# For example, the NumPy (Numerical Python) package, a popular third-party package useful for data science, is by convention imported under the alias np:
# 
# ```python
# import numpy as np
# np.cos(np.pi)
# ```
# 
# ### Explicit import of module contents
# 
# Sometimes rather than importing the module namespace, you would just like to import a few particular items from the module. This can be done with the `"from ... import ..."` pattern. 
# 
# For example, we can import just the cos function and the pi constant from the math module:
# 
# ```python
# from math import cos, pi
# cos(pi)
# ```
# 
# ### Implicit import
# 
# Finally, it is sometimes useful to import the entirety of the module contents into the local namespace. This can be done with the `"from ... import *"` pattern:
# 
# ```Python
# from math import *
# sin(pi) ** 2 + cos(pi) ** 2
# ```
# 
# This pattern should be used sparingly, if at all. The problem is that such imports can sometimes overwrite function names that you do not intend to overwrite, and the implicitness of the statement makes it difficult to determine what has changed.
# 

# ## Built-in modules
# 
# Python's standard library contains many useful built-in modules, which you can read about fully in Python's documentation. Any of these can be imported with the import statement. Here is a short list of some of the modules you might wish to explore and learn about:
# 
# - os and sys: Tools for interfacing with the operating system, including navigating file directory structures and executing shell commands
# - math and cmath: Mathematical functions and operations on real and complex numbers
# - itertools: Tools for constructing and interacting with iterators and generators
# - functools: Tools that assist with functional programming
# - random: Tools for generating pseudorandom numbers
# - pickle: Tools for object persistence: saving objects to and loading objects from disk
# - json and csv: Tools for reading JSON-formatted and CSV-formatted files.
# - urllib: Tools for doing HTTP and other web requests.
# 
# You can find information on these, and many more, in the Python standard library documentation: https://docs.python.org/3/library/.
# 
# ## Important modules
# 
# Here a list of some of the modules we will use frequently:
# 
# - [pandas](https://pandas.pydata.org/) is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool. We will use pandas regularly in our course and you will find all relevant content in this [introduction to pandas]()
# 
# - [NumPy](https://numpy.org/) offers tools for scientific computing like mathematical functions and random number generators.
# 
# - [SciPy](https://scipy.org/) contains algorithms for scientific computing.
# 
# - [matplotlib](https://matplotlib.org/) is a library for creating data visualizations.
# 
# - [Seaborn](https://seaborn.pydata.org/) provides a high-level interface for drawing attractive and informative statistical graphics.
# 
# - [plotly](https://plotly.com/python/) is a graphing library to make interactive, publication-quality graphs.
# 
# - [statsmodels](https://www.statsmodels.org/stable/index.html) includes statistical models, hypothesis tests, and data exploration.
# 
# - [scikit-learn](https://scikit-learn.org/stable/) provides a toolkit for applying common machine learning algorithms to data.
# 
# - [TensorFlow](https://www.tensorflow.org/) is an end-to-end open source platform for machine learning.

# ### NumPy
# 
# As an example, we take a closer look at NumPy (numerical Python), which provides an efficient way to store and manipulate multi-dimensional dense arrays in Python. 
# 
# The important features of NumPy are:
# 
# - It allows efficient storage and manipulation of vectors, matrices, and higher-dimensional datasets.
# 
# - It provides a readable and efficient syntax for operating on this data, from simple element-wise arithmetic to more complicated linear algebraic operations.
# 
# In the simplest case, NumPy arrays look a lot like Python lists. For example, here is an array containing the range of numbers 1 to 9 (compare this with Python's built-in range()):
# 

# In[1]:


import numpy as np
x = np.arange(1, 10)
x


# NumPy's arrays offer both efficient storage of data, as well as efficient element-wise operations on the data. For example, to square each element of the array, we can apply the "**" operator to the array directly:

# In[2]:


x = np.arange(1, 10)
x ** 2


# Compare this with the much more verbose Python-style list comprehension for the same result:

# In[3]:


x = range(1, 10)
[val ** 2 for val in x]


# Unlike Python lists (which are limited to one dimension), NumPy arrays can be multi-dimensional. A 2-dimensional array of size 2 x 3, composed of 4-byte integer elements:

# In[4]:


x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)

print("Type:", type(x), "\n" "Shape:", x.shape, "\n" "Data Type:", x.dtype)

#x.shape

#x.dtype

