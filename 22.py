
mochila = ('linterna', 'capa', 'sable de luz', 'alimento')
def usarLaFuerza(mochila, contador=0):
    if contador == len(mochila):
        print("Lamentablemente te has olvidado de cargar el sable de luz...")
        return -1
    elif mochila[contador] == 'sable de luz':
        print("¡Sable de luz encontrado!")
        return contador + 1
    else:
        print("Sacando", mochila[contador], "de la mochila...")
        return usarLaFuerza(mochila, contador + 1)


contador = usarLaFuerza(mochila)
if contador != -1:
    print("Se necesitaron", contador, "objetos para encontrar el sable.")
