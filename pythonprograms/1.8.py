# Iterators and Generators
# Generators are classes whose instances serve as iterators

def factors(n):
    results = []
    for k in range(1 ,n +1):
        if n%k == 0:
            results.append(k)
    return results

def factors_gen(n):
    for k in range(1 ,n +1):
        if n % k == 0:
            yield k

print([f for f in factors_gen(30)])

def fibonacci():
    a= 0
    b = 1
    while True:
        yield a
        future  = a+b
        a = b
        b = future

print(fibonacci())
