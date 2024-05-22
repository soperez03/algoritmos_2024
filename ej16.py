'''

Se tienen dos pilas con personajes de Star Wars, en una los del episodio V
 de “The empire strikes back” y
   la otra los del episodio VII “The force awakens”. 
   Desarrollar un algoritmo que permita obtener la intersección 
   de ambas pilas, es decir los personajes que aparecen en ambos episodios. '''
'''


from pila import Stack

Ep5 = Stack()
Ep7 = Stack()

coincidencia = Stack()
Ep5= ['Luke Skywalker', 'Han Solo', 'Princesa Leia','Obi Wan Kenobi','C3PO','R2D2','Chewbacca','Darth Vader','Emperador Palpatine','Yoda','Lando','Capitan Lennox']
Ep7=['Rey','Finn','Poe Dameron','Kylo Ren','Han Solo','Princesa Leia','Chewbacca','BB-8','General Hux']
ep7 = []
print('Episodio V :',Ep5)
print()
coincidencia=[]
print('Episodio VII :',Ep7)
def interseccion (Ep5,Ep7,coincidencia):
  coincidencia=[]
  while  Ep7 is not None:
   Ep7.pop()
   ep7.append()
  ep5 = []
  while  Ep5 is not None:
   Ep5.pop()
   ep5.append()
 
  while Ep5 is not None:
   personaje = Ep5.pop()
   if personaje in Ep7:
   coincidencia.push(personaje)
  return coincidencia
intersectan=interseccion(Ep5,Ep7, coincidencia)
result = []
while intersectan is not None:
  result.append(intersectan.pop())

print(f'La intersección de personajes entre el Episodio V y el Episodio VII es: {result}')

'''
from pila import Stack
epV = Stack()
epVII = Stack()
for personaje in ['Luke Skywalker', 'Han Solo', 'Princesa Leia','Obi Wan Kenobi','C3PO','R2D2','Chewbacca','Darth Vader','Emperador Palpatine','Yoda','Lando','Capitan Lennox']:
 epV.push(personaje)
for personaje in ['Rey','Finn','Poe Dameron','Kylo Ren','Han Solo','Princesa Leia','Chewbacca','BB-8','General Hux']:
 epVII.push(personaje)
print('Los personajes de Ep V son: ', epV)
print()
print('los personajes de Episodio VII son: ', epVII)
def interseccion (epV_,epVII_):
  
  coinciden=[]
  while epV_.size() > 0: 
    personaje = epV_.pop()  
    if personaje in epVII_:
      coinciden.append(personaje)
  return coinciden
intersectan = interseccion(epV, epVII)
print(f' la interseccion se da con los siguientes personajes: {intersectan} ')
