#!/usr/bin/env python
# coding: utf-8

# # IPython

# *This short tutorial is a very brief exploration of the essential features of IPython and Jupyter Notebooks. It is mainly based on content from [Python for Data Analysis](https://wesmckinney.com/book/) by Wes McKinney.*  

# You can run any file as a Python program inside the environment of your IPython session using the %run command. Suppose you had the following simple script stored in ipython_script_test.py:

# ```Python
# def f(x, y, z):
#     return (x + y) / z
# 
# a = 5
# b = 6
# c = 7.5
# 
# result = f(a, b, c)
# ```

# You can execute this by passing the filename to %run:

# In[1]:


get_ipython().run_line_magic('run', 'ipython_script_test.py')


# In the Jupyter notebook, you may also use the related %load magic function, which imports a script into a code cell:

# ## Magic commands
# 
# - IPython's special commands (which are not built into Python itself) are known as “magic” commands
# 
# - These are designed to facilitate common tasks 
# 
# - A magic command is any command prefixed by the percent symbol `%`. 

# In[2]:


get_ipython().run_line_magic('pwd', '')


# In[3]:


foo = get_ipython().run_line_magic('pwd', '')

foo


# - Type `%quickref` to view all magic commands

# In[4]:


get_ipython().run_line_magic('quickref', '')

