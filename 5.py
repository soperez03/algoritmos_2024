
'''
    TRABAJO NRO 1: Recursividad
        ejercicio nro 5:
            Desarrollar una función que permita convertir un número romano en un número decimal.
    Perez Sofia
'''

def conversion(numero):
    equivalencias = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000} #declaramos el diccionario con sus respectivas equivalencias 
    if numero == '':  #salida 1: si no se pasa un nro romano se devuelve 0
        return 0
    elif  numero == 1:  #salida 2: se supone que si contiene 1 digito el nro entonces estara declarado 
        return equivalencias[numero]
    else:
           return equivalencias[numero[0]] + conversion(numero[1:]) #se llama a la recursividad
    
print(conversion('C')) #en este caso devuelve 100. 
