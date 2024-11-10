'''23. Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
resuelva las siguientes consultas:
a. listado inorden de las criaturas y quienes la derrotaron;
b. se debe permitir cargar una breve descripción sobre cada criatura;
c. mostrar toda la información de la criatura Talos;

[169]

d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
e. listar las criaturas derrotadas por Heracles;
f. listar las criaturas que no han sido derrotadas;
g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
o dios que la capturo;
h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
Erimanto indicando que Heracles las atrapó;
i. se debe permitir búsquedas por coincidencia;
j. eliminar al Basilisco y a las Sirenas;
k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
derroto a varias;
l. modifique el nombre de la criatura Ladón por Dragón Ladón;
m. realizar un listado por nivel del árbol;
n. muestre las criaturas capturadas por Heracles.'''



from cola import Queue

class BinaryTree:

    class __Node:
        def __init__(self, value, left=None, right=None, other_value=None, descripcion=None, capturada = None):
            self.value = value
            self.left = left
            self.right = right
            self.other_value = other_value
            self.descripcion = descripcion
            self.capturada = capturada 

    def __init__(self):
        self.root = None
    
    def insert_node(self, value, other_value=None, descripcion=None, capturada = None):
        def _insert(root, value, other_value=None, descripcion=None, capturada = None):
            if root is None:
                return BinaryTree.__Node(value, other_value=other_value, descripcion=descripcion, capturada = capturada)
            elif value < root.value:
                root.left = _insert(root.left, value, other_value, descripcion, capturada = capturada)
            else:
                root.right = _insert(root.right, value, other_value, descripcion,  capturada)
            return root

        self.root = _insert(self.root, value, other_value, descripcion, capturada = capturada)


    
    def search(self, key):
        def __search(root, key):
            if root is not None:
                if root.value == key:
                    # print('lo encontre')
                    return root
                elif key < root.value:
                    # print(f'buscalo a la izquierda de {root.value}')
                    return __search(root.left, key)
                else:
                    # print(f'buscalo a la derecha de {root.value}')
                    return __search(root.right, key)
            # else:
            #     print('no hay nada')
        aux = None
        if self.root is not None:
            aux = __search(self.root, key)
        return aux

    def preorden(self):
        def __preorden(root):
            if root is not None:
                print(root.value)
                # print(f'izquierda de {root.value}')
                __preorden(root.left)
                # print(f'derecha de {root.value}')
                __preorden(root.right)

        if self.root is not None:
            __preorden(self.root)

    def contar_super_heroes(self):
        def __contar_super_heroes(root):
            counter = 0
            if root is not None:
                if root.other_value.get('is_hero') is True:
                    counter = 1
                counter += __contar_super_heroes(root.left)
                counter += __contar_super_heroes(root.right)
            return counter

        return __contar_super_heroes(self.root)

    def inorden(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                print(f"Nombre: {root.value}, Derrotado por: {root.other_value}, Descripción: {root.descripcion}, captuda : {root.capturada}")
                __inorden(root.right)

        if self.root is not None:
            __inorden(self.root)

    def postorden(self):
        def __postorden(root):
            if root is not None:
                __postorden(root.right)
                print(root.value)
                __postorden(root.left)

        if self.root is not None:
            __postorden(self.root)

    def inorden_villanos(self):
        def __inorden_villanos(root):
            if root is not None:
                __inorden_villanos(root.left)
                if root.other_value.get('is_hero') is not True:
                    print(root.value)
                __inorden_villanos(root.right)

        if self.root is not None:
            __inorden_villanos(self.root)

    def inorden_superheros_start_with(self, start):
        def __inorden_superheros_start_with(root, start):
            if root is not None:
                __inorden_superheros_start_with(root.left, start)
                if root.other_value.get('is_hero') is True and root.value.startswith(start):
                    print(root.value)
                __inorden_superheros_start_with(root.right, start)

        if self.root is not None:
            __inorden_superheros_start_with(self.root, start)

    def by_level(self):
        pendientes = Queue()
        if self.root is not None:
            pendientes.arrive(self.root)

        while pendientes.size() > 0:
            node = pendientes.attention()
            print(node.value)
            if node.left is not None:
                pendientes.arrive(node.left)
            if node.right is not None:
                pendientes.arrive(node.right)

    def delete_node(self, value):
        def __replace(root):
            if root.right is None:
                # print(f'no tiene derecha es el mayor {root.value}')
                return root.left, root
            else:
                # print('seguir buscando nodo par remplaz+ar a la dercha')
                root.right, replace_node = __replace(root.right)
                return root, replace_node

        def __delete(root, value):
            value_delete = None
            if root is not None:
                if root.value > value:
                    # print(f'buscar  a la izquierda de {root.value}')
                    root.left, value_delete = __delete(root.left, value)
                elif root.value < value:
                    # print(f'buscar  a la derecha de {root.value}')
                    root.right, value_delete = __delete(root.right, value)
                else:
                    # print('valor encontrado')
                    value_delete = root.value
                    if root.left is None:
                        # print('a la izquierda no hay nada')
                        return root.right, value_delete
                    elif root.right is None:
                        # print('a la derecha  no hay nada')
                        return root.left, value_delete
                    else:
                        # print('tiene ambos hijos')
                        root.left, replace_node = __replace(root.left)
                        root.value = replace_node.value
                        return root, value_delete
                
            return root, value_delete

        delete_value = None
        if self.root is not None:
            self.root, delete_value = __delete(self.root, value)
        return 
    def contar_villanos(self):
        def __contar_villanos(root):
            counter = 0
            if root is not None:
                if root.other_value.get('is_hero') is False:
                    counter = 1
                counter += __contar_villanos(root.left)
                counter += __contar_villanos(root.right)
            return counter

        return __contar_villanos(self.root)
    def proximity_search(self, search_value):
        def __proximity_search(root, search_value):
            if root is not None:
                __proximity_search(root.left, search_value)
                if root.value.startswith(search_value):
                    print(root.value)
                __proximity_search(root.right, search_value)

        if self.root is not None:
            __proximity_search(self.root, search_value)

   
tree= BinaryTree()
criaturas = [
    {"nombre": "Ceto", "derrotado por": "", "descripcion": "Diosa primordial del mar", "capturada": ""},
    {"nombre": "Tifón", "derrotado por": "Gigante de las tormentas", "descripcion": "Criatura monstruosa con múltiples cabezas", "capturada": ""},
    {"nombre": "Equidna", "derrotado por": "Madre de todas las criaturas", "descripcion": "Ser mitad mujer, mitad serpiente", "capturada": ""},
    {"nombre": "Dino", "derrotado por": "", "descripcion": "Una de las hermanas Griegas del destino", "capturada": ""},
    {"nombre": "Pefredo", "derrotado por": "", "descripcion": "Hermana de Dino y Enio", "capturada": ""},
    {"nombre": "Enio", "derrotado por": "", "descripcion": "Hermana de Pefredo y Dino", "capturada": ""},
    {"nombre": "Escila", "derrotado por": "", "descripcion": "Monstruo marino de múltiples cabezas", "capturada": ""},
    {"nombre": "Caribdis", "derrotado por": "", "descripcion": "Monstruo marino que genera remolinos", "capturada": ""},
    {"nombre": "Euríale", "derrotado por": "", "descripcion": "Una de las gorgonas, hermana de Medusa", "capturada": ""},
    {"nombre": "Águila del Cáucaso", "derrotado por": "", "descripcion": "Águila que devoraba el hígado de Prometeo", "capturada": ""},
    {"nombre": "Quimera", "derrotado por": "", "descripcion": "Criatura con cabeza de león, cabra y cola de serpiente", "capturada": ""},
    {"nombre": "Hidra de Lerna", "derrotado por": "Heracles", "descripcion": "Serpiente de múltiples cabezas, derrotada por Heracles", "capturada": "Heracles"},
    {"nombre": "León de Nemea", "derrotado por": "Heracles", "descripcion": "León con piel invulnerable, derrotado por Heracles", "capturada": "Heracles"},
    {"nombre": "Esfinge", "derrotado por": "", "descripcion": "Criatura con cuerpo de león y rostro humano que proponía acertijos", "capturada": ""},
    {"nombre": "Dragón de la Cólquida", "derrotado por": "", "descripcion": "Dragón que custodiaba el vellocino de oro", "capturada": ""},
    {"nombre": "Cerbero", "derrotado por": "", "descripcion": "Perro de tres cabezas que custodia el Hades", "capturada": ""},
    {"nombre": "Jabalí de Erimanto", "derrotado por": "Heracles", "descripcion": "Jabalí capturado por Heracles", "capturada": "Heracles"},
    {"nombre": "Cerda de Cromión", "derrotado por": "", "descripcion": "Creador de destrucción en Cromión", "capturada": ""},
    {"nombre": "Toro de Creta", "derrotado por": "Heracles", "descripcion": "Toro capturado por Heracles", "capturada": "Heracles"},
    {"nombre": "Minotauro de Creta", "derrotado por": "Teseo", "descripcion": "Criatura con cuerpo de hombre y cabeza de toro, derrotado por Teseo", "capturada": "Teseo"},
    {"nombre": "Medusa", "derrotado por": "Perseo", "descripcion": "Gorgona que convertía en piedra con la mirada, derrotada por Perseo", "capturada": "Perseo"},
    {"nombre": "Ladón", "derrotado por": "", "descripcion": "Dragón que custodiaba las manzanas de oro", "capturada": ""},
    {"nombre": "Aves del Estínfalo", "derrotado por": "Heracles", "descripcion": "Aves con plumas de metal, enfrentadas por Heracles", "capturada": "Heracles"},
    {"nombre": "Sirenas", "derrotado por": "", "descripcion": "Criaturas que atraían a los marineros con su canto", "capturada": ""},
    {"nombre": "Basilisco", "derrotado por": "", "descripcion": "Rey de las serpientes, capaz de matar con la mirada", "capturada": ""},
    {"nombre": "Talos", "derrotado por": "Egeo", "descripcion": "Gigante de bronce que protege Creta", "capturada": "Egeo"},
    {"nombre": "Pitón", "derrotado por": "Apolo", "descripcion": "Serpiente gigante, derrotada por Apolo", "capturada": "Apolo"},
    {"nombre": "Cierva de Cerinea", "derrotado por": "Heracles", "descripcion": "Cierva sagrada de Artemisa, capturada por Heracles", "capturada": "Heracles"},
    {"nombre": "Argos Panoptes", "derrotado por": "", "descripcion": "Gigante con múltiples ojos", "capturada": ""},
    {"nombre": "Jabalí de Calidón", "derrotado por": "", "descripcion": "Jabalí enorme enfrentado en la cacería de Calidón", "capturada": ""}
]


for criatura in criaturas:
    tree.insert_node(criatura["nombre"], 
                     other_value=criatura["derrotado por"], 
                     descripcion=criatura["descripcion"], 
                     )
#tree.inorden()
buscado = 'Talos'
resultado = tree.search(buscado)
if resultado:
    print(f'la informacion de {buscado} es ')
    print(f'nombre: {resultado.value}')
    print(f'derrotado por: {resultado.other_value}')

    print(f'descripción: {resultado.descripcion}')
print()
'''
d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
e. listar las criaturas derrotadas por Heracles;
f. listar las criaturas que no han sido derrotadas;
g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
o dios que la capturo;'''

derrotadosPorH = []
noDerrotados=[]
for criatura in criaturas:
    if criatura['derrotado por'] == 'Heracles':
        derrotadosPorH.append(criatura['nombre'])

    if criatura['derrotado por'] == '':
        noDerrotados.append(criatura['nombre'])

print(f'los derrotados por heracles son {derrotadosPorH}')
print()
print(f'y estos son los que nadie a podido derrotar {noDerrotados}')
'''h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
Erimanto indicando que Heracles las atrapó;
i. se debe permitir búsquedas por coincidencia;
j. eliminar al Basilisco y a las Sirenas;
k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
derroto a varias;
l. modifique el nombre de la criatura Ladón por Dragón Ladón;
m. realizar un listado por nivel del árbol;
n. muestre las criaturas capturadas por Heracles.'''


nodo_cerbero = tree.search("Cerbero")
if nodo_cerbero:
    nodo_cerbero.capturada = "Heracles"
    print("Cerbero ha sido capturado por Heracles.")

nodo_toro_creta = tree.search("Toro de Creta")
if nodo_toro_creta:
    nodo_toro_creta.capturada = "Heracles"
    print("Toro de Creta ha sido capturado por Heracles.")

nodo_cierva_cerinea = tree.search("Cierva de Cerinea")
if nodo_cierva_cerinea:
    nodo_cierva_cerinea.capturada = "Heracles"
    print("Cierva de Cerinea ha sido capturada por Heracles.")

nodo_jabali_erimanto = tree.search("Jabalí de Erimanto")
if nodo_jabali_erimanto:
    nodo_jabali_erimanto.capturada = "Heracles"
    print("Jabalí de Erimanto ha sido capturado por Heracles.")
'''punto i'''
tree.proximity_search('Jab')
'''punto j'''
tree.delete_node('Basilisco')
tree.delete_node('Sirenas')
#print(criaturas)
'''k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
derroto a varias;'''
nodo_aves = tree.search("Aves del Estínfalo")
if nodo_aves:
    nodo_aves.other_value = 'heracles las derroto varias veces'
#print(criaturas)
''' l '''
nodo_ladon = tree.search("Ladón")
if nodo_ladon:
    nodo_ladon.value = 'Dragón Ladón'

'''punto m'''
tree.by_level()

print()
'''ultimo (n)'''
capturadosPorHeracles = []
for criatura in criaturas:
    if criatura['capturada'] == 'Heracles':
        capturadosPorHeracles.append(criatura['nombre'])

print(f'Los capturados por Heracles son: {capturadosPorHeracles}')
