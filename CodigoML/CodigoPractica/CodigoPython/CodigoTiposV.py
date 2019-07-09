#Codigo para saber el tipo de dato

#declaracion
x = 3
y = 2.2

#operacion
a = x + y

#tipo de dato
print('Los tipos de dato son:')
print(type(x))
print(type(y))
print(type(a))

#Cambiar el tipo de dato
x = str(x) #Cambiar entero a cadena
y = int(y) #Cambiar decimal a entero
z = float(y)

print(type(x),x)
print(type(y),y)
print(type(z),z)
