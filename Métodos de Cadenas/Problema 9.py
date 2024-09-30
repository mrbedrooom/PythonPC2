# Remueve vocales

def elimina_vocales(cadena):

    vocales = "aeiouAEIOU"
    
    resultado = "".join([letra for letra in cadena if letra not in vocales])
    
    return resultado

texto = input("Ingrese una cadena de texto: ")

texto_sin_vocales = elimina_vocales(texto)
print("Texto sin vocales:", texto_sin_vocales)
