'''15. Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, can-
tidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. Y ade-
más la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver
las siguientes actividades utilizando lista de lista implementando las funciones necesarias:
a. obtener la cantidad de Pokémons de un determinado entrenador;
b. listar los entrenadores que hayan ganado más de tres torneos;

c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
d. mostrar todos los datos de un entrenador y sus Pokémos;
e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
(tipo y subtipo);
g. el promedio de nivel de los Pokémons de un determinado entrenador;
h. determinar cuántos entrenadores tienen a un determinado Pokémon;
i. mostrar los entrenadores que tienen Pokémons repetidos;

j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Te-
rrakion o Wingull;

k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
deberán mostrar los datos de ambos;'''
from lista2 import show_list_list, by_name, search
from random import choice
pokemones=[
    {
        "nombre": "Pikachu",
        "nivel": 35,
        "tipo": "Eléctrico",
        "subtipo": None
    },
    {
        "nombre": "Charizard",
        "nivel": 40,
        "tipo": "Fuego",
        "subtipo": "Volador"
    },
    {
        "nombre": "Bulbasaur",
        "nivel": 30,
        "tipo": "Planta",
        "subtipo": "Veneno"
    },
    {
        "nombre": "Starmie",
        "nivel": 30,
        "tipo": "Agua",
        "subtipo": "Psíquico"
    },
    {
        "nombre": "Psyduck",
        "nivel": 25,
        "tipo": "Agua",
        "subtipo":None
    },
    {
        "nombre": "Gyarados",
        "nivel": 35,
        "tipo": "Agua",
        "subtipo": "Volador"
    },
    {
        "nombre": "Onix",
        "nivel": 38,
        "tipo": "Roca",
        "subtipo": "Tierra"
    },
    {
        "nombre": "Geodude",
        "nivel": 28,
        "tipo": "Roca",
        "subtipo": "Tierra"
    },
    {
        "nombre": "Vulpix",
        "nivel": 20,
        "tipo": "Fuego",
        "subtipo":None
    },
    {
        "nombre": "Blastoise",
        "nivel": 50,
        "tipo": "Agua",
        "subtipo": None
    },
    {
        "nombre": "Umbreon",
        "nivel": 45,
        "tipo": "Siniestro",
        "subtipo": None
    },
    {
        "nombre": "Nidoking",
        "nivel": 40,
        "tipo": "Veneno",
        "subtipo": "Tierra"
    }]
entrenadores = [
{
"nombre": "Ash Ketchum",
"torneos_ganados": 7,
"batallas_perdidas": 50,
"batallas_ganadas": 120
},
{
"nombre": "Goh",
"torneos_ganados": 2,
"batallas_perdidas": 10,
"batallas_ganadas": 40
},
{
"nombre": "Leon",
"torneos_ganados": 10,
"batallas_perdidas": 5,
"batallas_ganadas": 100
},
{
"nombre": "Chloe",
"torneos_ganados": 1,
"batallas_perdidas": 8,
"batallas_ganadas": 30
},
{
"nombre": "Raihan",
"torneos_ganados": 4,
"batallas_perdidas": 15,
"batallas_ganadas": 60
}
]

names = ["Ash Ketchum", "Goh", "Leon", "Chloe", "Raihan"]

lista_entrenadores = []

for entrenador in entrenadores:
    entrenador.update({'sublist': []})
    lista_entrenadores.append(entrenador)

for pokemon in pokemones:
    pos = search(lista_entrenadores, 'nombre', choice(names))
    if pos is not None:
        lista_entrenadores[pos]['sublist'].append(pokemon)
    else:
        print('no existe el entrenador')

lista_entrenadores.sort(key=by_name)
show_list_list('Entrenadores', 'Pokemones', lista_entrenadores)
#b
torneosMasTres=[]
for entrenador in entrenadores:
    if entrenador["torneos_ganados"]>3:
        print()
        torneosMasTres.append(f'{entrenador['nombre']}: {entrenador['torneos_ganados']}')
print('los siguientes entreadores han ganado mas de tres torneos')
print(torneosMasTres)
'''
#c  el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
#?, falta relacionar bien el pokemon max

torneosMas=0
pokemonMax=0
for entrenador in entrenadores:
    if entrenador['torneos_ganados']>torneosMas:
        torneosMas=entrenador['torneos_ganados']
        torneosMas=entrenador
        pokemonMax=entrenador['pokemons']
        for pokemon in entrenador['pokemons']:
            if pokemon['nivel'] > pokemonMax['nivel']:
                pokemonMax= pokemon'''
#d. mostrar todos los datos de un entrenador y sus Pokémos;
#en la lista no se relacionan pokemons y entrenador

#e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
for entrenador in entrenadores:
    apto=[]
    total= entrenador["batallas_ganadas"] + entrenador['batallas_perdidas']

    porcentaje= entrenador['batallas_ganadas'] / total * 100
    if porcentaje > 79:
        apto.append({"nombre": entrenador["nombre"], "porcentaje": porcentaje})
print(f'los entrenadores cuyo porcentaje supera el 79% son: {apto}')
 #f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
#(tipo y subtipo) adaptado a las listas dadas;
 
for pokemon in pokemones:
    FYP=[]
    if pokemon['tipo'] == 'Fuego' and pokemon['subtipo'] == 'Planta':
        FYP.append({'nombre': pokemon['nombre'], 'tipo': pokemon['tipo'], 'subtipo': pokemon['subtipo']})
print(f'los siguientes pokemones tienen de tipo fuego y subtipo  planta {FYP} ')

for pokemon in pokemones:
    AyV=[]
    if pokemon['tipo'] == 'Agua' and pokemon['subtipo']== 'Volador':
        AyV.append({'nombre' : pokemon['nombre'], 'tipo': pokemon['tipo'], 'subtipo':pokemon['subtipo']})
print(f'los siguientes poemones tienen tip agua y subtipo volador { AyV}')
#g. el promedio de nivel de los Pokémons de un determinado entrenador;
for pokemon in pokemones:
    total_pokemones= len(pokemones)
    porcen_poke= pokemon['nivel']/total_pokemones * 100
print(f'el promedio de los niveles de los pokemones dados es de : { porcen_poke}')
'''
j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Te-
rrakion o Wingull;
'''
aparece= False
for pokemon in pokemones:
    if pokemon['nombre']== 'Tyrantrum' or pokemon['nombre']== 'Terrakion' or pokemon['nombre'] == 'Wingull':
        aparece=True
if aparece == True:
    print(f'el pokemon: {pokemon['nombre']} se encuentra en la lista de pokemones')
else:
    print('ninguno aparece')

'''
k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
deberán mostrar los datos de ambos
'''

buscado=str(input('ingrese pokemon  a buscar: '))
buscarEntrenador= str(input(' ingrese entrenador a buscar: '))
for pokemon in pokemones:
    if buscado == pokemon['nombre']:
        print(' se ha encontrado.')
if buscarEntrenador in entrenadores:
   print (f'su busqueda se ha realizado correctamente')
print(f' {buscado} es pokemon de {buscarEntrenador}')