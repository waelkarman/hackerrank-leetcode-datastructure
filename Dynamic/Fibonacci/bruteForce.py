

def fibonacci(n):
    if n < 2:
        return 1
    
    return fibonacci(n-1)+fibonacci(n-2)



print(fibonacci(4))
print(fibonacci(6))
print(fibonacci(7))
print(fibonacci(300)) #critical