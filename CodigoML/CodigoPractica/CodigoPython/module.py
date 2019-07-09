#Importar modulo

#import datetime
#hoy = datetime.date.today()
#print(hoy)

#from datetime import date
#hoy2 = date.today()
#print(hoy2)

#import time
#estampatemporal = time.time()
#print(estampatemporal)

#from time import time
#estampatemporal2 = time()
#print(estampatemporal2)

#from camelcase import CamelCase

import validador
from validador import validate_email

email = 'pruebaprueba.com'
if validate_email(email):
	print('El correo es valido')
else:
	print('El correo es invalido')
