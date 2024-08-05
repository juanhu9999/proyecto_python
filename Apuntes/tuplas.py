# es similar a la lista pero son inmutables, solo se puede agregar algo concatenando

mi_tupla = (1, 2, 3, 4, 5)
print(mi_tupla)

#concatenacion
mi_tupla += (5, 6, 7, 8)
print(mi_tupla)

#con un unico valor incluir coma

unico_valor = (2,)
print(unico_valor)

# funciones de tuplas

#len
print(len(mi_tupla))

#count

print(mi_tupla.count(5))

#index

print(mi_tupla.index(5))

tupla_anidada = ([1, 2, "hola"], "avions, 3")

lista_anidada = [(1, 2), "adios"]

print(tupla_anidada, lista_anidada)
print(tupla_anidada[0][1]) #el [1] para buscar dentro de las lista
print(lista_anidada[1])

#convertir listas a tuplas y viceversa

tupla_anidada = list(tupla_anidada)

print(tupla_anidada)

lista_anidada = tuple(lista_anidada)
print(lista_anidada)
