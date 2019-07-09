#Create a class
#class Persona:

#Constructor
#	def __init__(self, nombre, email, edad):
#		self.nombre = nombre
#		self.email = email
#		self.edad = edad

#	def saludo(self):
#		return 'Me llamo {0} y tengo {1}'.format(self.nombre, self.edad)

#Ini objeto para usuario
#Eduardo = Persona ('Eduardo', 'eduardo@gmail.com', 20)
#print(type(Eduardo))
#print(Eduardo.nombre)
#print(Eduardo.saludo())	  

class Cliente:

	def __init__(self, nombre, email, edad):
                self.nombre = nombre
                self.email = email
                self.edad = edad
		self.saldo = 0

	def establecerSaldo(self, saldo):
		self.saldo = saldo

	def saludo(self):
		return 'Me llamo {0} y tengo {1} y mi saldo es {2}'.format(self.nombre, self.edad, self.saldo)

#init Cliente
#Rufina_usuario = Usuario ('Rufina Madrid', 'rufina@hotmail.com', 200)
Rufina_cliente = Cliente('Rufina Madrid', 'rufina@hotmail.com', 200)
Rufina_cliente.establecerSaldo(50000)
#print(Rufina_usuario.saludo())
print(Rufina_cliente.saludo())


