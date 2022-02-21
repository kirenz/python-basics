#!/usr/bin/env python
# coding: utf-8

# # Regular expressions
# 
# *This short tutorial is a very brief exploration of the essential features of IPython and Jupyter Notebooks. It is mainly based on content from [Python for Data Analysis](https://wesmckinney.com/book/) by Wes McKinney.*  

# In[1]:


states = ['   Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda',
           'south   carolina##', 'West virginia?']


# - We mant to make this list of strings uniform and ready for analysis: 
#     - stripping whitespace, 
#     - removing punctuation symbols, 
#     - standardizing on proper capitalization. 
#     
# - We use the built-in string methods along with the re standard library module for regular expressions:

# In[2]:


import re

def clean_strings(strings):
    result = []
    for value in strings:
        value = value.strip()
        value = re.sub('[!#?]', '', value)
        value = value.title()
        result.append(value)
    return result


# In[3]:


clean_strings(states)


# - An alternative approach that you may find useful is to make a list of the operations you want to apply to a particular set of strings:

# In[4]:


def remove_punctuation(value):
    return re.sub('[!#?]', '', value)

clean_ops = [str.strip, remove_punctuation, str.title]

def clean_strings(strings, ops):
    result = []
    for value in strings:
        for func in ops:
            value = func(value)
        result.append(value)
    return result


# In[5]:


clean_strings(states, clean_ops)


# - A more functional pattern like this enables you to easily modify how the strings are transformed at a very high level. 
# 
# - The clean_strings function is also now more reusable and generic.
# 
# - You can use functions as arguments to other functions like the built-in map function, which applies a function to a sequence of some kind:

# In[6]:


for x in map(remove_punctuation, states):
    print(x)

