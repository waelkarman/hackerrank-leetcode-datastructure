
def fibonacci(n,cache={}):
    if n in cache:
        return cache[n] 
    if n < 2:
        return 1
    
    cache[n] = fibonacci(n-1,cache)+fibonacci(n-2,cache)
    return cache[n]


print(fibonacci(4))
print(fibonacci(6))
print(fibonacci(7))
print(fibonacci(300)) 