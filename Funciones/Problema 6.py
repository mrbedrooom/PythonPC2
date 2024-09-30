# Serie de Fibonacci de 0 a 50

def fibonacci_serie(limite):

    a, b = 0, 1

    fibonacci= [a]

    while b<= limite:
        fibonacci.append(b)
        a, b= b, a+b

    return fibonacci

limite= 50

fibonacci_resultado=fibonacci_serie(limite)

print(fibonacci_resultado)