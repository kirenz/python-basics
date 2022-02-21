#!/usr/bin/env python
# coding: utf-8

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

