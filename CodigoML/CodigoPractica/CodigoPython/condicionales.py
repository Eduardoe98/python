x = 1
y = 10
z = 15

if x > y:
	print ('{0} es mas grande que {1}'.format(x,y))

#else:
#	print(y)

elif x==y:
	print('{0} y {1} son iguales'.format (x, y))
elif x<y:
	print ('{1} es mas grande que {0}'.format(x,y))

if x<y and z>y:
        print ('{1} es mas grande que {0} y {2} es mas grande que {1}'.format(x,y,z))

