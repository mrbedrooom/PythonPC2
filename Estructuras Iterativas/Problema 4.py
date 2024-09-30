# Calificaciones de los alumnos

alumnos= []
notas= []

while True:
    nombre= input("Ingrese el nombre del alumno o escriba 'fin': ").lower()
    if nombre == 'fin':
        break

    for i in range(3):
        nota= float(input(f"Ingrese la nota {i+1} para {nombre}: "))
        notas.append(nota)
    alumnos.append({'nombre':nombre, 'notas': notas})

print ("\n\n*Reporte de notas - Alumnos del 5B*\n")
for alumno in alumnos:
    print(f"Alumno: {alumno['nombre']} \nNotas: {alumno['notas']}\n")
