# Calculadora de número factorial

def calculo_factorial(n):

    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular_factorial(n - 1)

numero = int(input("Ingrese un número para calcular su factorial: "))

factorial = calcular_factorial(numero)
print(f"El factorial de {numero} es: {factorial}")
