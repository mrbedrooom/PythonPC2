# Serie de Fibonacci de 0 a 50

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

n=50

item = fib(n)
print(f"La serie de Fibonacci del 0 al 50: {item}")