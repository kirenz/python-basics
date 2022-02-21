#!/usr/bin/env python
# coding: utf-8

# # Semantics
# 
# *This short tutorial is a very brief exploration of the essential features of Python semantics. It is mainly based on content from the App [Tinkerstellar](https://tinkerstellar.com) by Alex Staravoitau, Jack VanderPlas's [Whirlwind Tour of Python](https://jakevdp.github.io/WhirlwindTourOfPython/) and [Python for Data Analysis](https://wesmckinney.com/book/) by Wes McKinney.*  
# 
# 
# - Semantics of a language involve the meaning of the statements
# - This section will cover the semantics of variables and objects, which are the main ways you store, reference, and operate on data within a Python script

# ## Variables as pointers
# 
# - Assigning variables: putting a variable name to the left of the equals (=) sign
# - Variables are best thought of not as containers but as pointers. 
# - For example, you can define a pointer named `x` that points to some other bucket containing the value `4`: 

# In[1]:


# assign 4 to the variable x
x = 4


# - Variables just point to various objects, there is no need to "declare" the variable
# - "Dynamically-typed": variable names can point to objects of any type:

# In[2]:


# x is an integer
x = 1 
print('x as an integer: ', x)

# now x is a string
x = 'hello'  
print('x as a string: ', x)

# now x is a list
x = [1, 2, 3] 
print('x as a list: ', x)


# - If we have two variable names pointing to the same mutable object, then changing one will change the other as well: 

# In[3]:


x = [1, 2, 3]
y = x


# - We've created two variables x and y which both point to the same object. 
# - Because of this, if we modify the list via one of its names, we'll see that the "other" list will be modified as well:

# In[4]:


print('y = ', y)
# append 4 to the list pointed to by x
x.append(4)
# y's list is modified as well!
print('y = ', y)


# - Note also that if we use "=" to assign another value to x, this will not affect the value of y 
# – Assignment is simply a change of what object the variable points to:

# In[5]:


x = 'something else'
# y is unchanged
print(y)


# - This makes perfect sense if you think of x and y as pointers, and the "=" operator as an operation that changes what the name points to.
# - Using a question mark (?) before or after a variable will display some general information about the object.
# This is referred to as object introspection. 

# In[6]:


get_ipython().run_line_magic('pinfo', 'x')


# - If the object is a function or instance method, the docstring, if defined, will also be shown:

# In[7]:


get_ipython().run_line_magic('pinfo', 'print')


# ## Variables of simple types
# 
# - Numbers, strings, and other simple types are immutable: you can't change their value – you can only change what values the variables point to. 
# - So, for example, it's perfectly safe to do operations like the following:

# In[8]:


x = 10
y = x
x += 5  # add 5 to x's value, and assign it to x
print("x =", x)
print("y =", y)


# - When we call `x += 5`, we are not modifying the value of the 10 object pointed to by x
# - We are rather changing the variable `x` so that it points to a new integer object with value 15. 
# - For this reason, the value of y is not affected by the operation.

# ## Python types
# 
# - Python is an object-oriented programming language, and in Python everything is an object
# - An object is an entity that contains data along with associated metadata and/or functionality.

# In[9]:


x = 4
print(f'x = {x}, type is {type(x).__name__}')

x = 'hello'
print(f'x = {x}, type is {type(x).__name__}')

x = 3.14159
print(f'x = {x}, type is {type(x).__name__}')


# - Python has types and the types are linked not to the variable names but to the objects themselves.

# ## Attributes and methods
# 
# - In Python everything is an object: every entity has some metadata (called attributes) and associated functionality (called methods). 
# - Methods are like attributes, except they are functions that you can call using opening and closing parentheses.
# - These attributes and methods are accessed via the dot syntax. 
# - For example, before we saw that lists have an `append` method, which adds an item to the list, and is accessed via the dot (".") syntax:
# 

# In[10]:


L = [1, 2, 3]
L.append(100)
print(L)


# ## Artihmetic operations
# 
# - Semantics of some arithmetic operators:

# Operator | Name | Description
# ---|---|---
# a + b |	Addition |	Sum of a and b
# a - b |	Subtraction |	Difference of a and b
# a * b |	Multiplication |	Product of a and b
# a / b |	True division |	Quotient of a and b
# a // b |	Floor division |	Quotient of a and b, removing fractional parts 
# a % b |	Modulus |	Integer remainder after division of a by b
# a ** b |	Exponentiation |	a raised to the power of b
# -a |	Negation |	The negative of a
# +a |	Unary plus |	a unchanged (rarely used)

# - These operators can be used and combined in intuitive ways, using standard parentheses to group operations:

# In[11]:


# addition, subtraction, multiplication
(4 + 8) * (6.5 - 3)


# - Floor division is true division with fractional parts truncated:

# In[12]:


print('True division: ', 11 / 2)
print('Floor division: ', 11 // 2)


# ## Comparison operations
# 
# Standard comparison operators return Boolean values True and False:
# 
# Operation |	Description |		Operation |	Description
# ---|---|---|---
# a == b |	a equal to b |		a != b	| a not equal to b
# a < b |	a less than b	|	a > b |	a greater than b
# a <= b |	a less than or equal to b	|	a >= b	 |a greater than or equal to b
# 
# - Comparison operators can be combined with arithmetic operators 
# - For example, we can check if a number is odd by checking that the modulus with 2 returns 1:

# In[13]:


print('Is 25 odd? ', 25 % 2 == 1)
print('Is 66 odd? ', 66 % 2 == 1)


# - We can string-together multiple comparisons to check relationships:

# In[14]:


# check if a is between 15 and 30
a = 25
15 < a < 30


# ## Simple value types
# 
# - All Python objects have type information attached.
# - Here are the built-in simple types offered by Python:
# 
# Type |	Example |	Description
# --- | --- | ---
# int |	x = 1 |	integers (i.e., whole numbers)
# float |	x = 1.0 |	floating-point numbers (i.e., real numbers)
# bool |	x = True |	Boolean: True/False values
# str |	x = 'abc' |	String: characters or text
# NoneType |	x = None |	Special object indicating nulls
# 

# ## Dates and time
# 
# - The built-in Python datetime module provides datetime, date, and time types. 
# 
# - The datetime type combines the information stored in date and time and is the most commonly used:

# In[15]:


from datetime import datetime, date, time

dt = datetime(2011, 10, 29, 20, 30, 21)

print('Day:', dt.day)

print('Minute:', dt.minute)


# - Extract the date and time objects:

# In[16]:


dt.date()


# In[17]:


dt.time()


# - `strftime` formats a datetime as a string:

# In[18]:


dt.strftime('%m/%d/%Y %H:%M')


# Type, Description
# - %Y:  Four-digit year
# - %y:  Two-digit year
# - %m:  Two-digit month [01, 12]
# - %d:  Two-digit day [01, 31]
# - %H:  Hour (24-hour clock) [00, 23]
# - %I:  Hour (12-hour clock) [01, 12]
# - %M:  Two-digit minute [00, 59]
# - %S:  Second [00, 61] (seconds 60, 61 account for leap seconds)
# - %w:  Weekday as integer [0 (Sunday), 6]
# - %U:  Week number of the year [00, 53]; Sunday is considered the first day of the week, and days before the first Sunday of the year are “week 0”
# - %W:  Week number of the year [00, 53]; Monday is considered the first day of the week, and days before the first Monday of the year are “week 0”
# - %z:  UTC time zone offset as +HHMM or -HHMM; empty if time zone naive
# - %F:  Shortcut for %Y-%m-%d (e.g., 2012-4-18)
# - %D:  Shortcut for %m/%d/%y (e.g., 04/18/12)

# ## Compound types
# 
# - Python has several built-in compound types, which act as containers for other types. 
# - Round, square, and curly brackets have distinct meanings when it comes to the type of collection produced:
# 
# Type |	Example |	Description
# --- | --- | --- 
# list |	[1, 2, 3] |	Ordered collection
# tuple |	(1, 2, 3) |	Immutable ordered collection
# dict |	{'a':1, 'b':2, 'c':3} |	Unordered (key,value) mapping
# set |	{1, 2, 3} |	Unordered collection of unique values
# 

# ## Control flow
# 
# - With control flow, you can execute certain code blocks conditionally and/or repeatedly.

# ### Conditional statements: if-elif-else
# 
# - Conditional if-elif-else statements, often referred to as if-then statements, allow the programmer to execute certain pieces of code depending on some Boolean condition. 
# - A basic example of a Python conditional statement is this:

# In[19]:


x = -15

if x == 0:
    print(x, "is zero")
elif x > 0:
    print(x, "is positive")
elif x < 0:
    print(x, "is negative")
else:
    print(x, "is unlike anything I've ever seen...")


# - Note especially the use of colons (:) and whitespace to denote separate blocks of code.

# ### Loops
# 
# - Loops are a way to repeatedly execute some code statement. 
# - So, for example, if we'd like to print each of the items in a list, we can use a for loop:

# In[20]:


for N in [2, 3, 5, 7]:
    print(N, end=' ') # print all on same line


# - We specify the variable we want to use, the sequence we want to loop ("iterate") over, and use the "in" operator to link them together in an intuitive and readable way. 
# - One of the most commonly-used iterators is the range object, which generates a sequence of numbers:

# In[21]:


for i in range(10):
    print(i, end=' ')


# - Note that the range starts at zero by default, and that by convention the top of the range is not included in the output. 
# - Range objects can also have more complicated values:

# In[22]:


print('Range from 5 to 10: ', list(range(5, 10)))

print('Range from 0 to 10 by 2: ', list(range(0, 10, 2)))


# - The other type of loop in Python is a **while loop**, which iterates until some condition is met:  

# In[23]:


i = 0
while i < 10:
    print(i, end=' ')
    i += 1


# - The argument of the while loop is evaluated as a boolean statement, and the loop is executed until the statement evaluates to False.

# ### Continue
# 
# - There are two useful statements that can be used within loops to fine-tune how they are executed:
#     - The break statement breaks-out of the loop entirely
#     - The continue statement skips the remainder of the current loop, and goes to the next iteration
# 
# - These can be used in both for and while loops.
# - Here is an example of using continue to print a string of odd numbers:

# In[24]:


for n in range(20):
    # if the remainder of n / 2 is 0, skip the rest of the loop
    if n % 2 == 0:
        continue
    print(n, end=' ')


# ### Break
# 
# - The break statement breaks-out of the loop entirely. 
# - Here is an example of a break statement used for a less trivial task:
#     - This loop will fill a list with all Fibonacci numbers up to a certain value:

# In[25]:


a, b = 0, 1
amax = 100
L = []

while True:
    (a, b) = (b, a + b)
    if a > amax:
        break
    L.append(a)

print(L)


# - Notice that we use a while True loop, which will loop forever unless we have a break statement!

# ## Functions
# 
# - One way to organize our Python code and to make it more readable and reusable is to factor-out useful pieces into reusable functions. 
# - In this section we will cover two ways of creating functions: 
#     - the `def` statement, useful for any type of function, and the 
#     - `lambda` statement, useful for creating short anonymous functions.
# 
# - Functions are groups of code that have a name, and can be called using parentheses.

# In[26]:


print('abc')


# - Here print is the function name, and 'abc' is the function's argument.
# - In addition to arguments, there are keyword arguments that are specified by name. 
# - One available keyword argument for the `print()` function is `sep`, which tells what character or characters should be used to separate multiple items:

# In[27]:


print(1, 2, 3, sep='--')


# - When non-keyword arguments are used together with keyword arguments, the keyword arguments must come at the end.

# ### Defining functions
# 
# - Functions are defined with the def statement
# - It is good practice to include a description of your function ([docstring](https://www.python.org/dev/peps/pep-0257/#what-is-a-docstring)) at the top oy your function's body:
# 

# In[28]:


def add_numbers(a, b):
    """
    Add two numbers together

    Returns
    -------
    the_sum : type of arguments
    """
    return a + b


# - Then using `?` shows us the docstring:

# In[29]:


get_ipython().run_line_magic('pinfo', 'add_numbers')


# - Using `??` will also show the function’s source code if possible:

# In[30]:


get_ipython().run_line_magic('pinfo2', 'add_numbers')


# - Example of a function

# In[31]:


a = []
def func():
    for i in range(5):
        a.append(i)


# In[32]:


func()

a


# - Return multiple values

# In[33]:


def f():
    a = 5
    b = 6
    c = 7
    return a, b, c

a, b, c = f()


# In[34]:


b


# - As another example, we can create a function to get a Fibonacci sequence (in which each number is the sum of the two preceding ones):

# In[35]:


def fibonacci(N):
    L = []
    a, b = 0, 1
    while len(L) < N:
        a, b = b, a + b
        L.append(a)
    return L


# - Now we have a function named fibonacci which takes a single argument N, does something with this argument, and returns a value; in this case, a list of the first N Fibonacci numbers:

# In[36]:


fibonacci(10)


# ### Default argument values
# 
# - Often when defining a function, there are certain values that we want the function to use most of the time, but we'd also like to give the user some flexibility. 
# - In this case, we can use default values for arguments. 
# - Consider the fibonacci function from before. What if we would like the user to be able to play with the starting values? We could do that as follows:

# In[37]:


def fibonacci(N, a=0, b=1):
    L = []
    while len(L) < N:
        a, b = b, a + b
        L.append(a)
    return L


# - With a single argument, the result of the function call is identical to before:

# In[38]:


fibonacci(10)


# - But now we can use the function to explore new things, such as the effect of new starting values

# In[39]:


fibonacci(10, 0, 2)


# - The values can also be specified by name if desired, in which case the order of the named values does not matter:

# In[40]:


fibonacci(10, b=3, a=1)


# ### Flexible arguments
# 
# - Sometimes you might wish to write a function in which you don't initially know how many arguments the user will pass. 
# - In this case, you can use the special form \*args and \**kwargs to catch all arguments that are passed. Here is an example:
# 

# In[41]:


def catch_all(*args, **kwargs):
    print("args =", args)
    print("kwargs = ", kwargs)


# In[42]:


catch_all(1, 2, 3, a=4, b=5)


# In[43]:


catch_all('a', keyword=2)


# ### Asterisk
# 
# - In case of \*args and \**kwargs, it is not the names args and kwargs that are important, but the \* characters preceding them. 
# - args and kwargs are just the variable names often used by convention, short for "arguments" and "keyword arguments":
#     - a single \* before a variable means "expand this as a sequence", while a double 
#     - \** before a variable means "expand this as a dictionary". 
#     
# - This syntax can be used not only with the function definition, but with the function call as well:

# In[44]:


inputs = (1, 2, 3)
keywords = {'pi': 3.14}

catch_all(*inputs, **keywords)


# ### Anonymous (lambda) functions
# 
# - Defining short, one-off functions with the lambda statement (without using def):

# In[45]:


add = lambda x, y: x + y
add(1, 2)


# - This lambda function is roughly equivalent to:

# In[46]:


def add(x, y):
    return x + y


# - Functions can be passed as arguments to functions.
# - As an example of a lambda function passed as argument, suppose we have some data stored in a list of dictionaries:

# In[47]:


data = [{'first':'Guido', 'last':'Van Rossum', 'YOB':1956},
        {'first':'Grace', 'last':'Hopper',     'YOB':1906},
        {'first':'Alan',  'last':'Turing',     'YOB':1912}]


# - Now suppose we want to sort this data 
# - Python has a `sorted` function, which can order a list of integers, for example
# - But dictionaries are not orderable: we need a way to tell the function how to sort our data
# - We can do this by specifying the key function, a function which given an item returns the sorting key for that item:

# In[48]:


# sort alphabetically by first name
sorted(data, key=lambda item: item['first'])


# In[49]:


# sort by year of birth
sorted(data, key=lambda item: item['YOB'])


# ## Iterator syntax
# 
# Often an important piece of data analysis is repeating a similar calculation, over and over, in an automated fashion. 
# 
# ### Range
# 
# For example, you may have a table of a names that you'd like to split into first and last, or perhaps of dates that you'd like to convert to some standard format. 
# 
# One of Python's answers to this is the iterator syntax. We've seen this already with the range iterator:
# 

# In[50]:


for i in range(10):
    print(i, end=' ')


# range is not a list, but is something called an iterator, and learning how it works is key to understanding a wide class of very useful Python functionality.

# ## Iterating over lists
# 
# - Iterators are perhaps most easily understood in the concrete case of iterating through a list. 
# - Consider the following:

# In[51]:


for value in [2, 4, 6, 8, 10]:
    # Do some operation
    print(value)


# In[52]:


for i in range(10):
    print(i, end=' ')


# - The familiar "for x in y" syntax allows us to repeat some operation for each value in the list. 

# ### Enumerate
# 
# - Sometimes you need to iterate not only the values in an array, but also keep track of the index:

# In[53]:


L = [2, 4, 6, 8, 10]
for i, val in enumerate(L):
    print(i, val)


# ### Zip
# 
# - Other times, you may have multiple lists that you want to iterate over simultaneously. 
# - Use the zip iterator, which zips together iterables:

# In[54]:


L = [2, 4, 6, 8, 10]
R = [3, 6, 9, 12, 15]
for lval, rval in zip(L, R):
    print(lval, rval)


# ### Map
# 
# - The map iterator takes a function and applies it to the values in an iterator:

# In[55]:


# find the first 10 square numbers
square = lambda x: x ** 2

for val in map(square, range(10)):
    print(val, end=' ')


# In[56]:


print(*map(lambda x: x ** 2, range(10)))


# ### Filter
# 
# - The filter iterator looks similar, except it only passes-through values for which the filter function evaluates to True:

# In[57]:


# find values up to 10 for which x % 2 is zero
is_even = lambda x: x % 2 == 0

for val in filter(is_even, range(10)):
    print(val, end=' ')


# ### List comprehensions
# 
# - List comprehensions are a way to compress a list-building for-loop into a single short, readable line. 
# - For example, here is a loop that constructs a list of the first 12 square integers:

# In[58]:


L = []
for n in range(12):
    L.append(n ** 2)
L


# In[59]:


[n ** 2 for n in range(12)]


# ## Multiple iteration
# 
# - Sometimes you want to build a list not just from one value, but from two. 
# - To do this, simply add another for expression in the comprehension:

# In[60]:


[(i, j) for i in range(2) for j in range(3)]


# - Notice that the second for expression acts as the interior index, varying the fastest in the resulting list 
# - This type of construction can be extended to three, four, or more iterators within the comprehension

# ## Errors and Exceptions
# 
# - No matter your skill as a programmer, you will eventually make a coding mistake. Such mistakes come in three basic flavors:
# 
# 1. **Syntax** errors: Errors where the code is not valid Python (generally easy to fix)
# 
# 1. **Runtime** errors: Errors where syntactically valid code fails to execute, perhaps due to invalid user input (sometimes easy to fix)
# 
# 1. **Semantic** errors: Errors in logic: code executes without a problem, but the result is not what you expect (often very difficult to track-down and fix)
# 
# - In this section we are going to focus on how to deal cleanly with runtime errors. 
# - As we'll see, Python handles runtime errors via its exception handling framework.
# 

# ### Runtime errors
# 
# - If you've done any coding in Python, you've likely come across runtime errors. 
# - They can happen in a lot of ways. For example, if you try to reference an undefined variable:

# In[61]:


# print(Q)


# - Or if you try an operation that's not defined:

# In[62]:


# 1 + 'abc'


# - Or you might be trying to compute a mathematically ill-defined result:

# In[63]:


# 2 / 0


# - Note that in each case, Python is not simply indicate that an error happened, but also includes information about what exactly went wrong, along with the exact line of code where the error happened. 
# - Having access to meaningful errors like this is immensely useful when trying to trace the root of problems in your code.
