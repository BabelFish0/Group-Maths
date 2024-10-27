## Functions

`def` keyword defines function which can take inputs like below. The function has to contain something which has to be indented. `pass` can be used to do nothing.

```python
def function(input1, input2):
    pass
```

To run the code in a function, you 'call' it. You have to provide all the parameters (called 'arguments' or 'args') it needs:

```python
function() # Will error because it needs two arguments
function(0, 0) # Runs the function and does nothing
```

Functions can have default parameters, specified like this:

```python
def function(input1=0, input2=1):
    pass
```

If we don't give the function inputs when we call it it will then default to these values. When you give arguments default values all the arguments to the right of it need to have default values. So:

```python
def f(a=0, b): # is not allowed;
    pass

def f(a, b=0): # is allowed.
    pass
```

When you call a function it runs whatever is inside the function. By default variables outside the function cannot be accessed from within the function (and vice versa). The main use of functions is with the `return` keyword which allows the function to output a value.

```python
def f():
    return 0 # super simple function always outputs 0.
```

When the function is called, we assign its value to a variable as follows:

```python
a = f()
print(a) # -> outputs 0
```
When the function is called it acts as the output data type. So we can do operations directly to the function:
```python
b = f() + f() + 8 * f() + f() ** 2 # etc.
```

When a python file is run, the `__name__` variable (a special variable) is automatically populated. We often pack the whole code into one function and call it only if this Python file is the one being run to avoid issues with multiprocessing or when we import the file as a module in another .py file.

```python
# In: ../file1.py
def f():
    print('Function running...')

if __name__ == 'main':
    f()
```
If we run `file1.py` we get the output 'Function running...'

Now if I access this from another file by importing it:

```python
# In: ../file2.py
import file1
```
Now nothing runs since the `__name__` variable is not `'__main__'`.