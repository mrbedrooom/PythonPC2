# Convertir el formato de fechas

fecha_ingresada= input("Ingrese la fecha en formato mm/dd/aaaa: ")

def convertir_fecha(fecha):

    mes, dia, año = fecha.split('/')
    
    fecha_formateada = f"{año}-{int(mes):02}-{int(dia):02}"
    
    return fecha_formateada

fecha_salida= convertir_fecha(fecha_ingresada)

print (f"Fecha en el formato aaaa/mm/dd: {fecha_salida}")
