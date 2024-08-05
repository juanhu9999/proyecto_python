#estan commpuestos por llaves y valores (amarillo es key y yellow valor)

colores = {"amarillo": "yellow", "azul": "blue"}

print(colores["amarillo"]) #me devuelve el valor

#mutar valor

colores["amarillo"] = "white"
print(colores["amarillo"])

#hacer operaciones

edades = {"juan": 26}

edades["juan"] +=5
print(edades)

# usar addd para agregar cosas

edades['pedro'] = 8
print(edades)

# los mismo con update

edades.update({'Carlos': 3, 'Luis': 4})
print(edades)

#Creando otro diccionario

otro_dict = dict(Angel=7)

edades.update(otro_dict)
print(edades)

#len

print(len(edades))

#diccionario prolijo y con saltos de linea

datos_personales = { "nombre": "Juan",
"Apellido": "Isabella",
"Edad": 37,
"Nacionalidad": "Argentina"}

print(datos_personales)

#Del elimina 

#se configura mi_dict["clave"]