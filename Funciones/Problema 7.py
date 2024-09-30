# Todos los números perfectos menores a 1000

def es_perfecto(n):

    suma_divisores= 0

    for i in range(1, n):
        if n % i == 0:
            suma_divisores += i
    return suma_divisores == n

def perfectos_menores():

    perfectos= []

    for num in range(1, 1000):
        if es_perfecto(num):
            perfectos.append(num)
    return perfectos

perfectos= perfectos_menores()
print(f"Números perfectos menores a 1000: {perfectos}")