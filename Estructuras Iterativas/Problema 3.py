# Contador de pares e impares

numeros= []
pares= 0
impares= 0

while True:

    ingreso= input ("¿Desea ingresar un número? (si/no): ")
    if ingreso.lower() == 'no':
         break

    elif ingreso == 'si':
        entrada= input("Ingrese el número: ")
        
        try:
             numero= int(entrada)
             numeros.append(numero)
             
        except ValueError:
             print ("Por favor, ingrese un número válido.")

    else:
         print ("Ingrese un número válido o escriba 'no' para finalizar.")

for numero in numeros:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1


print (f"\nNúmeros Ingresados: {numeros}")
print (f"Número Pares: {pares} ")
print (f"Números Impares: {impares}")






