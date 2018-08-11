# Conditional expressions
"""
result = foo(n if n >= 0 else -n)

Comprehension syntax
[expression for value in iterable if condition]
if clause in optional

"""
squares = [k*k for k in range(1, n+1)]
# factors
factors = [k for k in range(1, n+1) if n % k == 0]

# unpacking and packing sequences
a,b,c,d = range(7, 11)

def fibonacci():
    a,b = 0, 1
    while True:
        yield a
        a,b = b, a+b 
