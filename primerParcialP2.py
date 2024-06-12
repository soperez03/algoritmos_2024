
dinosaurios = [
    {
      "nombre": "Tyrannosaurus Rex",
      "especie": "Theropoda",
      "peso": 7000 ,
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1902
    },
    {
      "nombre": "Triceratops",
      "especie": "Ceratopsidae",
      "peso": 6000 ,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1889
    },
    {
      "nombre": "Velociraptor",
      "especie": "Dromaeosauridae",
      "peso": 15 ,
      "descubridor": "Henry Fairfield Osborn",
      "ano_descubrimiento": 1924
    },
    {
      "nombre": "Brachiosaurus",
      "especie": "Sauropoda",
      "peso": 56000 ,
      "descubridor": "Elmer S. Riggs",
      "ano_descubrimiento": 1903
    },
    {
      "nombre": "Stegosaurus",
      "especie": "Stegosauridae",
      "peso": 5000 ,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Spinosaurus",
      "especie": "Spinosauridae",
      "peso": 10000 ,
      "descubridor": "Ernst Stromer",
      "ano_descubrimiento": 1912
    },
    {
      "nombre": "Allosaurus",
      "especie": "Theropoda",
      "peso": 2000,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Apatosaurus",
      "especie": "Sauropoda",
      "peso": 23000 ,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Diplodocus",
      "especie": "Sauropoda",
      "peso": 15000 ,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1878
    },
    {
      "nombre": "Ankylosaurus",
      "especie": "Ankylosauridae",
      "peso": 6000,
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1908
    },
    {
      "nombre": "Parasaurolophus",
      "especie": "Hadrosauridae",
      "peso": 2500 ,
      "descubridor": "William Parks",
      "ano_descubrimiento": 1922
    },
    {
      "nombre": "Carnotaurus",
      "especie": "Theropoda",
      "peso": 1500,
      "descubridor": "José Bonaparte",
      "ano_descubrimiento": 1985
    },
    {
      "nombre": "Styracosaurus",
      "especie": "Ceratopsidae",
      "peso": 2700 ,
      "descubridor": "Lawrence Lambe",
      "ano_descubrimiento": 1913
    },
    {
      "nombre": "Therizinosaurus",
      "especie": "Therizinosauridae",
      "peso": 5000 ,
      "descubridor": "Evgeny Maleev",
      "ano_descubrimiento": 1954
    },
    {
      "nombre": "Pteranodon",
      "especie": "Pterosauria",
      "peso": 25 ,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1876
    },
    {
      "nombre": "Quetzalcoatlus",
      "especie": "Pterosauria",
      "peso": 200 ,
      "descubridor": "Douglas A. Lawson",
      "ano_descubrimiento": 1971
    },
    {
      "nombre": "Plesiosaurus",
      "especie": "Plesiosauria",
      "peso": 450 ,
      "descubridor": "Mary Anning",
      "ano_descubrimiento": 1824
    },
    {
      "nombre": "Mosasaurus",
      "especie": "Mosasauridae",
      "peso": 15000 ,
      "descubridor": "William Conybeare",
      "ano_descubrimiento": 1829
    },

  ]
pila=[]
'''
#a
def contadorDeEspecies(dinosaurios):
  cont=[]
  for especie in dinosaurios:
    pila.append(especie['especie'])
  while len(pila) > 0 :
    especie = pila.pop()
    cont.append(especie)
  return len(cont)

#b
def contadorDescubridores(dinosaurios):
  descubridores=[]
  pila2=[]
  for descubridor in dinosaurios:
    pila2.append(descubridor['descubridor'])
  while len(pila2) > 0 :
    descubridor= pila2.pop()
    if descubridor not in descubridores:
      descubridores.append(descubridor)
  return len(descubridores)


contador=contadorDeEspecies(dinosaurios)
contador2=contadorDescubridores(dinosaurios)
print(f'la cant de descubridores es de {contador2}')
print(f' La cant de especies es de {contador}')

#c
def comienzaConT (dinosaurios):
  conT=[]
  for dinosaurio in dinosaurios:
    if dinosaurio['nombre'].startswith('T'):
      conT.append(dinosaurio['nombre'])
  return (conT)

nombresConT=comienzaConT(dinosaurios)
print(f'los dinos q comienzan con t son {nombresConT}')

#d
def comanMas(dinosaurios):
  delgaditos=[]
  for dinosaurio in dinosaurios:
    if dinosaurio['peso'] < 275:
      delgaditos.append(dinosaurio['nombre'])
  return(delgaditos)

flacos=comanMas(dinosaurios)
print(f'los dinosaurios que se encuentran en 275 kg son: {flacos}')'''


def iniciales(dinosurios):
  pila_aux=[]
  for dinosaurio in dinosaurios:
    if dinosaurio['nombre'].startswith('A'):
      pila_aux.append(dinosaurio['nombre'])
    else:
        if dinosaurio['nombre'].startswith('Q'):
          pila_aux.append(dinosaurio['nombre'])
    if dinosaurio['nombre'].startswith('S'):
      pila_aux.append(dinosaurio['nombre'])
  return pila_aux

empiezaCon= iniciales(dinosaurios)
print(f'Los dinosaurios que comienzan con <A>,<Q>,<S> son: {empiezaCon}')