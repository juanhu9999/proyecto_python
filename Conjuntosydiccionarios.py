#Conjuntos una coleccion no ordenada de objetos unicos, no tienen un orden especifico y no incluyen al ejecutarlo valores repetidos de cualquier tipo de dato que sea. No se puede trabajar con indice o slicing por que esta todo desordenado, tampoco puede incluir lista, tuplas u otros conjuntos.

conjunto = {1, 2, 3, 4, "hola", }
conjunto_vacio = set()

#otra forma de crear conjuntos

set = set(range(8))
print(set)

#convertir a lista o al reves

mi_lista = list({1,2,3})
print(mi_lista)


#los conjuntos son utiles para trabajar con elementos unicos

#agregar un elemento

numeros = {1,2,3}
numeros.add(5) #se pueden usar operaciones matematicas tambien
print(numeros)

#actualizar el set

numeros.update([28, "Hola"], range(9,20))
print(numeros)

#eliminar un item, remove() hace lo mismo pero si el valor no existe devuelve un error.
numeros.discard(10)
print(numeros)

#in o not in con true or false responde si esta o no

print(2 in numeros)

print(1000 not in numeros)

#Eliminar todos los posibles valores

numeros.clear()
print(numeros)

#Pop, no se usa mucho

