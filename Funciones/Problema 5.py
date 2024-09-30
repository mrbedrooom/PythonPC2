# Suma de números primos menores a 100

def numeros(primo):

    if primo <= 1:
        return False
    for i in range(2, int(primo**0.5)+1):
        if primo % i == 0:
            return False
    return True

def suma_primo(enésimo):
    total= 0
    
    for num in range(enésimo):
        if numeros(num):
            total += num
    return total

print (f"""La sumatoria de los números primos menores es: 
       {suma_primo(100)}""")

