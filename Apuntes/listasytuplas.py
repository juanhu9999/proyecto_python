#listas y tuplas

# listas, los items de las listas son mutables, se pueden incluir cualquier tipo de dato, siempre llevan corchetes

mi_lista = [-11, 20, 3, 41]
otra_lista = ["Hola", "como", "estas", "?"]
print(mi_lista)
print(mi_lista[2])
print(mi_lista[-1])
print(mi_lista[-2:])
mi_lista += [1, "hola"]
print(mi_lista)

#listas mutables

pares = [2,4]
pares[1] = 3
print(pares)

# funciones integradas en las listas

# append (agregar item al final de la lista)

pares_1 = [2,4]
pares_1.append(6)
print(pares_1)

#insert(indice, valor)

pares_1.insert(1, 10)
print(pares_1)

#el uso de len en listas sirve para marcar los items
print(len(pares_1))

#pop elimina el ultimo item de la lista

pares_1.pop(1)
print(pares_1)

#count cuenta cuantas veces esta un elemento, si no lo encuentra devuelve cero
numeros = [1,2,3,4,1]
print(numeros.count(1))

#Index para saber en que indice esta un elemento devuelve al primero que encuentra si se repite despues no lo devuelve

print(numeros.index(2))



