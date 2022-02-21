#!/usr/bin/env python
# coding: utf-8

# # Syntax
# 
# *This short tutorial is a very brief exploration of the essential features of Python syntax. It is mainly based on content from the excellent app Tinkerstellar.*

# 
# - Syntax refers to the structure of the language (i.e., what constitutes a correctly-formed program). 
# - Here, we'll not focus on the semantics – the meaning of the words and symbols within the syntax.

# In[1]:


# set the midpoint
midpoint = 5

# make two empty lists
lower = []
upper = []

# split the numbers into lower and upper
for i in range(10):
    if (i < midpoint):
        lower.append(i)
    else:
        upper.append(i)
        
print("lower:", lower)
print("upper:", upper)


# ## Comments
# 
# - Comments in Python are marked by #
# - Anything on the line following the # sign is ignored by the interpreter

# In[2]:


# set the midpoint


# In[3]:


# below are examples of inline comments
x = 1 # create a variable x and assign value 1
x += 2  # shorthand for x = x + 2
print(x) # print x


# ## Statements
# 
# - End-of-line terminates a statement in Python

# In[4]:


midpoint = 5


# - This is an assignment operation, where we've created a variable named midpoint and assigned it the value 5. 
# - Notice that the end of this statement is simply marked by the end of the line. 
# - If you'd like a statement to continue to the next line, it is possible to use the "\\" marker to indicate this:

# In[5]:


x = 1 + 2 + 3 + 4 +    5 + 6 + 7 + 8
print(x)


# - It is also possible to continue expressions on the next line within parentheses:

# In[6]:


x = (1 + 2 + 3 + 4 +
     5 + 6 + 7 + 8)
print(x)


# - Most Python style guides recommend the second version of line continuation (within parentheses) 

# ## Indentation

# - A block of code is a set of statements that should be treated as a unit
# - Code blocks are denoted by indentation (white space)
# - The amount of whitespace used for indenting code blocks is up to the user, as long as it is consistent throughout the script
# - By convention, most style guides recommend to indent code blocks by four spaces 
# - Indented code blocks are always preceded by a colon (:) on the previous line

# In[7]:


midpoint = 5
for i in range(10):
    if i < midpoint:
        lower.append(i)
    else:
        upper.append(i)


# - In the snippet below, print(x) is in the indented block, and will be executed only if x is less than 4

# In[8]:


x=5
if x < 4:
    y = x * 2
    print(x)      


# - In the snippet below, print(x) is outside the block, and will be executed regardless of the value of x

# In[9]:


x=5
if x < 4:
    y = x * 2
print(x)      


# ## Whitespace wihin lines

# - White space within lines of Python code does not matter
# - For example, all three of these expressions are equivalent

# In[10]:


a=1+2
a = 1 + 2
a   =   1   +   2

print(a)


# - Using whitespace effectively can lead to much more readable code

# In[11]:


b=10**-2

b = 10 ** -2


# ## Parentheses
# 
# - Parentheses are used for grouping or calling
# - They can be used in the typical way to group statements or mathematical operations:

# In[12]:


2 * (3 + 4)


# - They can also be used to indicate that a function is being called. 
# - In the next snippet, the `print()` function is used to display the contents of a variable. 
# - The function call is indicated by a pair of opening and closing parentheses, with the arguments to the function contained within:

# In[13]:


print('Value:', 1)


# - Some functions can be called with no arguments at all, in which case the opening and closing parentheses still must be used to indicate a function evaluation. 
# - An example of this is the sort method of lists:

# In[14]:


L = [4,2,3,1]
L.sort()

print(L)


# - The "()" after sort indicates that the function should be executed, and is required even if no arguments are necessary.

# ## Style guides
# 
# - The most widely used style guide in Python is known as PEP8, and can be found at https://www.python.org/dev/peps/pep-0008/
