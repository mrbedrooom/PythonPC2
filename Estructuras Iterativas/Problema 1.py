# Divisibles por 7 y múltiplos de 5

selec_num= []

for i in range(1500, 2700):
    if i % 7 == 0 and i % 5 == 0:
        selec_num.append(i)

print ("\nLos números divisibles por 7 y múltiplos de 5 en el intervalo"
       " de 1500 a 2700 son: ")
print (f"\n{selec_num}")


