

def fibonacciTab(n):
    f=[0 for _ in range(n+1)]
    f[1]=1
    for i in range(len(f)-1):
        if i+1 <= n:
            f[i+1]=f[i+1]+f[i]
        if i+2 <= n:
            f[i+2]=f[i+2]+f[i]

    print(f)
    return f[len(f)-1]

print(fibonacciTab(8))